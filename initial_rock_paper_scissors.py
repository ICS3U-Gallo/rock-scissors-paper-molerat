import random

games = 0

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.RED + "WELCOME TO ROCK, PAPER , AND SCISSORS" + color.END)

def good_games():

   games = int(input("Please say how many games you would like to play: ")

   if games == 0:
      print("Ok, see you later")
      return
      
   if games < 0:
      print("Try typing that again.")
      good_games()
      
   else:
      print("Try typing that again."
      good_games()

def get_computer_move(previousMoves):
  if len(previousMoves)>2:
    if previousMoves[-1] == "s" and previousMoves[-2] == "s" and previousMoves[-3] == "s":
      return 3
      
    elif previousMoves[-1] == "p" and previousMoves[-2] == "p" and previousMoves[-3] == "p":
      return 1
    
    elif previousMoves[-1] == "r" and previousMoves[-2] == "r" and previousMoves[-3] == "r":
      return 2 
      
  return random.randint(1,3)

c=0
y=0
totalPlays = 0
previousMoves = ""
values = "spr" #1, 2, 3
bestoutof=int(input("pick a total score to reach for the win: "))

for games > 0:
   games = games + 1
   while c<bestoutof and y<bestoutof:
      totalPlays=totalPlays+1
      playerInput = input("please input either p or s or r: ")
      x=get_computer_move(previousMoves)
      print("your previous moves",previousMoves)
      if playerInput is "s" or "p" or "r":
         print("computer picks",values[x-1])
      else:
         continue

      if playerInput is "s" and  x == 1:
         print(color.BLUE + "You Tie!" + color.END)
    
      elif playerInput is "s" and x == 2:
         y = y+1
         print(color.GREEN + "You Win!" + color.END)
    
      elif playerInput is "s" and x == 3:
         c = c+1
         print(color.RED + "You Lose!" + color.END)
    
      elif playerInput is "p" and x == 1:
         c = c+1
         print(color.RED + "You Lose!" + color.END)
    
      elif playerInput is "p" and x == 2:
         print(color.BLUE + "You Tie!" + color.END)
    
      elif playerInput is "p" and x == 3:
         y = y+1
         print(color.GREEN + "You Win!" + color.END)
    
      elif playerInput is "r" and x == 1:
         y = y+1
         print(color.GREEN + "You Win!" + color.END)
    
      elif playerInput is "r" and x == 2:
         c = c+1
         print(color.RED + "You Lose!" + color.END)
    
      elif playerInput is "r" and x == 3:
         print(color.BLUE + "You Tie!" + color.END)
    
      print("play number:",totalPlays)  
  
      print("computer score:",c, "your score:",y)
  
      previousMoves = previousMoves+playerInput
  
if y == bestoutof:
  print("You Won the Match!")
else:
  print("The Computer Won the Match!")
