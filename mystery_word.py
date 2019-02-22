#User inputs level of difficulty by selecting 1 of 3 options, if not, message tells user to enter one. You cannot bypass this. 
#When an easy level is selected, the computer generates a random word from a list. It can only be 4-6 characters. 

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

print(words)


#sort words in list by length
# create three seperate lists or simply output the values that fit the parameters
# check 2/22 video for clarity

#rename the lists

# user must enter level of difficulty

# x = input('Please select your level of difficulty - easy, medium, or hard: ')
# print('You selected: ',x)

# create a for loop with three seperate if statements

# for number_of_letters in words: 
#     if len('number_of_letters') >= 4 and <=6






# medium = []
# hard = []

#create main game loop