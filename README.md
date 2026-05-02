# **DEPARTMENT OF INFORMATION SYSTEMS**

## **INFORMATION STORAGE AND RETRIEVAL PROJECT REPORT**

### **SECTION 02**

## **Group Members**

| Name            | ID          |
| --------------- | ----------- |
| Israel Tsegaye    | UGR/4738/17 |
|  Israel Tesfaye   | UGR/2424/17 |
| Fraol Shiferaw    | UGR/9328/17 |
| Hailetsion Debash | UGR/8486/17 |
| Ismael Ibrahim    | UGR/2279/17 |


**Submitted To:** Dr. Demeke Ayele
**Submission Date:** 05/02/2026

---

# **Introduction**

This project involves the design and implementation of a complete Information Retrieval (IR) system. The work was carried out in several stages, where each assignment contributed to building one part of the full retrieval pipeline. These stages included data preprocessing, indexing, ranking, evaluation, and machine learning-based enhancements.

The Cranfield dataset was used throughout the project. It contains a collection of documents, queries, and relevance judgments, which made it suitable for testing retrieval accuracy and system performance.

During development, raw text data was transformed into a structured format, enabling efficient searching. Various retrieval models such as TF-IDF, BM25, and Okapi TF were implemented and compared. The system was also evaluated using standard IR metrics like Precision, Recall, and Mean Average Precision (MAP). In later phases, clustering and machine learning techniques were introduced to extend system capabilities.

The overall objective was not only to implement an IR system but also to deeply understand how each component interacts within the full pipeline.

---

# **Technical Implementation and Tools**

## **Initial Plan: Elasticsearch**

At the beginning, the group intended to use Elasticsearch as the main search engine, following the project instructions. Elasticsearch is widely known for its built-in inverted index and BM25 ranking functionality. We successfully attempted to set up a local instance to begin development.

---

## **Problems Encountered**

Several issues were faced during setup and execution:

* Compatibility issues with Java Runtime Environment and JDK versions
* Performance instability and occasional crashes
* Difficulty configuring ports and elasticsearch.yml
* Network restrictions that affected collaboration and testing

These challenges slowed down progress and made the system difficult to maintain.

---

## **Switch to Python-Based Implementation**

Due to the above limitations, we decided to implement the entire IR pipeline using Python.

This approach provided several advantages:

### **Better Conceptual Understanding**

We implemented core IR components manually, including inverted indexing, TF-IDF scoring, and ranking algorithms.

### **Direct Dataset Control**

We worked directly with Cranfield dataset files such as:

* cran.all.1400
* cran.query
* cranqrel

This ensured full control over preprocessing and evaluation consistency.

### **Simplified Development Process**

Python made debugging and testing easier compared to a complex server-based system.

---

## *Tools Used**

The final system includes:

* Inverted Index (custom implementation)
* Ranking Models: TF-IDF, BM25, Okapi TF
* Evaluation Tools: Precision, Recall, MAP (TREC format)

---

# **HW1 —> System Setup and Basic Retrieval**

In the first phase, we established the foundation of the IR system using the Cranfield dataset. The focus was on understanding how documents, queries, and relevance judgments are structured.

We implemented Python scripts such as:

* CreateIndex.py
* QueryProcessing.py
* RetrievalModels.py

An initial index file (index.pkl) was created, and basic ranking outputs were generated.

### **Outputs Produced**

* tfidf.txt
* bm25.txt
* okapi_tf.txt
* laplace.txt

### **Result**

The system successfully processed queries and returned ranked documents using multiple models, confirming that the retrieval pipeline was functional.

---

# **HW2 —> Data Cleaning and Inverted Index Construction**

This phase focused on cleaning and structuring the dataset for retrieval.

### **Processing Steps**

* Tokenization of text
* Conversion to lowercase
* Removal of punctuation and stopwords

An inverted index was built using indexer.py, mapping terms to documents.

### **Outcome**

* index.pkl successfully generated
* Faster and more structured retrieval process
* Improved consistency in document representation

---

# **HW4 —> URL Normalization and Link-Based Ranking Techniques**

This stage introduced web structure analysis and URL processing.

We implemented:

* URL canonicalization (Canonicalizer.py)
* Link analysis algorithms (PageRank and HITS)

### **Generated Outputs**

* pagerank_results.txt
* auth.txt
* hub.txt

### **Result**

* URLs were normalized effectively
* Duplicate links were reduced
* Authority and hub scores were successfully computed

---

# **HW5 —>Retrieval Modeling and Performance Evaluation**

This stage focused on evaluating retrieval performance using standard IR metrics.

### **Models Used**

* TF-IDF
* BM25
* Okapi TF

### **Evaluation Tools**

* trec_eval
* qrels.txt
* rankList.txt

### **Results**

* Query 151801 → AP: 0.2952, P@10: 0.2000
* Query 151802 → AP: 0.2607, P@10: 0.1000
* Query 151803 → AP: 0.2987, P@10: 0.2000
* **MAP: 0.3**

---

# **HW6 —>Machine Learning Integration for Ranking Optimization**

In this phase, machine learning techniques were introduced for ranking improvement.

### **Approach**

* Feature extraction from documents
* Feature selection using Chi-Square (SelectKBest)

### **Result**

* Classification accuracy achieved: ~0.39

---

# **HW7 —> System Refinement and Performance Enhancement**

This stage focused on improving preprocessing and feature representation.

### **Improvements**

* Better text cleaning
* Enhanced feature selection
* More stable ranking outputs

### **Result**

* More consistent retrieval and classification performance

---

# **HW8 —>Document Clustering and System Integration**

The final stage involved clustering documents into groups based on similarity.

### **Tools Used**

* clustering.py
* partition.py

### **Output**

* Documents grouped into thematic clusters stored in the topics/ directory

---

# **Conclusion**

This project successfully developed a complete Information Retrieval system by combining multiple components including indexing, ranking, evaluation, machine learning, and clustering.

Each stage contributed to building a deeper understanding of how IR systems function. By integrating all modules into a single pipeline, we demonstrated how raw text data can be transformed into structured and meaningful search results.
