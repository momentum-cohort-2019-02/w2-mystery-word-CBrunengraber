# import random
# import string


# def normalize_text(text):
#     """Takes text and removes punctuation and replaces whitespace with normal spaces- compressing single spaces"""
#     text = text.lower()
#     valid_chars = string.ascii_letters + string.whitespace + \
#         string.digits  # check for valid chars add them to new var

#     # remove punctuation
#     new_text = ""
#     for char in text:
#         if char in valid_chars:
#             new_text += char
#     text = new_text
#     text = text.replace("\n", " ")
#     return text   
  
#open the file and put it into a format that Python can understand
# with open('words.txt') as file:
#     words = file.read().splitlines() 

    # print(words)

word_to_guess = "racecar"
letters_guessed = []

def word_guessed(word_to_guess, letters_guessed):
    for letter in word_to_guess:
        if letter not in letters_guessed:
            return False
        return True    

def is_letter_input(user_input):
    return len(user_input) == 1 and user_input.isalpha()

def get_letter_input():
    user_input = input('Type a letter to guess: ').casefold()
    while not is_letter_input(user_input):
        print("That was not a letter.")    
        user_input = input('Type a letter to guess: ').casefold()

    return user_input


if __name__ == "__main__":
    while not word_guessed(word_to_guess, letters_guessed):
        letter_guessed = get_letter_input()
        letters_guessed.append(letter_guessed)
     






#get random words into game
# def auto_selected_word(words):          
#     return random.choice(words).lower()    

#main area of the game: this will be the main function to call the game overall


#sort words into different lengths to be "called by level when" list is accessed
#get level from user
#get word from list based on the level
#get guesses from the user
#start function