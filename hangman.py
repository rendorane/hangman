import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    all_letters = set(string.ascii_uppercase)
    used_letters = set()
    lives = 5

    while len(word_letters) > 0 and lives > 0:
        for letter in word:
            if letter in used_letters:
                print(letter, end=' ')
            else:
                print('-', end=' ')
        print()
        user_letter = input("Guess a letter: ").upper()
        if user_letter in all_letters - used_letters:
            used_letters.add(user_letter)
            print("Used letters:", ' '.join(used_letters))
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good choice!")
            else:
                lives -= 1
                print("Wrong! You have {} lives left".format(lives))
        elif user_letter in used_letters:
            print("You already used that letter.")
        else:
            print("Invalid character.")
        print()
    if lives == 0:
        print("W A S T E D")
    else:
        print("You win!")


hangman()
