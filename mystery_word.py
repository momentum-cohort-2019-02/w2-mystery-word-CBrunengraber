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

# print(words) 
# - run this if you need to see what the words look like and in what format
# user must now enter level of difficulty

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


#sort words in list by length

# create three seperate lists or simply output the values that fit the parameters

# check 2/22 video for clarity

#rename the lists

# create a for loop with three seperate if statements

# for number_of_letters in words: 
#     if len('number_of_letters') >= 4 and <=6






# medium = []
# hard = []

#create main game loop
# user must guess a hidden word in 12 trys or lose
# *****how to get into game loop after completing above loop?******
# I need the words to be brought into the game *****can they be defined and left outside loops or have to be put in each time?
# words must be randomly selected for the user
# letters must be guessed at
# letters must be hidden and replaced with underscores, letters only shown when guessed
# keep track of number of guesses
# keep track of letters guessed
# if user enters a guessed letter, print statement to select another letter
# if user selects anything other than 1 letter (numbers, symbols, more than one letter), print statement telling them to select an unguessed letter. 
# limit the number of attempts to 8 (****are any words in the list going to fall outside this spectrum?)



game_loop = True # this should make the game run, and it will be false when won or lost

while game_loop:
    choices = ('words') #not sure if this needs brackets instead, and if it should exist outside loop. 
    auto_selected_word = random.choice(words).lower
    guesses = 0 # other games online set this to none, not sure why - this is where the user guesses letters
    guessed_letters = [] #users guesses get put here
    unguessed_word = [] #replaces letters of unguessed word with dashes
    for letter in auto_selected_word:
        unguessed_word.append('_') # this should add letters guessed to the underscore until the word is completed
    attempts = 8