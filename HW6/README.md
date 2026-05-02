# Information Retrieval HW6: Machine Learning for Ranking

## Project Overview
This project implements a Machine Learning approach for ranking documents in an Information Retrieval system. Instead of relying on a single ranking formula, multiple retrieval models are combined as features and used to train a learning algorithm that predicts document relevance.

---

## Main Idea
Each query–document pair is represented using multiple IR scoring models. A machine learning model is then trained to learn the best way to combine these scores for better ranking performance.

---

## Feature Engineering

For each query–document pair, a feature vector is created using the following IR models:

- TF-IDF  
- Okapi TF  
- BM25  
- Laplace Language Model  
- Jelinek-Mercer Language Model  

Each model produces a score representing how relevant a document is to a query.

---

## Dataset Format (Feature Matrix)

The dataset used for training is stored in:
staticFeatureMatrix.csv

### Structure:
QID-DocID, TF-IDF, Okapi TF, BM25, Laplace,Jelinek-Mercer, Label

### Column Meaning:
- QID-DocID → Query and document identifier  
- TF-IDF → TF-IDF score  
- Okapi TF → Okapi TF score  
- BM25 → BM25 score  
- Laplace → Laplace language model score  
- Jelinek-Mercer → Jelinek-Mercer score  
- Label → relevance label (1 = relevant, 0 = not relevant)
## Machine Learning Model

The system uses a supervised learning approach:

### Linear Regression (Learning-to-Rank style)
- Input: Feature matrix (IR scores)
- Output: Predicted relevance score
- Goal: Learn how to combine multiple IR models effectively

---
## Evaluation Strategy
The model is evaluated using:
- K-Fold Cross Validation (5 splits)
- Ranking based on predicted scores
- Comparison of predicted rankings per query
---

## Output Files
The system generates:
- `staticFeatureMatrix.csv` → Feature dataset  
- `trainingperformance.txt` → Final ranked results per query  

Format of output: 
query_id Q0 document_id rank score EXP

---

## Pipeline Summary

1. Load relevance data (qrels)
2. Compute IR model scores
3. Build feature matrix
4. Save dataset (`staticFeatureMatrix.csv`)
5. Train Linear Regression model
6. Predict document scores
7. Generate final ranking output

---

## Summary
This project demonstrates a learning-to-rank approach where multiple Information Retrieval models are combined using Machine Learning to improve ranking quality and prediction accuracy.