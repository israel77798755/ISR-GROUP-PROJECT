queries = ["151801", "151802", "151803"]
docs = [f"doc{i}" for i in range(1, 51)]

with open("qrels.txt", "w") as f:
    for q in queries:
        for i, d in enumerate(docs):
            relevance = 1 if i < 10 else 0
            f.write(f"{q} 0 {d} {relevance}\n")
