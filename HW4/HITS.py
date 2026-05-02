from collections import defaultdict

graph = {}


class Node:
    def __init__(self):
        self.inlinks = set()
        self.outlinks = set()
        self.auth = 1.0
        self.hub = 1.0


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

                if link not in graph:
                    graph[link] = Node()

                graph[node].outlinks.add(link)
                graph[link].inlinks.add(node)


def hits(iterations=30):

    for _ in range(iterations):

        new_auth = {}
        new_hub = {}

        
        for n, obj in graph.items():
            new_auth[n] = sum(graph[i].hub for i in obj.inlinks)

       
        for n, obj in graph.items():
            new_hub[n] = sum(graph[o].auth for o in obj.outlinks)

        
        norm_a = sum(v * v for v in new_auth.values()) ** 0.5
        norm_h = sum(v * v for v in new_hub.values()) ** 0.5

        if norm_a != 0:
            for n in new_auth:
                new_auth[n] /= norm_a

        if norm_h != 0:
            for n in new_hub:
                new_hub[n] /= norm_h

        for n in graph:
            graph[n].auth = new_auth[n]
            graph[n].hub = new_hub[n]


def save_top():

    auth_sorted = sorted(graph.items(), key=lambda x: x[1].auth, reverse=True)
    hub_sorted = sorted(graph.items(), key=lambda x: x[1].hub, reverse=True)

    print("\n Top 10 Authorities:")
    for n, obj in auth_sorted[:10]:
        print(n, round(obj.auth, 6))

    print("\n Top 10 Hubs:")
    for n, obj in hub_sorted[:10]:
        print(n, round(obj.hub, 6))


if __name__ == "__main__":

    load_graph("linkgraph.txt")

    hits()

    save_top()

    print("\nNodes:", len(graph))

   
with open("hub.txt", "w") as f:
    for n, obj in graph.items():
        f.write(f"{n} {obj.hub}\n")

with open("auth.txt", "w") as f:
    for n, obj in graph.items():
        f.write(f"{n} {obj.auth}\n")