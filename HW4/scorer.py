def score_evaluator(file_path):

    score_holder = 0.0

    try:
        with open(file_path, "r") as f:

            for line in f:
                parts = line.strip().split()

                if len(parts) < 2:
                    continue

                try:
                    score_holder += float(parts[1])
                except:
                    continue

    except FileNotFoundError:
        print(f"Missing file: {file_path}")
        return 0.0

    return score_holder


if __name__ == "__main__":

    hub_score = score_evaluator("hub.txt")
    auth_score = score_evaluator("auth.txt")
    pr_score = score_evaluator("pagerank_results.txt")

    print("Total hub score:", hub_score)
    print("Total authority score:", auth_score)
    print("Total PageRank score:", pr_score)