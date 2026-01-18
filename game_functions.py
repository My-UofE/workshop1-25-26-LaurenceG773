import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if (current_val < next_val and user_input == 'h'):
        return True
    elif (current_val > next_val and user_input == 'l'):
        return True
    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter not in word:
        print(f"Sorry, {letter} is not in the word")
        return False
    i = 0
    for char in word:
        if char == letter:
            board[i] = letter
        i += 1
    print(f"Well done! {letter} is in the word")
    return True







