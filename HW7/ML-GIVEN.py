import csv


def norm(x):
    return x.strip().lower()


def load_rank_file(filename):
    data = {}

    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 5:
                continue

            qid = norm(parts[0])
            docid = norm(parts[2])
            score = float(parts[4])

            key = f"{qid}-{docid}"
            data[key] = score

    return data


def load_qrels(filename):
    qrels = {}

    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) < 4:
                continue

            qid = norm(parts[0])
            docid = norm(parts[2])
            rel = parts[3]

            key = f"{qid}-{docid}"

            try:
                qrels[key] = int(rel)
            except:
                qrels[key] = 0

    return qrels


def main():

    bm25 = load_rank_file("OkapiBM25_Results_File.txt")
    tfidf = load_rank_file("tfidf_Results_File.txt")
    okapi = load_rank_file("OkapiTF_Results_File.txt")
    laplace = load_rank_file("UnigramLMLaplace_Results_File.txt")
    jm = load_rank_file("UnigramLMJM_Results_File.txt")

    qrels = load_qrels("qrels.txt")

    keys = set(bm25) | set(tfidf) | set(okapi) | set(laplace) | set(jm)

    pos = 0
    neg = 0

    with open("staticFeatureMatrix.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "DocID",
            "TF-IDF",
            "Okapi TF",
            "BM25",
            "Laplace",
            "Jelinek-Mercer",
            "Label"
        ])

        for key in keys:

            label = qrels.get(key, 0)

            if label == 1:
                pos += 1
            else:
                neg += 1

            writer.writerow([
                key,
                tfidf.get(key, 0),
                okapi.get(key, 0),
                bm25.get(key, 0),
                laplace.get(key, 0),
                jm.get(key, 0),
                label
            ])

    print("staticFeatureMatrix.csv created")
    print("Positive samples:", pos)
    print("Negative samples:", neg)


main()