import os

files = os.listdir("Files/")

for file in files:

    if file == ".DS_Store":
        continue

    path = os.path.join("Files", file)

    with open(path, "r", encoding="ISO-8859-1") as f:
        content = f.read()

    lines = content.split("\n")

    if len(lines) == 0:
        continue

   
    first_line = lines[0]

    if "/" in first_line:
        parts = first_line.rsplit("/", 1)
        tag = parts[1].replace("EMAIL>", "/EMAILID>")
        lines[0] = parts[0] + tag

    new_content = "\n".join(lines)

    with open(path, "w", encoding="ISO-8859-1") as f:
        f.write(new_content)

print("Done processing files.")