import os
import random

spam_words = ["win", "free", "money", "prize", "click", "offer"]
ham_words = ["meeting", "project", "schedule", "report", "discussion"]

def generate_email(email_id, label):

    if label == "spam":
        words = random.choices(spam_words, k=20)
    else:
        words = random.choices(ham_words, k=20)

    text = " ".join(words)

    content = f"""<EMAILID>{email_id}</EMAILID>
<TEXT>{text}</TEXT>
<LABEL>{label}</LABEL>
"""

    return content


def main():

    if not os.path.exists("Files"):
        os.makedirs("Files")

    emails = []

    for i in range(200):

        email_id = str(1000 + i)

        label = "spam" if i < 100 else "ham"

        email_content = generate_email(email_id, label)

        emails.append((email_id, label))

        with open(f"Files/{email_id}.txt", "w") as f:
            f.write(email_content)

    print("Generated emails:", len(emails))


if __name__ == "__main__":
    main()