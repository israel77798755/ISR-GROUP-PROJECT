import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression

def create_dict(qdIDTest, predictions):
    result = {}

    for i in range(len(predictions)):
        qd = qdIDTest[i][0]
        qid, docid = qd.split("-", 1)

        if qid not in result:
            result[qid] = []

        result[qid].append((docid, predictions[i]))

    return result


def sort_dict(d):
    for qid in d:
        d[qid] = sorted(d[qid], key=lambda x: x[1], reverse=True)
    return d


def write_file(d):
    with open("trainingperformance.txt", "w") as f:
        for qid in d:
            rank = 1
            for doc, score in d[qid]:
                f.write(f"{qid} Q0 {doc} {rank} {score:.4f} Exp\n")
                rank += 1


def main():

    df = pd.read_csv("staticFeatureMatrix.csv")

    qdID = df[["QID-DocID"]].values

    X = df[[
        "TF-IDF",
        "Okapi TF",
        "BM25",
        "Laplace",
        "Jelinek-Mercer"
    ]].values

    Y = df["Label"].values

    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    for train, test in kf.split(X):

        model = LinearRegression()
        model.fit(X[train], Y[train])

        preds = model.predict(X[test])

        test_qd = qdID[test]

        d = create_dict(test_qd, preds)
        d = sort_dict(d)

        write_file(d)

        break

    print("trainingperformance.txt created")


main()