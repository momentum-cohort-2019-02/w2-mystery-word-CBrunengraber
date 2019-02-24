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


with open('words.txt') as file:
    # words = file.read()
    # - this gave me a long list that had no commas
    # put into a list python can understand
    words = file.read().splitlines() 
    # now - sort your lists

# print(words) - run this if you need to see what the words look like and in what format

running = True

while running:
    x = input('Please select your level of difficulty - easy, medium, or hard: ')
    print('You selected: ', x)
    if x == 'easy':
        running = False
        print("let's play!")
    if x == 'medium':
        running = False
        print("let's play!")
    if x == 'hard':
        running = False
        print("let's play!")
    if x not in ['easy', 'medium', 'hard']:     
        print('you must enter easy, medium, or hard')



game_loop = True

while game_loop:
    choices = ('words') #
    auto_selected_word = random.choice(words).lower
    guesses = 0 # other games online set this to none - this is where the user guesses letters
    guessed_letters = [] #users guesses get put here
    unguessed_word = [] #replaces letters of unguessed word with dashes
    for letter in auto_selected_word:
        unguessed_word.append('_') # this should add letters guessed to the underscore until the word is completed
    attempts = 12   