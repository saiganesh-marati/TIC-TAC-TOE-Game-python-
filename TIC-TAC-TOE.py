#!/usr/bin/env python
# coding: utf-8

# In[ ]:


board=[['','',''],['','',''],['','','']]
def printboard(board):
    print(*board[0],sep=" | ")
    print("---------")
    print(*board[1],sep=" | ")
    print("---------")
    print(*board[2],sep=" | ")
    


def get_markers():
    p1=input("Player 1 choice (X or O):").upper()
    p2=""
    if(p1=='X'):
        p2='O'
        return ['X','O']
    elif(p1=='O'):
        p2='X'
        return ['O','X']
    else:
        print("Invalid Input")
        return get_markers() 

def get_coordinates(board):
    x,y=list(map(int,input("enter the cordinates with space:").split()))
    if x in [0,1,2] and y in [0,1,2] and board[x][y]=='':
        return [x,y]
    else:
        print("Invalid input")
        return get_coordinates(board)

def check_for_win(board):
    #check row wise
    for i in range(len(board)):
        if ((board[i][0]==board[i][1]==board[i][2]=="X" )or( board[i][0]==board[i][1]==board[i][2]=="O")):
                return True
    #check column wise
    for j in range(len(board)):
        if((board[0][j]==board[1][j]==board[2][j]=="X" )or( board[0][j]==board[1][j]==board[2][j]=="O")):
            return True
        #check diagonal
    if((board[0][0]==board[1][1]==board[2][2]=="X" )or( board[0][0]==board[1][1]==board[2][2]=="O")):
        return True
    else:
         return False

def update_board(board,chance,marker,x,y):
    if(chance ==True):
        board[x][y]=marker
        if check_for_win(board):
            print("player 1 wins")
            return "game over"
        return False
    else:
        board[x][y]=marker
        if check_for_win(board):
            print("player 2 wins")
            return "game over"
        return True
    
def play_game():
    player1=0
    player2=0
    m1,m2=get_markers()
    print(f"player1:{m1},player2:{m2}")
    chance=True
    l=0
    while True:
        printboard(board)
        #x,y =get_coordinates(board)
        if chance:
            print("player 1 choice:")
            x,y =get_coordinates(board)
            chance=update_board(board,chance,m1,x,y)
            l+=1
            if chance=="game over":
                print("Game over")
                break
            if l==9:
                print("Draw Match")
                print("game over")
                break
        
        else:
            print("player2 choice:")
            x,y =get_coordinates(board)
            chance=update_board(board,chance,m2,x,y)
            l+=1
            if chance=="game over":
                print("Game over")
                break
            
            if l==9:
                print("Draw Match")
                print("game over")
                break

play_game()


# In[ ]:





# In[ ]:




