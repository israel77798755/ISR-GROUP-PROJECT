docID = set()
linkgraph = {}
lg = {}
sinkNodes = set()

with open("linkgraph.txt", "r") as f:

    for line in f:
        parts = line.strip().split()

        if len(parts) == 0:
            continue

        node = parts[0]
        links = parts[1:]

        docID.add(node)

        if node not in linkgraph:
            linkgraph[node] = set()

        for l in links:
            docID.add(l)

            if l not in linkgraph:
                linkgraph[l] = set()

            linkgraph[l].add(node)

for node in linkgraph:
    if node in docID:
        lg[node] = linkgraph[node]

for node in lg:
    if len(lg[node]) == 0:
        sinkNodes.add(node)


with open("LinkGraphDummy.txt", "w") as out:
    for node in lg:
        out.write(node + " " + " ".join(lg[node]) + "\n")

print("Dummy graph built successfully")
print("Sink nodes count:", len(sinkNodes))