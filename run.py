import random
from hangman_part import parts
from time import sleep

class Game:
  """
  Get username input to start the game 
  """
  def __init__(self,username,welcome):
    self.username
    self.welcome
    print(f"Welcome the HangMan, {self.username}. Get ready to play")

username = input("Welcome to HangMan 😎\nPlease insert your name\n")
while len(username) < 1 or username.isalpha() is False:
  print('Please insert letters only ☠️ \n')
  username = input("Please insert you name\n")


def update():
   for i in correct:
    print(i, end=' ')
   print()
print('Let me think of a word', username)

def loading():
  for i in range(5):
    print('.', end = '' )
    sleep(0.4)
  print() 

loading() 

words = ['program', 'computer', 'hello']
picked = random.choice(words)
print('The word has', len(picked), 'letters.')
correct = ['_'] * len(picked)
wrong = []

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
        print("That's correct!")
      index += 1
    update()  
    parts(len(wrong))
   
  else:
      if guess not in wrong:
          wrong.append(guess)
          parts(len(wrong))
          print("That's not correct, try another letter. You wrote:", wrong)
      else:
          print('You already guessed that!') 
  if len(wrong) > 4:
    print('You loose 🫂')
    print(' I picked', picked)
    break      
  if '_' not in correct:
       print('Yay! You win 🙌🏼') 
       break

def replay(self):
        """
        Get the play input value to give to the user the chance to choose if 
        want play another game or close the match
        """
        play = input("Do you want to do another game y/n ??: ").upper()
        while play != 'Y' or play != 'N':
            if play == "Y":
                print('Brilliat!!')    
                replay = Game(self,username,welcome)
                replay.game_mode()
            elif play == "N":
                print("Thanks for your time")
                print('Game Over')
                exit()
            else:
                print("Invalid input, Y for yes and N for no ")
                play = input("Do you want to do another game y/n ??: ").upper()













