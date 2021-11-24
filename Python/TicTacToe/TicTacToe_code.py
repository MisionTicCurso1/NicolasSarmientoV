from collections import deque
import random

turn=deque(['O','X'])

board=[
    ['','',''],
    ['','',''],
    ['','','']
]

menu_board=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def showboard():
    for i in range(3):
        print(board[i])

def play():
    
    if position==1:
        if board[0][0]=='':
         board[0][0]=player
        else:
            turn.rotate()
    elif position==2:
        if board[0][1]=='':
            board[0][1]=player
        else:
            turn.rotate()
    elif position==3:
        if board[0][2]=='':
            board[0][2]=player
        else:
            turn.rotate()
    elif position==4:
        if board[1][0]=='':
            board[1][0]=player
        else:
            turn.rotate()
    elif position==5:
        if board[1][1]=='':
            board[1][1]=player
        else:
            turn.rotate()
    elif position==6:
        if board[1][2]=='':
            board[1][2]=player
        else:
            turn.rotate()
    elif position==7:
        if board[2][0]=='':
            board[2][0]=player
        else:
            turn.rotate()
    elif position==8:
        if board[2][1]=='':
            board[2][1]=player
        else:
            turn.rotate()
    elif position==9:
        if board[2][2]=='':
            board[2][2]=player
        else:
            turn.rotate()
    else:
        pass 

def winner(p):
    if ((board[0]==[p,p,p]) or (board[1]==[p,p,p]) or (board[2]==[p,p,p])
        or (board[0][0]==p and board[1][0]==p and board[2][0]==p) or
        (board[0][1]==p and board[1][1]==p and board[2][1]==p) or 
        (board[0][2]==p and board[1][2]==p and board[2][2]==p) or
        (board[0][0]==p and board[1][1]==p and board[2][2]==p) or
        (board[0][2]==p and board[1][1]==p and board[2][0]))  :
        
        return p
    
    
def tie():
    blank=0
    for i in board:
        for item in range(3):
            if i[item]!='':
                blank+=1
    
    if blank==9:
        return True
    else:
        return False

print('Para jugar... usa el siguiente menu')
for i in range(3):
        print(menu_board[i])
print("0 para salir...")
while True:
    turn.rotate()
    player= turn[0]
    print(f'Turno: {player}')
    position=int(input('Elija posicion: '))

    if position!=0:
        play()
    else:
        break

    if winner(player):
        showboard()
        print(f"El ganador es: {player}")
        replay=int(input("desea volver a jugar 1:si, 0: No "))
        if replay==1:
           for i in board:
               for item in range(3):
                   i[item]=''
        start_player=random.randint(0,1)
        if start_player==1:
            turn.rotate()
        else:
            break
    else:
        showboard()
        if tie():
            print('Empate: ')

            replay=int(input("desea volver a jugar 1:si, 0: No"))
            if replay==1:
                for i in board:
                    for item in range(3):
                        i[item]=''
                start_player=random.randint(0,1)
                if start_player==1:
                    turn.rotate()
            else:
                break



