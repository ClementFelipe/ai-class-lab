import re

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    isOver = False
    isOver = self.verifyAdjacents(_PLAYER_SYMBOL)

    if isOver == False:
      isOver = self.verifyAdjacents(_MACHINE_SYMBOL)
      
      #gano la maquina
      if isOver == True:
        self.winner = _MACHINE
    #gano la persona
    else:
      self.winner = _PLAYER

    if isOver == False:
      isOver = True
      for item in self.board:
        if item == None:
          isOver=False
    

    return isOver

  def verifyAdjacents(self, symbol):
    threeAd = False

    if self.equalIndexs(0,1,2,symbol):
      threeAd = True
    elif self.equalIndexs(3,4,5,symbol):
      threeAd = True
    elif self.equalIndexs(6,7,8,symbol):
      threeAd = True
    elif self.equalIndexs(0,3,6, symbol):
      threeAd = True
    elif self.equalIndexs(1,4,7,symbol):
      threeAd = True
    elif self.equalIndexs(2,5,8,symbol):
      threeAd = True
    elif self.equalIndexs(0,4,8,symbol):
      threeAd = True
    elif self.equalIndexs(2,4,6,symbol):
      threeAd - True

    return threeAd

  def equalIndexs(self, i, j, k, symbol):
    if(self.board[i] == symbol and self.board[j] == symbol and self.board[k] == symbol):
      return True
    else:
      return False

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied

    for i, cell in enumerate(self.board):
      if cell is None:
        self.board[i] = _MACHINE_SYMBOL
        break

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o| 
    #   | | 
    #   | | 
    return self.board

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner

    pass
