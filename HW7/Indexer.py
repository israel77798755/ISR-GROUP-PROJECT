import os
from bs4 import BeautifulSoup
import json
import time

path = "Files/"
start_time = time.time()

index = {}
i = 0


for filename in os.listdir(path):

    if filename == ".DS_Store":
        continue

    print(filename)

    file_path = os.path.join(path, filename)

    with open(file_path, "r", encoding="ISO-8859-1") as file:
        page = file.read()

    soup = BeautifulSoup("<root>" + page + "</root>", "html.parser")

    i += 1

    doc_id_tag = soup.find("emailid")
    text_tag = soup.find("text")
    label_tag = soup.find("label")

    doc_id = doc_id_tag.get_text().strip() if doc_id_tag else str(i)
    text = text_tag.get_text().strip() if text_tag else ""
    label = label_tag.get_text().strip() if label_tag else ""

    index[doc_id] = {
        "text": text,
        "label": label
    }

    print(f"Indexed {i} documents")


with open("local_index.json", "w") as f:
    json.dump(index, f, indent=2)


temp = time.time() - start_time

hours = int(temp // 3600)
temp -= hours * 3600

minutes = int(temp // 60)
seconds = int(temp - minutes * 60)

print(f"\nDone in {hours}:{minutes}:{seconds}")
print("Index saved to local_index.json")