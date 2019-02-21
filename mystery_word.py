# print("Welcome to word guess!")
# print("Please select your level of difficulty: easy, medium, hard")

import string

#tell the computer that words is word.txt - use with open so it will close the file when its done reading it


def normalize_text(text):
    """Takes text and removes punctuation and replaces whitespace with normal spaces- compressing single spaces"""
    text = text.lower()
    valid_chars = string.ascii_letters + string.whitespace + string.digits # check for valid chars add them to new var

    #remove punctuation
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char
    text = new_text
    text = text.replace("\n", " ")
    return text

with open('words.txt') as f: 
    words = f.read()

print(words)