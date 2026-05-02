d = 0.85
graph = {}


class Node:
    def __init__(self):
        self.outlinks = set()
        self.rank = 1.0


def load_graph(file):

    global graph
    graph = {}

    with open(file, "r") as f:
        for line in f:
            parts = line.split()

            if not parts:
                continue

            node = parts[0]

            if node not in graph:
                graph[node] = Node()

            for link in parts[1:]:

                graph[node].outlinks.add(link)

                if link not in graph:
                    graph[link] = Node()


def pagerank(iterations=30):

    N = len(graph)

    for _ in range(iterations):

        new_rank = {}

        for node in graph:

            rank_sum = 0

            for n in graph:
                if node in graph[n].outlinks:
                    if len(graph[n].outlinks) > 0:
                        rank_sum += graph[n].rank / len(graph[n].outlinks)

            new_rank[node] = (1 - d) / N + d * rank_sum

        
        norm = sum(new_rank.values())

        if norm != 0:
            for n in new_rank:
                new_rank[n] /= norm

        for n in graph:
            graph[n].rank = new_rank[n]


def save():

    sorted_nodes = sorted(graph.items(), key=lambda x: x[1].rank, reverse=True)

    print("\n Top 10 PageRank:")

    for n, obj in sorted_nodes[:10]:
        print(n, round(obj.rank, 6))

    with open("pagerank_results.txt", "w") as f:
        for n, obj in sorted_nodes[:10]:
            f.write(f"{n} {obj.rank}\n")

    print("\nPageRank completed")


if __name__ == "__main__":
    load_graph("linkgraph.txt")
    pagerank()
    save()