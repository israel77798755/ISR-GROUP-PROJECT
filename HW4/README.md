
# **Information Retrieval Assignment 4: Link-Based Ranking System**

## **Overview of the Work**

In this assignment, we explored ranking techniques that rely on relationships between documents rather than only text similarity. Building on the indexing work completed earlier, we created a graph structure from the Cranfield dataset and applied link analysis algorithms to determine document importance.

The key idea behind this task is to evaluate documents using their connections within a graph, allowing us to capture structural importance in addition to term-based relevance.

---

## **Core Functionalities**

### **1. Graph Formation from Documents**

A directed graph was created where nodes represent documents and edges represent relationships derived from shared content or references.


### **2. HITS-Based Scoring Mechanism**

The HITS algorithm was implemented to calculate two types of scores:

* **Hub Values**: Indicate documents that link to many significant documents
* **Authority Values**: Indicate documents that are frequently referenced by strong hubs

The scores were updated iteratively until they stabilized.


### **3. PageRank Computation**

We applied the PageRank algorithm to measure the overall importance of each document within the graph.

* A damping factor (commonly set to 0.85) was used
* Scores were updated repeatedly until convergence was reached

### **4. Simplified Testing Modules**

To ensure correctness, lightweight versions of the graph and ranking algorithms were implemented.

These were used for:

* Verifying graph structure
* Testing ranking logic in a controlled environment



### **5. Evaluation Component**

A scoring module was used to analyze and summarize the ranking outputs, helping us verify whether the computed scores were reasonable.


## **Dataset Description**

The experiments were conducted using the **Cranfield dataset**, which includes:

* **cran.all.1400** – collection of documents
* **cran.query** – set of queries
* **cranqrel** – relevance judgments

---

## **System Requirements and Dependencies**

The implementation depends on previously generated data structures from earlier work, particularly the inverted index stored as a pickle file.

This data is essential for:

* Constructing the document graph
* Supporting ranking computations


## **Processing Steps**

### **Step 1: Importing Data**

Load processed data and index structures (e.g., `index.pkl`) generated earlier.


### **Step 2: Building the Graph**

Using document-term relationships, a graph is constructed through the main graph module.

---

### **Step 3: Exporting Graph Structure**

The graph is saved in a text-based format (`linkgraph.txt`) for further processing.

---

### **Step 4: Applying HITS Algorithm**

Compute hub and authority values through iterative updates.



### **Step 5: Running PageRank**

Calculate document importance scores using rank propagation across the graph.


### **Step 6: Result Analysis**

Evaluate the ranking outputs using a scoring script.



### **Step 7: Verification**

Use simplified implementations to validate correctness of both graph structure and ranking behavior.


## **Generated Outputs**

* `linkgraph.txt` → Representation of the document graph
* `pagerank_results.txt` → Final PageRank scores
* `PageRankDummy_results.txt` → Output from simplified PageRank
* `auth.txt` → Authority scores from HITS
* `hub.txt` → Hub scores from HITS
* Evaluation output → Summary scores from the scoring module

---

## **Additional Remarks**

* The work is based entirely on the Cranfield dataset rather than web-scale data
* Graph construction is derived from term-based relationships created earlier
* Both HITS and PageRank operate on the same graph structure
* Simplified modules are included only for testing and debugging
* All outputs are generated dynamically from processed inputs

---

## **Final Summary**

This assignment illustrates how graph-based techniques such as HITS and PageRank can be applied within an Information Retrieval system. Unlike traditional approaches that rely only on term frequency, these methods use document relationships to identify important documents, providing an additional perspective on ranking.

