import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    # Create a copy of the letter pool dictionary
    letter_pool = LETTER_POOL.copy()

    # Draw 10 letters from the pool
    letters = []
    for i in range(10):
        letter = random.choice(list(letter_pool.keys()))
        while letter_pool[letter] == 0:
            letter = random.choice(list(letter_pool.keys()))
        letters.append(letter)
        letter_pool[letter] -= 1

    # Return the list of drawn letters
    return letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass