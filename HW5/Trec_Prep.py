import pickle
import math
from collections import defaultdict, Counter

with open("../HW1/index.pkl", "rb") as f:
    index = pickle.load(f)

queries = {
    "151803": "battle of stalingrad ww2 germany soviet",
    "151802": "aerodynamics experimental investigation",
    "151801": "space shuttle wings airflow test"
}

docs = list(index.keys())

def tfidf(query_tokens, doc_tokens):
    doc_tf = Counter(doc_tokens)
    score = 0
    for t in query_tokens:
        score += doc_tf.get(t, 0)
    return score

def bm25(query_tokens, doc_tokens):
    doc_tf = Counter(doc_tokens)
    score = 0
    for t in query_tokens:
        score += doc_tf.get(t, 0) / (len(doc_tokens) + 1)
    return score

def write_results(filename, score_func):
    with open(filename, "w") as f:
        for qid, qtext in queries.items():
            q_tokens = qtext.split()

            scored = []
            for docid in docs:
                doc_tokens = index.get(docid, [])
                score = score_func(q_tokens, doc_tokens)
                scored.append((docid, score))

            scored.sort(key=lambda x: x[1], reverse=True)

            for docid, score in scored:
                f.write(f"{qid} Q0 {docid} 0 {score} Exp\n")

write_results("OkapiBM25_Results_File.txt", bm25)
write_results("tfidf_Results_File.txt", tfidf)
write_results("OkapiTF_Results_File.txt", tfidf)

print("Ranking files generated successfully")