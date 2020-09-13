'''Minesweeper game!
Meraj Mostamand Kashi'''

import random
import os,sys

# read size of the game board and number of mines
row,col = input("Please enter your screen size: [ X,Y ]:  ").split(",")
mines=int(input("How many mines do you want to put in: "))

screen= [['?']*int(col) for i in range(int(row))]  #create masking matrix
board= [[0]*int(col) for i in range(int(row))] #creating default board matrix

# Function to print out the board!
def PrintOut(matrix):
    if sys.platform=='linux': os.system('clear') #Clearing screen
    elif sys.platform=='windows': os.system('cls')  
    row_asci=65
    print(" ",end=" ")
    for ch in range (len(matrix[0])):
        print(chr(row_asci),end="   ")
        row_asci+=1
    print("\r")
    for i in range(len(matrix)):
        print(i+1,end=" ")
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="   ")
        print("\r")

# Put Mines on the board
for i in range(mines):
    board[random.randint(0,int(row)-1)][random.randint(0,int(col)-1)]='*' # put mines on the board matrix randomely
for i_t in range(int(row)): # put number of other arreis considering mines positions 
    for j_t in range(int(col)):
        if board[i_t][j_t]!='*':
            i_first_point=i_t-1
            i_end_point=i_t+2
            if i_first_point < 0 : i_first_point=0
            if i_end_point > len(board): i_end_point=i_t+1

            j_first_point=j_t-1
            j_end_point=j_t+2
            if j_first_point < 0 : j_first_point=0
            if j_end_point > len(board[0]): j_end_point=j_t+1

            for i_l in range (i_first_point,i_end_point):
                for j_l in range (j_first_point,j_end_point):
                    if board[i_l][j_l]=='*':
                        board[i_t][j_t]+=1

# Winner function
def winning(matrix,count):
    win=False
    min=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='?':
                min+=1
    if min == count: # comparing number of remained arraies and number of mines
        win=True
        PrintOut(board)
        print("Congratulation! You won!")
    return win

all_mines=0
end=False

PrintOut(board)
# Main loop of game

while not end :
    PrintOut(screen)
    x_input,y_input=input("Where is mine [X,Y]: ").split(",")
    x_in=ord(x_input.capitalize())-65
    y_in=int(y_input)-1

    if board[int(y_in)][int(x_in)]=='*' : 
        end=True 
        PrintOut(board)
        print("You lost") 
    elif board[int(y_in)][int(x_in)] != 0:
        screen[int(y_in)][int(x_in)] = board[int(y_in)][int(x_in)]
        end=winning(screen,mines)
    elif board[int(y_in)][int(x_in)] == 0:
            i_first_point=y_in-1
            i_end_point=y_in+2
            if i_first_point < 0 : i_first_point=0
            if i_end_point > len(board): i_end_point=y_in+1

            j_first_point=x_in-1
            j_end_point=x_in+2
            if j_first_point < 0 : j_first_point=0
            if j_end_point > len(board[0]): j_end_point=x_in+1

            for i_l in range (i_first_point,i_end_point):
                for j_l in range (j_first_point,j_end_point):
                    if board[i_l][j_l]==0:
                        screen[i_l][j_l]=0
            end=winning(screen,mines)

