# Tic - Tac - Toe
# author: Hector Rodriguez

# Board

board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

currentplayer = "x"
winner = None
running = True

def main(board):
    print("__________")
    print(board[0] + " + " + board[1] + " + " + board[2])
    print(board[3] + " + " + board[4] + " + " + board[5])
    print(board[6] + " + " + board[7] + " + " + board[8])
    print("__________")
main(board)

# player 1
def playerinp(board):
    inp = int(input("Please enter a number betwen 1 to 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print ("Number already used, please try different number")

def checkhorin(board):
    global winner        
    if board[0] == board[1] == board[2] and board [1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board [6]
        return True

 def checkroad(board):
     global winner
     if board[0] == board[3] ==board[6] and board[0] != "-":
         return True
    elif board[1] == board[4] ==board[7] and board[1] != "-":
        return True
    elif board[2] == board[5] ==board[8] and board[2] != "-":
        return True

def checkdia(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] ==board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checktie(board):
    global running
    if"=" not in board:
        main(board)
        print("It's a tie")
        running = False

def checkwin():
    if checkdia(board) or checkhorin(board) or checkroad(board)
    print("The winner is {winner}")

def secplayer():
    global playerinp
    if playerinp == "x":
        playerinp = "O"
    else:
        player = "x"


while running:
    main(board)
    playerinp(board)
    checkwin()
    checktie(board)
    secplayer()
