import string  #imports always at the top
import random

def auto_selected_word(words):          
    return random.choice(words).lower


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



difficulty = True  

while difficulty:
    level = input('Please select your level of difficulty - easy, medium, or hard: ')
    print('You selected: ', level)
    if level == 'easy':
        difficulty = False
        print("let's play!")
    if level == 'medium':
        difficulty = False
        print("let's play!")
    if level == 'hard':
        difficulty = False
        print("let's play!")
    if level not in ['easy', 'medium', 'hard']:     
        print('you must enter easy, medium, or hard')



                

            #using level as a parameter, make a function that will let you have a word list of difficulty selected for you based on easy, medium or hard ----- return level_emh - look at what taylor posted
# create one words list with randomizer that was written below

#sort words in list by length


# check 2/22 video for clarity

# create a for loop with three seperate if statements

# for number_of_letters in words: 
#     if len('number_of_letters') >= 4 and <=6


#create main game loop - MUST BE DEFINED FIRST - THEN MAKE THIS THE MAIN CALL - should it be a class instead?
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



# game_loop = True # this should make the game run, and it will be false when won or lost

# while game_loop:
#     choices = ('words') #not sure if this needs brackets instead, and if it should exist outside loop. 

#     guesses = 0 # other games online set this to none, not sure why - this is where the user guesses letters
#     guessed_letters = [] #users guesses get put here
#     unguessed_word = [] #replaces letters of unguessed word with dashes
#     for letter in auto_selected_word:
#         unguessed_word.append('_') # this should add letters guessed to the underscore until the word is completed
#     attempts = 8