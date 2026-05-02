# Information Retrieval HW8
## Overview
This project applies two unsupervised learning methods on the Cranfield dataset:
- LDA (Topic Modeling)
- K-Means (Document Clustering)

The goal is to analyze documents by grouping them based on similarity and hidden topics.

---

## Part A: LDA Clustering (clustering.py)

- Loads Cranfield documents and query relevance file (cranqrel)
- Groups documents based on queries
- Uses CountVectorizer to convert text into word counts
- Applies Latent Dirichlet Allocation (LDA)
- Extracts topics (important words for each group)
- Saves results in `topics/` folder

### Output:
- Each query shows several topics
- Each topic contains related words
- Represents what the documents are about

---

## Part B: K-Means Clustering (partition.py)

- Loads all Cranfield documents
- Converts text into TF-IDF vectors
- Applies K-Means clustering
- Groups similar documents together
- Saves clusters in `clusters/clusters.txt`

### Output:
- Each cluster contains similar documents
- Shows document similarity based on content

---

## Key Difference

- LDA: Finds topics (word-level meaning)
- K-Means: Groups documents (document similarity)

---

## Summary
LDA shows what the text is about, while K-Means shows which documents are similar to each other.