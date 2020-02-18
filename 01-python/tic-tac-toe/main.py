from tic_tac_toe import TicTacToeGame

def play():
  game = TicTacToeGame()

  while not game.is_over:
    game.play()
    game.print()

if __name__ == "__main__":
  play()
