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

# user_name = input("Please insert your name: ")
# while len(user_name) < 1 or user_name.isalpha() is False:
#     print('Incorrect input. Please insert only letters')
    
#     user_name = input("Please insert your name: ")
