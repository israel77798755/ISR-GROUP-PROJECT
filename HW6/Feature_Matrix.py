import csv
from collections import defaultdict

def load_rank_file(filename, model_dict):
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) < 5:
                continue

            qid = parts[0]
            docid = parts[2]
            score = float(parts[4])

            key = f"{qid}-{docid}"
            model_dict[key] = score


def load_qrels(filename):
    qrels = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()

            qid = parts[0]
            docid = parts[2]
            rel = int(parts[3])

            key = f"{qid}-{docid}"
            qrels[key] = rel

    return qrels


def main():

    bm25 = {}
    tfidf = {}
    laplace = {}
    jm = {}
    okapi = {}

    load_rank_file("OkapiBM25_Results_File.txt", bm25)
    load_rank_file("tfidf_Results_File.txt", tfidf)
    load_rank_file("UnigramLMLaplace_Results_File.txt", laplace)
    load_rank_file("UnigramLMJM_Results_File.txt", jm)
    load_rank_file("OkapiTF_Results_File.txt", okapi)

    qrels = load_qrels("qrels.txt")

    all_keys = set(list(bm25.keys()) + list(tfidf.keys()) +
                   list(laplace.keys()) + list(jm.keys()) +
                   list(okapi.keys()))

    with open("staticFeatureMatrix.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "QID-DocID",
            "TF-IDF",
            "Okapi TF",
            "BM25",
            "Laplace",
            "Jelinek-Mercer",
            "Label"
        ])

        for key in all_keys:

            writer.writerow([
                key,
                tfidf.get(key, 0),
                okapi.get(key, 0),
                bm25.get(key, 0),
                laplace.get(key, 0),
                jm.get(key, 0),
                qrels.get(key, 0)
            ])

    print("staticFeatureMatrix.csv created")


main()
def normalize(docid):
    return docid.strip().lower()