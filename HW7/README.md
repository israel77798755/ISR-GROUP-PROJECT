# Information Retrieval HW7

## Project Overview
This project implements a **document classification system** for spam detection using machine learning techniques. The goal is to classify emails into **spam** or **ham (non-spam)** categories based on their textual content.

The system follows a complete pipeline from **data extraction → feature representation → model training → evaluation**.

---

## Dataset
The dataset consists of email files stored in the `Files/` directory.

Each file contains structured tags:
- `<label>` → class label (spam / ham)
- `<emailid>` → unique document ID
- `<text>` → email content

---

## Methodology

### 1. Data Extraction
- Emails are read from files
- Content is parsed using **BeautifulSoup**
- Extracted fields:
  - Label
  - Document ID
  - Text content

---

### 2. Text Preprocessing
- Convert text to lowercase
- Remove extra whitespace
- Remove punctuation and numbers
- Remove label leakage terms (e.g., "spam", "ham")

---

### 3. Feature Representation
- Text is transformed into numerical features using:
  - **TF-IDF Vectorization**
- Stopwords are removed
- Feature space is limited to improve generalization

---

### 4. Model Training
- Algorithm used:
  - **Logistic Regression**
- Labels are encoded into numeric form (0 / 1)

---

### 5. Evaluation
- Evaluation method:
  - **K-Fold Cross Validation (k=5)**
- Metric used:
  - **Accuracy**

---

## Output
The system prints:
- Accuracy for each fold
- Final average accuracy

Example:Fold accuracy: 100.0
...
Final Average Accuracy: 100.0

---

## Key Observations
- The model achieved **100% accuracy**.
- All documents are unique (no duplicates).
- This indicates that:
  - The dataset is **highly separable**
  - Spam and ham emails contain **distinct vocabulary patterns**

---

## Important Note
Such perfect performance is uncommon in real-world scenarios.  
In practical applications, datasets are more complex and noisy, leading to lower accuracy.

---

## Tools & Libraries
- Python
- NumPy
- Scikit-learn
- BeautifulSoup (bs4)

---

## Conclusion
This project demonstrates how **text classification** can be effectively performed using machine learning. The pipeline shows a clear transformation from raw text data to meaningful predictions using standard IR and ML techniques.