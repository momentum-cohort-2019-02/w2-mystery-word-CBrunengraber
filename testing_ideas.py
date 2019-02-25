import random
import string


#get random words into game
def auto_selected_word(words):          
    return random.choice(words).lower()

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

def difficulty(words, difficulty):  # IF STATEMENT - CONDITION IS MET THAN -----X HAPPENS, NOT A REPEATING LOOP
    if difficulty = "easy": 
        # select words from list 4-6 letters       
    if difficulty = "normal":
        # select words from list 6-8 letters
    if difficulty = "hard":
        # select words from list += 8 letters
  
#open the file and put it into a format that Python can understand
with open('words.txt') as file:
    words = file.read().splitlines() 

    # print(words)

#main area of the game: this will be the main function to call the game overall
if __name__ == "__main__":
    level = input([easy, medium, false])      
#sort words into different lengths to be "called by level when" list is accessed
#get level from user
#get word from list based on the level
#get guesses from the user
#start function