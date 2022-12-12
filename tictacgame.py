# --------- Global Variables -----------
import random

# Will hold our game board data
board = ["-","-","-","-","-",
         "-","-","-","-","-",
         "-","-","-","-","-",
         "-","-","-","-","-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
playerlist=["X","O"]
current_player = random.choice(playerlist)


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] +"   1 | 2 | 3 | 4")
  print(board[4] + " | " + board[5] + " | " + board[6] + " | " + board[7] +"   5 | 6 | 7 | 8")
  print(board[8] + " | " + board[9] + " | " + board[10] + " | " + board[11] +"   9 | 10| 11| 12")
  print(board[12]+ " | " + board[13] + " | " + board[14] + " | " + board[15] + "   13| 14| 15| 16")
  print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  if player=="X":
    position = input("Choose a position from 1-16: ")
    p=int(position)
    while p not in range(1,17):
      position = input("Choose a position from 1-16: ")
      p=int(position)
  elif player=="O":
    pos=random.randint(1,16)
    position =pos
    

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:
      
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      if player=="X":
        print("You can't go there. Go again.")
        position = input("Choose a position from 1-16: ")
      else:
        pos=random.randint(1,16)
        position =pos
  if player=="O":
    print("computer choses:",position+1)      

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()


# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2]== board[3] != "-"
  row_2 = board[4] == board[5] == board[6]== board[7] != "-"
  row_3 = board[8] == board[9] == board[10]== board[11] != "-"
  row_4 = board[12] == board[13] == board[14]== board[15] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3 or row_4:
    game_still_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[4] 
  elif row_3:
    return board[8]
  elif row_3:
    return board[12]
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[4] == board[8]== board[12] != "-"
  column_2 = board[1] == board[5] == board[9]== board[13] != "-"
  column_3 = board[2] == board[6] == board[10]== board[14] != "-"
  column_4 = board[3] == board[7] == board[11]== board[15] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2]
  elif column_4:
    return board[3]
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[5] == board[10]== board[15] != "-"
  diagonal_2 = board[3] == board[6] == board[9]== board[12] != "-"
  diagonal_3 = board[1] == board[6] == board[11] != "-"
  diagonal_4 = board[2] == board[5] == board[8] != "-"
  diagonal_5 = board[4] == board[9] == board[14] != "-"
  diagonal_6 = board[7] == board[10] == board[13] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2 or diagonal_3 or diagonal_4 or diagonal_5 or diagonal_6 :
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[3]
  elif diagonal_3:
    return board[1]
  elif diagonal_4:
    return board[2]
  elif diagonal_5:
    return board[4]
  elif diagonal_6:
    return board[7]
  # Or return None if there was no winner
  else:
    return None


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def flip_player():
  # Global variables we need
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
