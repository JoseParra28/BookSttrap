import random

words = ['programe']

picked = random.choice(words)

print('The word has', len(picked), 'letters')


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
    index = 0 
    for i in picked:
      if i == guess:
        correct[index] = guess
      index += 1
    update()  
   
  else:
      if guess not in wrong:
          wrong.append(guess)
      else:
          print('You already guessed that!') 
      print(wrong)  
  if '_' not in correct:
       print('Yay! You win') 
       break





# user_name = input("Please insert your name: ")
# while len(user_name) < 1 or user_name.isalpha() is False:
#     print('Incorrect input. Please insert only letters')
    
#     user_name = input("Please insert your name: ")
