import os
import math
import dill
import re
from operator import itemgetter

INDEX_FILE = "Pickles/index.pkl"
STATS_FILE = "Pickles/stats.pkl"
DOC_MAP_FILE = "Pickles/doc_to_id.pkl"
QUERY_FILE = "cran.query"
OUTPUT_DIR = "results"

os.makedirs(OUTPUT_DIR, exist_ok=True)

index = dill.load(open(INDEX_FILE, "rb"))
stats = dill.load(open(STATS_FILE, "rb"))

V = stats["V"]
N = stats["N"]

doc_to_id = dill.load(open(DOC_MAP_FILE, "rb"))
id_to_doc = {v: k for k, v in doc_to_id.items()}

def tokenize(text):
    return re.findall(r"[a-z0-9]+(?:\.[a-z0-9]+)*", text.lower())

def load_queries(path):
    queries = {}
    qid = None
    buffer = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith(".I"):
                if qid is not None:
                    queries[qid] = " ".join(buffer)
                qid = line.split()[1]
                buffer = []

            elif line.startswith(".W"):
                continue
            else:
                buffer.append(line)

        if qid is not None:
            queries[qid] = " ".join(buffer)

    return queries

queries = load_queries(QUERY_FILE)

k1 = 1.2
b = 0.75

avg_doc_len = sum(index[t]["postings"][d]["doc_len"]
                  for t in index
                  for d in index[t]["postings"]) / N


def bm25(query_terms):
    scores = {}

    for term in query_terms:
        if term not in index:
            continue

        df = index[term]["df"]
        idf = math.log((N - df + 0.5) / (df + 0.5) + 1)

        for doc_id, info in index[term]["postings"].items():
            tf = info["tf"]
            doc_len = info["doc_len"]

            denom = tf + k1 * (1 - b + b * (doc_len / avg_doc_len))
            score = idf * ((tf * (k1 + 1)) / denom)

            scores[doc_id] = scores.get(doc_id, 0) + score

    return sorted(scores.items(), key=itemgetter(1), reverse=True)

def tfidf(query_terms):
    scores = {}

    for term in query_terms:
        if term not in index:
            continue

        df = index[term]["df"]
        idf = math.log10(N / df)

        for doc_id, info in index[term]["postings"].items():
            tf = info["tf"]
            score = tf * idf
            scores[doc_id] = scores.get(doc_id, 0) + score

    return sorted(scores.items(), key=itemgetter(1), reverse=True)

def laplace(query_terms):
    scores = {}

    for doc_id in range(N):
        score = 0

        for term in query_terms:
            if term in index and doc_id in index[term]["postings"]:
                tf = index[term]["postings"][doc_id]["tf"]
                doc_len = index[term]["postings"][doc_id]["doc_len"]
            else:
                tf = 0
                doc_len = avg_doc_len

            prob = (tf + 1) / (doc_len + V)
            score += math.log(prob)

        scores[doc_id] = score

    return sorted(scores.items(), key=itemgetter(1), reverse=True)

def write_results(qid, results, filename):
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "a") as f:
        for rank, (doc_id, score) in enumerate(results[:100], start=1):
            f.write(f"{qid} Q0 {doc_id} {rank} {score} Exp\n")

print(f"Loaded {len(queries)} queries")

for qid, text in queries.items():

    query_terms = tokenize(text)

    print("Processing Query:", qid)

    write_results(qid, bm25(query_terms), "bm25.txt")
    write_results(qid, tfidf(query_terms), "tfidf.txt")
    write_results(qid, laplace(query_terms), "laplace.txt")

print("DONE")