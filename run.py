import random

words = ['programe', 'computer', 'questions']

picked = random.choice(words)

print('The word has', len(picked), 'letters.')


correct = ['_'] * len(picked)
wrong = []

def update():
  for i in correct:
    print(i, end=' ')
  print()

update()  

while True:

  guess = input("Please guess a letter\n")

  if guess in picked:
    correct.append(guess)
    print('Correct',correct)
  else:
    wrong.append(guess)
    print('wrong',wrong)
