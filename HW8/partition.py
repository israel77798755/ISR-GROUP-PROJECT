import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


NUM_CLUSTERS = 10


def load_documents(filepath):
    docs = {}
    doc_ids = []

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
        doc_ids.append(doc_id)

    return docs, doc_ids



def run_kmeans():

    print("Loading Cranfield documents...")

    docs, doc_ids = load_documents("cranfield/cran.all.1400")

    text_data = []

    for doc_id in doc_ids:
        text = docs.get(doc_id, "")
        if text:
            text_data.append(text)
        else:
            text_data.append("")

    print("Total documents:", len(text_data))

   
    vectorizer = TfidfVectorizer(stop_words="english", max_features=2000)
    X = vectorizer.fit_transform(text_data)

    print("Running K-Means clustering...")

    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42)
    kmeans.fit(X)

    labels = kmeans.labels_

    
    clusters = {}

    for i, label in enumerate(labels):
        if label not in clusters:
            clusters[label] = []

        clusters[label].append(doc_ids[i])

    
    os.makedirs("clusters", exist_ok=True)

    with open("clusters/clusters.txt", "w") as f:
        for label in clusters:
            f.write(f"Cluster {label}:\n")
            f.write(", ".join(clusters[label]))
            f.write("\n\n")

    print("Clustering completed successfully!")



if __name__ == "__main__":
    run_kmeans()