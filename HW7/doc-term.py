import os
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from bs4 import BeautifulSoup

textList = []
labelList = []
docIDList = []

def load_data(path="Files/"):

    for filename in os.listdir(path):

        if filename.startswith("."):
            continue

        file_path = os.path.join(path, filename)

        with open(file_path, "r", encoding="ISO-8859-1") as f:
            content = f.read()

        soup = BeautifulSoup("<root>" + content + "</root>", "html.parser")

        label = soup.find("label")
        docid = soup.find("emailid")
        text = soup.find("text")

        if label is None or docid is None or text is None:
            continue

        label = label.get_text().strip()
        docid = docid.get_text().strip()
        text = text.get_text()

        # -------- CLEAN TEXT --------
        text = text.lower()
        text = " ".join(text.split())

        # remove label leakage
        text = re.sub(r"spam|ham", "", text)

        # remove numbers and punctuation
        text = re.sub(r"\d+", "", text)
        text = re.sub(r"[^\w\s]", "", text)

        textList.append(text)
        labelList.append(label)
        docIDList.append(docid)



def main():

    print("Loading data...")
    load_data()

    print("Total docs:", len(textList))

    
    print("Unique texts:", len(set(textList)))

    
    le = LabelEncoder()
    Y = le.fit_transform(labelList)

    
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=500
    )

    X = vectorizer.fit_transform(textList)

    
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)

    accuracies = []

    for train_idx, test_idx in kfold.split(X):

        X_train, X_test = X[train_idx], X[test_idx]
        Y_train, Y_test = Y[train_idx], Y[test_idx]

        model = LogisticRegression(max_iter=1000, C=0.1)
        model.fit(X_train, Y_train)

        preds = model.predict(X_test)

        acc = accuracy_score(Y_test, preds)
        accuracies.append(acc)

        print("Fold accuracy:", round(acc * 100, 2))

    print("\nFinal Average Accuracy:", round(np.mean(accuracies) * 100, 2))


if __name__ == "__main__":
    main()