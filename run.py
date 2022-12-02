import random
from hangman_part import parts
from time import sleep

class game:
  """
  Get username input to start the game 
  """
  def __init__(self,username):
    self.username
    print(f"Welcome the HangMan, {self.user_name}. Get ready to play")

def main():
  """
  Run input pre-game and restart 
  """ 
username = input("Please insert your name\n")
while len(username) < 1 or username.isalpha() is False:
  print('Please insert letter only\n')
  username = input("Please insert you name")

words = ['program', 'computer', 'hello']
picked = random.choice(words)
print('The word has', len(picked), 'letters.')
correct = ['_'] * len(picked)
wrong = []


def update():
   for i in correct:
    print(i, end=' ')
   print()
print('Let me think of a word')

def loading():
  for i in range(5):
    print('.', end = '' )
    sleep(0.4)
  print() 

loading() 

update() 
parts(len(wrong)) 

while True:

  guess = input("Please guess a letter\n")
  print('Let me check')
  loading()

  if guess in picked:
    index = 0 
    for i in picked:
      if i == guess:
        correct[index] = guess
      index += 1
    update()  
    parts(len(wrong))
   
  else:
      if guess not in wrong:
          wrong.append(guess)
          parts(len(wrong))
      else:
          print('You already guessed that!') 
      print(wrong)
  if len(wrong) > 4:
    print('You loose')
    print(' I picked', picked)
    break      
  if '_' not in correct:
       print('Yay! You win😎') 
       break










# user_name = input("Please insert your name: ")
# while len(user_name) < 1 or user_name.isalpha() is False:
#     print('Incorrect input. Please insert only letters')
    
#     user_name = input("Please insert your name: ")
