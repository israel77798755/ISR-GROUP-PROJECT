# Information Retrieval HW4

---
## Project Overview

This project implements graph-based retrieval and ranking algorithms using the Cranfield dataset. It extends the inverted index developed in HW2 and constructs a document relationship graph to support graph-based ranking models.

The main objective is to analyze document importance using link structure rather than only term-based similarity.

---

## Implemented Components

### 1. Document Link Graph Construction
Construction of a directed graph representing relationships between documents based on shared structure and references.

### 2. HITS Algorithm (Hub and Authority Scores)
- Computes **Hub scores**, representing pages that point to important documents.
- Computes **Authority scores**, representing important documents pointed to by strong hubs.
- Iterative update until convergence.

### 3. PageRank Algorithm
- Computes global importance of documents based on link structure.
- Uses damping factor (typically 0.85).
- Iteratively distributes rank until convergence.

### 4. Dummy / Debug Implementations
- Used to verify correctness of graph structure and ranking logic.
- Includes simplified versions of PageRank and graph processing.

### 5. Score Evaluation Module
- Evaluates and validates ranking outputs.
- Provides aggregated score summaries for analysis.

---

## Dataset

The project uses the **Cranfield Collection**, which includes:

- cran.all.1400 → document corpus  
- cran.query → query set  
- cranqrel → relevance judgments  

---

## System Dependency

This system relies on intermediate data and inverted index structures generated in HW2 (stored as pickle files). These are used to construct the document graph and support ranking computations.

---

## Pipeline Workflow

### Step 1: Data Loading
Load inverted index and processed data from HW2 (`index.pkl`).

### Step 2: Graph Construction
Extract document-term relationships and build the document link graph (`Graph.py`).

### Step 3: Link Graph Generation
Generate the graph representation file (`linkgraph.txt`).

### Step 4: HITS Algorithm
Compute:
- Hub Scores
- Authority Scores

### Step 5: PageRank Algorithm
Compute document importance scores using iterative rank propagation.

### Step 6: Evaluation
Evaluate ranking outputs using `scorer.py`.

### Step 7: Validation
Validate graph and ranking logic using:
- `GraphDummy.py`
- `PageRankDummy.py`

---

## Output Files

- `linkgraph.txt` → Document link graph representation  
- `pagerank_results.txt` → Final PageRank ranked list  
- `PageRankDummy_results.txt` → Simplified PageRank output (debugging)  
- `auth.txt` → Authority scores (HITS)  
- `hub.txt` → Hub scores (HITS)  
- `scorer.py output` → Aggregated evaluation scores  

---

## Notes

- The dataset used is Cranfield, not web-based or AP collections.  
- The graph is constructed from document-term relationships derived from HW2.  
- HITS and PageRank operate on the same underlying graph structure.  
- Dummy modules are used strictly for debugging and validation purposes.  
- All outputs are generated dynamically from processed dataset inputs.

---

## Summary

This project demonstrates the application of graph-based ranking algorithms (HITS and PageRank) in information retrieval systems. It highlights how link structure can be used to measure document importance beyond traditional term-based retrieval models.