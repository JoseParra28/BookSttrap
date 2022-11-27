import random
from word import wordsjson

def get_word():
    word = random.choice(wordsjson)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7 
    print("Let's play Handman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n") 
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter," guess)
        elif guess not in word:
            print(guess, "is not the word.")
            tries -= 1
            guessed_letters.append(guess)
            
            else:
            
            print("Good job", guess, "is the right word!")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                    word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                    guessed = True    
        elif len(guess) == len(word) and guess.isalpha():

            else:

            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")