import dill
from collections import defaultdict

DATA_DIR = "../HW2/Pickles"

linkGraph = defaultdict(set)


def load_index():
    with open(f"{DATA_DIR}/index.pkl", "rb") as f:
        return dill.load(f)


def build_graph(index):

    term_docs = defaultdict(list)

   
    for term_id, data in index.items():

        if "postings" not in data:
            continue

        df = data["df"]

        
        if df > 80:
            continue

        docs = list(data["postings"].keys())
        term_docs[term_id] = docs

   
    for docs in term_docs.values():

        for i in range(len(docs)):
            for j in range(i + 1, len(docs)):

                d1 = str(docs[i])
                d2 = str(docs[j])

                linkGraph[d1].add(d2)
                linkGraph[d2].add(d1)


def save_graph():
    with open("linkgraph.txt", "w") as f:
        for doc in linkGraph:
            f.write(doc + " " + " ".join(linkGraph[doc]) + "\n")


if __name__ == "__main__":
    index = load_index()
    build_graph(index)
    save_graph()

    edges = sum(len(v) for v in linkGraph.values())
    degrees = [len(v) for v in linkGraph.values()]

    print("Graph built successfully")
    print("Nodes:", len(linkGraph))
    print("Total edges:", edges)
    print("Min degree:", min(degrees))
    print("Max degree:", max(degrees))
    print("Average degree:", sum(degrees) / len(degrees))