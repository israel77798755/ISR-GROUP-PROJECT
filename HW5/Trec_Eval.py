from collections import defaultdict
import os


def load_qrels(file):
    qrels = defaultdict(set)

    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 4:
                continue

            qid = parts[0]
            docid = parts[2]
            rel = parts[3]

            if rel == "1":
                qrels[qid].add(docid)

    return qrels


def load_rank(file):
    ranks = defaultdict(list)

    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 3:
                continue

            qid = parts[0]
            docid = parts[2]

            ranks[qid].append(docid)

    return ranks


def average_precision(relevant, retrieved):
    if not relevant:
        return 0.0

    score = 0.0
    hit = 0

    for i, doc in enumerate(retrieved):
        if doc in relevant:
            hit += 1
            score += hit / (i + 1)

    return score / len(relevant)


def precision_at_k(relevant, retrieved, k=10):
    retrieved = retrieved[:k]
    return sum(1 for d in retrieved if d in relevant) / k


def evaluate(qrels, ranks):
    APs = []

    for q in qrels:

        if q not in ranks:
            continue

        relevant = qrels[q]
        retrieved = ranks[q]

        ap = average_precision(relevant, retrieved)
        APs.append(ap)

        print("\nQuery:", q)
        print("AP:", round(ap, 4))
        print("P@10:", round(precision_at_k(relevant, retrieved), 4))
        print("Overlap:", len(set(relevant) & set(retrieved)))

    print("\nMAP:", round(sum(APs) / len(APs), 4) if APs else 0.0)


def main():
    if not os.path.exists("qrels.txt"):
        print("ERROR: qrels.txt not found")
        return

    if not os.path.exists("rankList.txt"):
        print("ERROR: rankList.txt not found")
        return

    qrels = load_qrels("qrels.txt")
    ranks = load_rank("rankList.txt")

    evaluate(qrels, ranks)


if __name__ == "__main__":
    main()