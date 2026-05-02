import os
import math
import re
import dill
from collections import defaultdict

CRAN_FILE = "cran.all.1400"
OUTPUT_DIR = "Pickles"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def tokenize(text):
    
    return re.findall(r"[a-z0-9]+(?:\.[a-z0-9]+)*", text.lower())

with open(CRAN_FILE, "r", encoding="utf-8") as f:
    data = f.read()

docs = data.split(".I ")[1:]

print(f"Total documents found: {len(docs)}")

inverted_index = defaultdict(lambda: defaultdict(list))
doc_lengths = {}
doc_ids = {}

term_to_id = {}
doc_to_id = {}

term_id_counter = 0
doc_id_counter = 0

total_tokens = 0
total_terms = 0

for doc in docs:
    lines = doc.split("\n")

    doc_no = lines[0].strip()

    text = []
    capture = False

    for line in lines:
        if line.strip() == ".W":
            capture = True
            continue
        if capture:
            text.append(line)

    text = " ".join(text)
    tokens = tokenize(text)

    if doc_no not in doc_to_id:
        doc_to_id[doc_no] = doc_id_counter
        doc_id_counter += 1

    doc_id = doc_to_id[doc_no]
    doc_lengths[doc_id] = len(tokens)

    total_tokens += len(tokens)

    position = 0

    for token in tokens:
        position += 1

        if token not in term_to_id:
            term_to_id[token] = term_id_counter
            term_id_counter += 1

        term_id = term_to_id[token]

        inverted_index[term_id][doc_id].append(position)

vocab_size = len(term_to_id)
total_docs = len(doc_to_id)

print("Vocabulary size:", vocab_size)
print("Total docs:", total_docs)


final_index = {}

for term, postings in inverted_index.items():
    df = len(postings)
    cf = sum(len(pos) for pos in postings.values())

    final_index[term] = {
        "df": df,
        "cf": cf,
        "postings": {}
    }

    for doc, positions in postings.items():
        final_index[term]["postings"][doc] = {
            "tf": len(positions),
            "positions": positions,
            "doc_len": doc_lengths[doc]
        }

dill.dump(final_index, open(os.path.join(OUTPUT_DIR, "index.pkl"), "wb"))
dill.dump(term_to_id, open(os.path.join(OUTPUT_DIR, "term_to_id.pkl"), "wb"))
dill.dump(doc_to_id, open(os.path.join(OUTPUT_DIR, "doc_to_id.pkl"), "wb"))
dill.dump(doc_lengths, open(os.path.join(OUTPUT_DIR, "doc_lengths.pkl"), "wb"))


stats = {
    "V": vocab_size,
    "N": total_docs,
    "total_tokens": total_tokens
}

dill.dump(stats, open(os.path.join(OUTPUT_DIR, "stats.pkl"), "wb"))

print("\nINDEXING COMPLETE")
print("Files saved in Pickles/")