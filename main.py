import random
import time
import sys


def lets_play():
  human_choice = raw_input("Pick one: Rock, Paper or Scissors: \n").lower()
  choices = {
  1 : "rock",
  2 : "paper",
  3 : "scissors",
  }
  options = ("rock","paper","scissors")
  computer_choice = choices[random.randint(1,3)]
  if human_choice in options:
    if human_choice == computer_choice:
      print ("How predictable, both human and computer picked " + human_choice)
      print ("That was boring, try again")
      print ("\n")
      time.sleep(2)
      lets_play()
    if compare(human_choice.capitalize(),computer_choice.capitalize()):
      print (random.choice(loser_pc) + computer_choice +"!!")
      print ("Human is lucky, human beat the almighty computer!")
      play_again()
    else:
      print (random.choice(winning_pc) + " Computer picked " + computer_choice)
      print ("HA, HA, HA, computer beats you, human scum.")    
      play_again()
  else:
    print ("Play fair, only Rock, Paper or Scissors allowed. Try again")
    lets_play()

loser_pc =[
  "This stupid, silly computer picked ",
  "Unacceptable, I think I suck at this game, you beat my ",
  "You think this is funny human? You're just lucky this is random. I picked ",
  "404 Error: Computer can't beat you with ",
  "I would had preffered a full frontal assault with automated laser monkeys, scalpel mines and acid instead of picking ",
  "Human, please do not noogie me during combat prep. I was testing you with ",
  "It/'s strange. I have often dreamed of dying in combat. I/'m not enjoying it as much as I/'d hoped. Why did I choose "
  ]

winning_pc = [
  "Human, you've failed in your mission!",
  "Surrender your women and intellectuals!!",
  "You're looking very green today.",
  "You should consider upgrading yourself."
  ]


def compare(playerChoice,computerChoice):
    results = {('Paper','Rock') : True,
               ('Paper','Scissors') : False,
               ('Rock','Paper') : False,
               ('Rock','Scissors') : True,
               ('Scissors','Paper') : True,
               ('Scissors','Rock') : False}
    return results[playerChoice,computerChoice]

def game_start():
  begin = raw_input("Would you like to play Rock, Paper, Scissors? ").lower()
  while begin != "y" and begin != "yes":
    if begin == "n" or begin =="no":
      print("Yeah that's right, run away you chicken!")
      sys.exit()
    else:
      print("I'm a computer you dumb-dumb, I only accept YES or NO, try again.")
      begin = raw_input("Would you like to play Rock, Paper, Scissors? ").lower()
  lets_play()

def play_again():
  while True:
    begin = raw_input('Play again? \n').lower()
    while begin != "y" and begin != "yes":
      if begin == "n" or begin =="no":
        print("Yeah that's right, run away you chicken!")
        time.sleep(1)
        sys.exit()
      else:
        print("I'm a computer you dumb-dumb, I only accept YES or NO, try again.")
        begin = raw_input("Play again? \n").lower()
    lets_play()

game_start()  
