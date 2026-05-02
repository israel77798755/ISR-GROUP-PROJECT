import os
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from sklearn.decomposition import LatentDirichletAllocation

NUM_TOPICS = 10
TOP_WORDS = 10
STOPWORDS = list(ENGLISH_STOP_WORDS)

def load_qrels(filepath):
    qrels = {}

    with open(filepath, "r") as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) < 2:
                continue

            qid = parts[0]
            docid = parts[1]

            if qid not in qrels:
                qrels[qid] = set()

            qrels[qid].add(docid)

    return qrels


def load_documents(filepath):
    docs = {}

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    raw_docs = content.split(".I ")

    for doc in raw_docs:
        if not doc.strip():
            continue

        lines = doc.strip().split("\n")
        doc_id = lines[0].strip()

        text = ""
        if ".W" in doc:
            text = doc.split(".W")[1]

        docs[doc_id] = text.strip()

    return docs

def get_topic_words(model, feature_names, n_words):
    output = ""

    for topic_idx, topic in enumerate(model.components_):
        top_features = topic.argsort()[:-n_words - 1:-1]

        words = [feature_names[i] for i in top_features]
        output += f"\nTopic {topic_idx + 1}: {' '.join(words)}"

    return output


def run_lda():

    print("Loading Cranfield data...")

    qrels = load_qrels("cranfield/cranqrel")
    docs = load_documents("cranfield/cran.all.1400")

    os.makedirs("topics", exist_ok=True)

    processed = 0

    for qid in qrels:

        if processed >= 20:
            break

        print("Processing Query:", qid)

        doc_ids = list(qrels[qid])
        text_docs = []

        for doc_id in doc_ids:
            text = docs.get(doc_id, "")

            if text and len(text.strip()) > 0:
                text_docs.append(text)

        if len(text_docs) < 2:
            print("Skipping Query", qid)
            continue

        vectorizer = CountVectorizer(stop_words=STOPWORDS)
        X = vectorizer.fit_transform(text_docs)

        lda = LatentDirichletAllocation(
            n_components=NUM_TOPICS,
            max_iter=10,
            random_state=42
        )

        lda.fit(X)

        topic_text = get_topic_words(
            lda,
            vectorizer.get_feature_names_out(),
            TOP_WORDS
        )

        with open(f"topics/query_{qid}.txt", "w") as f:
            f.write(topic_text)

        processed += 1

    print("\nLDA clustering completed successfully!")

if __name__ == "__main__":
    run_lda()