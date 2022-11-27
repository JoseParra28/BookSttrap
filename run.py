
import random
import WORDS

word = "Secret"

errors = 6 
guesslist = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesslist:
            print(letter, end=" ")
        else:
            print(" ", end=" ")
    print("")
done = True

