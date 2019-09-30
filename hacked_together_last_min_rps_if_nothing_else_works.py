import random
import camera
import sys
from PySide2.QtCore import QObject, Signal, Slot 
from PySide2.QtWidgets import * # QApplication, QDialog, QLineEdit, QPushButton, QLabel

def get_full_move_name(letter: str) -> str:
    return {"R": "rock", "P": "paper", "S": "scissors"}[letter]

def get_match_winner(human: str, computer: str) -> bool:
  """Determine the winner of a match of RPS. Returns -1 if the human won, 0 if tie, and 1 if computer won."""
  
  if human not in ["R","P","S"] or computer not in ["R","P","S"]:
    raise ValueError("Inputs must be either 'R', 'P', or 'S'!")

  if human == computer:
    return 0

  if human == "R":
    if computer == "S":
      return -1
    return 1
  
  if human == "P":
    if computer == "R":
      return -1
    return 1
  
  if human == "S":
    if computer == "P":
      return -1
    return 1

def get_computer_move() -> str:
    """Generates a move to be played by the computer."""

    return random.choice(["R", "P", "S"])

class Form(QDialog):

    def __init__(self, parent=None):
        self.H = 400
        self.W = 800 
        self.games_played = 0
        self.computer_wins = 0
        self.human_wins = 0
        super(Form, self).__init__(parent)
        self.setWindowTitle("RPS")
        self.setFixedSize(self.W, self.H)
        self.go_button = QPushButton("Go!", self)
        self.go_button.setFixedSize(150, 50)
        self.go_button.move((self.W - 150)/2, self.H-50)  # DON'T TOUCH
        self.go_button.clicked.connect(self.play_move)
        self.win_lose_text = QLabel('', self)
        self.win_lose_text.move(0, 0)
    @Slot()
    def play_move(self):
        computer_move = get_computer_move()
        human_move = camera.main()
        winner = get_match_winner(human_move, computer_move)
        if winner == -1:
          self.human_wins += 1
        elif winner == 1:
          self.computer_wins += 1 
        self.games_played += 1
        result = {1: "LOSE", 0: "TIE", -1: "WIN"}[winner] # MASSIVE HACK
        self.win_lose_text.setText(f"You played {get_full_move_name(human_move).upper()} and the computer played {get_full_move_name(computer_move).upper()} which means you {result}!\n\nComputer wins: {self.computer_wins}\nHuman wins: {self.human_wins}\nGames played: {self.games_played}")
        self.win_lose_text.adjustSize()

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())