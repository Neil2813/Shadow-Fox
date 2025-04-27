import random
try:
    from getpass import getpass
except ImportError:
    getpass = input

HANGMAN_STAGES = [stage.strip("\n") for stage in [
"""
   +---+
   |   |
       |
       |
       |
       |
=========
""",
"""
   +---+
   |   |
   O   |
       |
       |
       |
=========
""",
"""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
""",
"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
""",
"""
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========
""",
"""
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
""",
"""
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
"""
]]

WORDS = {
    'fruits': {
        'easy': ['apple', 'pear', 'plum', 'kiwi', 'lime'],
        'medium': ['banana', 'orange', 'papaya', 'mango', 'grapes'],
        'hard': ['pineapple', 'watermelon', 'pomegranate', 'blackberry', 'raspberry']
    },
    'animals': {
        'easy': ['cat', 'dog', 'cow', 'pig', 'hen'],
        'medium': ['tiger', 'monkey', 'panda', 'zebra', 'giraffe'],
        'hard': ['hippopotamus', 'alligator', 'chameleon', 'rhinoceros', 'elephant']
    },
    'colors': {
        'easy': ['red', 'blue', 'green', 'pink', 'gray'],
        'medium': ['orange', 'purple', 'yellow', 'maroon', 'indigo'],
        'hard': ['turquoise', 'magenta', 'chartreuse', 'aquamarine', 'fuchsia']
    }
}

ATTEMPTS = {
    'easy': 6,
    'medium': 5,
    'hard': 4
}

def get_random_word(difficulty):
    theme = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[theme][difficulty])
    return word

def get_word_from_player():
    while True:
        word = getpass("Player 1, enter the secret word (letters only): ").strip().lower()
        if not word.isalpha():
            print("Invalid word. Use letters only.")
        else:
            print("\n" * 50)
            return word

def display_progress(secret_word, correct_guesses, wrong_guesses, attempts_left):
    print(HANGMAN_STAGES[len(wrong_guesses)])
    display = ''
    for letter in secret_word:
        if letter in correct_guesses:
            display += letter + ' '
        else:
            display += '_ '
    print("Word:", display.strip())
    print("Wrong guesses:", ' '.join(wrong_guesses))
    print(f"Attempts left: {attempts_left}")

def play_game(secret_word, max_attempts):
    secret_word = secret_word.lower()
    correct_guesses = []
    wrong_guesses = []
    attempts_left = max_attempts

    while attempts_left > 0:
        display_progress(secret_word, correct_guesses, wrong_guesses, attempts_left)
        if all(letter in correct_guesses for letter in secret_word):
            print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
            return
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Enter a single letter.")
            continue
        if guess in correct_guesses or guess in wrong_guesses:
            print("You've already guessed that letter. Try again.")
            continue
        if guess in secret_word:
            correct_guesses.append(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_guesses.append(guess)
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    display_progress(secret_word, correct_guesses, wrong_guesses, attempts_left)
    print(f"Game Over. The word was '{secret_word}'.")

def main():
    print("Welcome to Hangman!\n")
    mode = ''
    while mode not in ['1', '2']:
        mode = input("Choose mode: 1) Single-player 2) Multiplayer: ").strip()
    if mode == '1':
        diff = ''
        while diff not in ['easy', 'medium', 'hard']:
            diff = input("Choose difficulty (easy, medium, hard): ").strip().lower()
        word = get_random_word(diff)
        print("A secret word has been chosen. Let's begin!")
        play_game(word, ATTEMPTS[diff])
    else:
        diff = ''
        while diff not in ['easy', 'medium', 'hard']:
            diff = input("Choose difficulty (easy, medium, hard): ").strip().lower()
        word = get_word_from_player()
        print("Let's start guessing!")
        play_game(word, ATTEMPTS[diff])

if __name__ == "__main__":
    main()
