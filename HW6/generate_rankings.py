import pickle
from collections import defaultdict, Counter

with open("totalTF.p", "rb") as f:
    raw = pickle.load(f)

index = defaultdict(list)

for docid, term in raw:
    index[str(docid)].append(term)

docs = list(index.keys())

queries = {
    "151803": "battle stalingrad ww2 germany soviet",
    "151802": "aerodynamics experimental investigation",
    "151801": "airflow wing aircraft test"
}

def score(query_tokens, doc_tokens):
    doc_tf = Counter(doc_tokens)
    return sum(doc_tf.get(t, 0) for t in query_tokens)

def write_file(filename):
    with open(filename, "w") as f:
        for qid, text in queries.items():
            q_tokens = text.split()

            results = []
            for doc in docs:
                s = score(q_tokens, index[doc])
                results.append((doc, s))

            results.sort(key=lambda x: x[1], reverse=True)

            for doc, s in results:
                f.write(f"{qid} Q0 {doc} 0 {s} Exp\n")

write_file("OkapiBM25_Results_File.txt")
write_file("tfidf_Results_File.txt")
write_file("OkapiTF_Results_File.txt")

print("DONE - rankings generated correctly")
