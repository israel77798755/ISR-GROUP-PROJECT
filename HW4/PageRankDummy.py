graph = {}

class Node:
    def __init__(self):
        self.inlinks = set()
        self.outdeg = 0
        self.rank = 1.0


def load_graph(file):
    global graph
    graph.clear()

    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) == 0:
                continue

            node = parts[0]

            if node not in graph:
                graph[node] = Node()

            for link in parts[1:]:
                if link == "":
                    continue

                graph[node].inlinks.add(link)

                if link not in graph:
                    graph[link] = Node()

                graph[link].outdeg += 1


def simple_pagerank():
    N = len(graph)

    if N == 0:
        print("Empty graph")
        return

    for node in graph:
        graph[node].rank = 1 / N


def save_dummy():
    sorted_nodes = sorted(graph.items(), key=lambda x: x[1].rank, reverse=True)

    with open("PageRankDummy_results.txt", "w") as f:
        for n, obj in sorted_nodes[:10]:
            f.write(f"{n} {obj.rank}\n")

    print("PageRank Dummy done")


if __name__ == "__main__":
    load_graph("linkgraph.txt")
    simple_pagerank()
    save_dummy()