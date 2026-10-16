# Text File Analyzer.

from collections import Counter
import string

filename = input("Enter text file path: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    characters = len(text)
    lines = text.splitlines()

    cleaned_words = [
        word.strip(string.punctuation).lower()
        for word in words
    ]

    cleaned_words = [word for word in cleaned_words if word]

    frequency = Counter(cleaned_words)

    print("\n===== FILE ANALYSIS =====")
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)

    print("\nTop 5 frequent words:")

    for word, count in frequency.most_common(5):
        print(f"{word}: {count}")

except FileNotFoundError:
    print("File not found.")

except OSError as error:
    print("Unable to read file:", error)