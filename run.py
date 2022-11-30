import random

words = ['programe', 'computer', 'questions']

picked = random.choice(words)


correct = []
wrong = []

while True:

  guess = input("Please guess a letter\n")

  if guess in picked:
    correct.append(guess)
    print('Correct',correct)
  else:
    wrong.append(guess)
    print('wrong',wrong)
