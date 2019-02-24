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

# running = True

# while running:
#     x = input('Please select your level of difficulty - easy, medium, or hard: ')
#     print('You selected: ', x)
#     if x == 'easy':
#         running = False
#         print("let's play!")
#     if x == 'medium':
#         running = False
#         print("let's play!")
#     if x == 'hard':
#         running = False
#         print("let's play!")
#     if x not in ['easy', 'medium', 'hard']:     
#         print('you must enter easy, medium, or hard')

    


guesses_taken = 0

print('Hello! What is your name?')
myName = input()

auto_selected_word = random.choice('words').lower

print('Well, ' + myName + ', I am thinking of a word, and you must guess it.')

for guessesTaken in range(8):
    print('Take a guess.') 
    guess = input()
    guess = guess.lower()
    blanks = '_' * len(auto_selected_word)

    # char needs to be defined. not sure how to do this. It also needs to be recognized as a non-integer

    if guess == char in auto_selected_word:
        print() # you have to tell it to replace a blank with a letter 

    if guess != char in auto_selected_word:
        print('Sorry ' + () 'is not a letter in word, guess again')

    if guess == auto_selected_word:
        break

if guess == auto_selected_word:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my word in ' +
      guessesTaken + ' trys!')

if guess != auto_selected_word:
    number = str(number)
    print('Sorry, the word I was thinking of was ' + number + '.')