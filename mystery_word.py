# print("Welcome to word guess!")
# print("Please select your level of difficulty: easy, medium, hard")

import string
import random


def normalize_text(text):
    """Takes text and removes punctuation and replaces whitespace with normal spaces- compressing single spaces"""
    text = text.lower()
    valid_chars = string.ascii_letters + string.whitespace + \
        string.digits  # check for valid chars add them to new var

    # remove punctuation
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char
    text = new_text
    text = text.replace("\n", " ")
    return text

# tell the computer that words is word.txt - use with open so it will close the file when its done reading it


with open('words.txt') as f:
    words = f.read()

# print(words)

# user must enter level of difficulty
level_of_difficulty = input("easy", "medium", "hard")

#turn this to a while not loop

while level_of_difficulty == (input):

    if level_of_difficulty != (input):
        return(print("You must enter easy, medium, hard, or just go play something else"))

    if level_of_difficulty == "easy":
        # program needs to slect proper list
        # program print the word/spaces

    elif level_of_difficulty == "medium":
     # program needs to slect proper list
     # program print the word/spaces

    elif level_of_difficulty == "hard":
        # program needs to slect proper list
        # program print the word/spaces


def level_of_difficulty(user_input="Welcome to word guess, please enter your level of difficulty: easy, medium, or hard")


# create a for loop with three seperate if statements
easy = []
medium = []
hard = []


print("Great, you selected " + level_of_difficulty)
