#This is the drawing of the tic tac toe board a 2x2 array
''' 
7  |  8  |  9
--------------
4  |  5  |  6
--------------
1  |  2  |  3

To insert in the grid replicate your
number pad in the keyboard.
'''
boardStatus = [
    [ '-', '-', '-' ], 
    [ '-', '-', '-' ], 
    [ '-', '-', '-' ] 
]

# This function checks the best move for AI by calling minimax and places the best move in the boardStatus
def bestMoveForAi():
  bestPoint = -1000
  for i in range (3):
    for j in range (3):
      if (boardStatus[i][j] == '-'):
        boardStatus[i][j] = 'X'
        point = minimax(boardStatus, 0, False)
        boardStatus[i][j] = '-'
        if (point > bestPoint):
          bestPoint = point
          move = [i,j]
  boardStatus[move[0]][move[1]] = 'X'
  
  print("---AI Move---")
  for i in range (3):
    print(boardStatus[i])
  print("")
  print("")



#This function checks if 3 values passed are same either 'X' or 'O'
def checkEqual3(a, b, c):
  return a == b and b == c and a != '-'


#This function checks if there is any winner and returns the sign of the winner
def checkForWinner():
  winner = None

  #checks if vertical has the same player
  for i in range (3):
    if (checkEqual3(boardStatus[i][0], boardStatus[i][1], boardStatus[i][2])):
      winner = boardStatus[i][0]

  #checks if horizontal has the same player
  for i in range (3):
    if (checkEqual3(boardStatus[0][i], boardStatus[1][i], boardStatus[2][i])):
      winner = boardStatus[0][i]

  #checks if the Diagonal has the same player
  if (checkEqual3(boardStatus[0][0], boardStatus[1][1], boardStatus[2][2])):
    winner = boardStatus[0][0]

  if (checkEqual3(boardStatus[2][0], boardStatus[1][1], boardStatus[0][2])):
    winner = boardStatus[2][0]

  openSpots = 0
  for i in range (3):
    for j in range (3):
      if (boardStatus[i][j] == '-'):
        openSpots=openSpots+1

  if (winner == None and openSpots == 0):
    return 'tie'
  else:
    return winner



#This the minimax algorithm which needs parameter boardStatus situation, depth and isMaximizing
#This function returns the best possible point for the AI to judge the best move
def minimax(boardStatus, depth, isMaximizing):
  result = checkForWinner()
  if (result != None):    
    if (result=='O'):
      return -10+depth
    elif (result=='X'):
      return 10-depth
    else:
      return 0

  if (isMaximizing):
    bestPoint = -1000
    for i in range (3):
      for j in range (3):
        if (boardStatus[i][j] == '-'):
          boardStatus[i][j] = 'X'
          point = minimax(boardStatus, depth + 1, False)
          boardStatus[i][j] = '-'
          bestPoint = max(point, bestPoint)
    return bestPoint

  else:
    bestPoint = 1000
    for i in range (3):
      for j in range (3):
        if (boardStatus[i][j] == '-'):
          boardStatus[i][j] = 'O'
          point = minimax(boardStatus, depth + 1, True)
          boardStatus[i][j] = '-'
          bestPoint = min(point, bestPoint)
    return bestPoint



#This is human turn where player is required to give input as per number pad to place 'O' in the boardStatus
def forHumanTurn():
    moves = {
        7: [0, 0], 8: [0, 1], 9: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        1: [2, 0], 2: [2, 1], 3: [2, 2],
    }
    move = input('Use numpad to enter (1..9): ')
    if (move=='1' or move=='2' or move=='3' or move=='4' or move=='5' or move=='6' or move=='7' or move=='8' or move=='9'):
      coordinates=moves[int(move)]
      if(boardStatus[coordinates[0]][coordinates[1]]=="-"):
        boardStatus[coordinates[0]][coordinates[1]]="O"
        print("---Your Move---")

        for i in range (3):
          print(boardStatus[i])
        print("")
        print("")
        if (checkForWinner()==None):
          bestMoveForAi()
      else:
        print("-- That place is already taken choose another move : --")
        forHumanTurn()
    else:
      print("--       Please enter a correct input                --")


#This checks if the game is over or not
def checkIsGameOver():
  won=checkForWinner()
  if (won!=None):
    if (won=='X' or won=='O'):
      print("The winner is: "+str(won)) 
      endFunction()
    else:
      print("Draw")
      endFunction()
    return True
  else: 
    return False



#This is the ending function of the program
def endFunction():
  print("--------------------------------------------------")
  print("|                                                |")
  print("|              The game ended !                  |")
  print("|        Type 'y' for yes and 'n' for no         |")
  print("|             Do you want to play again?         |")
  print("|                                                |")
  print("--------------------------------------------------")
  ans=input("").upper()
  if (ans=="Y"):
    for i in range (3):
      for j in range (3):
        boardStatus[i][j]="-"
    main()
  elif (ans=="N"):
    print("|         Hope you enjoyed playing.              |")
  else:
    print("|        Choose the correct option               |")
    endFunction()


#This is the main method which runs when the program starts
def main():
  print("--------------------------------------------------")
  print("|                                                |")
  print("|         You can win the game by making         |")
  print("|         3 of your playing sign in a row        |")
  print("|         horizontal, vertical or diagonal       |")
  print("|                                                |")
  print("--------------------------------------------------")
  print("")
  print("")
  print("--------------------------------------------------")
  print("|                                                |")
  print("|            'X' is AI.    'O' is human.         |")
  print("|       Do you want to go first or second        |")
  print("|     Type 1 to go first and 2 to go second      |")
  print("|                                                |")
  print("--------------------------------------------------")
  print("")
  turn = input(" Enter here: ")
  
  if (turn=="1"):
    print("")
    print("|        Follow the number pad tutorial.         |")
    print("|              7  |  8  |  9                     |")
    print("|              --------------                    |")
    print("|              4  |  5  |  6                     |")
    print("|              --------------                    |")
    print("|              1  |  2  |  3                     |")
    print("|                                                |")
    print("--------------------------------------------------")
    print("Press the number according to the place in the grid")
    for i in range (5):
      forHumanTurn()
      if (checkIsGameOver()):
        break
      
  elif(turn=="2"): 
    print("")
    print("|        Follow the number pad tutorial.         |")
    print("|              7  |  8  |  9                     |")
    print("|              --------------                    |")
    print("|              4  |  5  |  6                     |")
    print("|              --------------                    |")
    print("|              1  |  2  |  3                     |")
    print("|                                                |")
    print("--------------------------------------------------")
    print("Press the number according to the place in the grid")
    bestMoveForAi()
    if (not checkIsGameOver()):
      for i in range (4):
        forHumanTurn()
        if (checkIsGameOver()):
          break

  else:
    print("--------- Please choose correct option ----------")
    main()
  
main()