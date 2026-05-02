import math
import dill

DATA_DIR = "Pickles"


def load_data():
    index = dill.load(open(f"{DATA_DIR}/index.pkl", "rb"))
    doc_lengths = dill.load(open(f"{DATA_DIR}/doc_lengths.pkl", "rb"))
    vocab_size = dill.load(open(f"{DATA_DIR}/vocab_size.pkl", "rb"))
    return index, doc_lengths, vocab_size

def get_tf(data):
    if isinstance(data, dict):
        return data.get("tf") or data.get("frequency") or 0
    if isinstance(data, (list, tuple)):
        return data[0]
    return data

def get_postings(data):
    if isinstance(data, dict) and "postings" in data:
        return data["postings"]
    return {}


def tfidf(index, N):
    scores = {}

    for term, data in index.items():

        postings = get_postings(data)
        df = len(postings)

        if df == 0:
            continue

        idf = math.log(N / df)

        for doc, value in postings.items():
            tf = get_tf(value)
            scores[doc] = scores.get(doc, 0) + tf * idf

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


def bm25(index, doc_lengths, N):
    k1 = 1.2
    b = 0.75

    scores = {}

    avg_len = sum(doc_lengths.values()) / len(doc_lengths)

    for term, data in index.items():

        postings = get_postings(data)
        df = len(postings)

        if df == 0:
            continue

        idf = math.log((N - df + 0.5) / (df + 0.5))

        for doc, value in postings.items():

            tf = get_tf(value)
            doc_len = doc_lengths.get(doc, avg_len)

            tf_part = (tf * (k1 + 1)) / (
                tf + k1 * (1 - b + b * doc_len / avg_len)
            )

            scores[doc] = scores.get(doc, 0) + idf * tf_part

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


def main():
    print("Retrieval Models module loaded successfully")

    index, doc_lengths, vocab_size = load_data()

    N = len(doc_lengths)

    print(f"Total documents: {N}")
    print(f"Vocabulary size: {vocab_size}")

    tfidf_results = tfidf(index, N)
    bm25_results = bm25(index, doc_lengths, N)

    print("\nTop TF-IDF:")
    for doc, score in tfidf_results[:10]:
        print(doc, score)

    print("\nTop BM25:")
    for doc, score in bm25_results[:10]:
        print(doc, score)


if __name__ == "__main__":
    main()