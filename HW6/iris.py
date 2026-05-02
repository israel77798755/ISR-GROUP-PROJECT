import os
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_selection import SelectKBest, chi2


STOPWORDS = list(ENGLISH_STOP_WORDS)


def load_documents(filepath):
    docs = {}

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    raw_docs = content.split(".I ")

    for doc in raw_docs:
        if not doc.strip():
            continue

        lines = doc.split("\n")
        doc_id = lines[0].strip()

        text = ""
        if ".W" in doc:
            text = doc.split(".W")[1]

        docs[doc_id] = text.strip()

    return docs


def load_qrels(filepath):
    qrels = {}

    with open(filepath, "r") as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) < 3:
                continue

            qid = parts[0]
            docid = parts[1]
            rel = int(parts[2])

            if qid not in qrels:
                qrels[qid] = {}

            qrels[qid][docid] = rel

    return qrels


def main():

    print("Loading Cranfield-style dataset...")

    docs = load_documents("cran.all.1400")
    qrels = load_qrels("cranqrel")

    X_text = []
    y = []

    for qid in qrels:

        for docid, label in qrels[qid].items():

            text = docs.get(docid, "")

            if text.strip():
                X_text.append(text)
                y.append(label)

    print("Documents Loaded:", len(X_text))

    if len(X_text) < 5:
        print("ERROR: Not enough data loaded. Check file paths.")
        return

    vectorizer = CountVectorizer(stop_words=STOPWORDS)
    X = vectorizer.fit_transform(X_text)

    print("Original Features:", X.shape[1])

    X = SelectKBest(chi2, k=min(10, X.shape[1])).fit_transform(X, y)

    print("Selected Features:", X.shape[1])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\nAccuracy:", accuracy_score(y_test, y_pred))

    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred, zero_division=0))


if __name__ == "__main__":
    main()