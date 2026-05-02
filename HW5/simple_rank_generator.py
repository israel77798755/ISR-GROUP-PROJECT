import random

queries = ["151801", "151802", "151803"]
docs = [f"doc{i}" for i in range(1, 51)]

with open("rankList.txt", "w") as f:
    for q in queries:
        shuffled = docs.copy()
        random.shuffle(shuffled)   
        for i, d in enumerate(shuffled):
            score = random.random()  
            f.write(f"{q} Q0 {d} {i+1} {score} EXP\n")