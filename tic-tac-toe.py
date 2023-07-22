def line():
    print("\n---------------------------------------------\n")

def line2(): print("+-----------------------------+")
    
def display(board: list) -> None:
    print("+---+---+---+")
    k=0
    for i in range(3):
        print('| ',end='')
        for j in range(3):
            print( board[k],end=' | ')
            k+=1
        print()
        print("+---+---+---+")


def check(l:list):
    for each_win in wins:
        flag=1
        for pos in each_win:
            if pos not in l:
                flag=0
        if flag==1:
            return 1
    return 0

def intro(choices:list) ->None:
    print("---------------------- TIC-TAC-TOE ----------------------")
    print("---------------------- INSTRUCTIONS----------------------")
    print("Enter corresponding number of the free box to place your piece(X/O)")
    display(choices)
    if(n%2==0):
        print("Player 1 plays X")
        print("Player 2 plays O")
    else:
        print("Player 2 plays X")
        print("Player 1 plays O")
    start=input("Press any key to start the game : ")
    print("Game starts now")


def accept(player:str,l:list,choices:list,board:list) -> None:
    print(f"Player {player}\'s turn : ")
    display(board)
    ch=0
    while ch not in choices:
        ch=int(input("Enter number(1-9) of a valid free square : "))
    l.append(ch)
    choices.remove(ch)
    board[ch-1]=player

def scoreboard() -> None :
    global p1_score,p2_score
    line2()
    print("|          SCORE              |")
    line2()
    print("|   PLAYER 1  |    PLAYER 2   |")
    line2()
    print(f"|      {p1_score}      |       {p2_score}       |")
    line2()

def play() -> str:
    board=[" " for i in range(9)]
    choices=[1,2,3,4,5,6,7,8,9]
    p1_list=[]
    p2_list=[]
    global p1_score,p2_score
    intro(choices)
    line()
    for i in range(0,9):
        if i%2==0:
            player='X'
            l=p1_list
        else:
            player='O'
            l=p2_list
        accept(player,l,choices,board)
        line()
        if(i<4):
            continue
        res=check(l)
        if(res==1):
            display(board)
            if n%2==0:
                if (player=='X') :
                    p1_score+=1 
                else:
                    p2_score+=1
            else:
                if (player=='X'):
                    p2_score+=1 
                else:
                    p1_score+=1
            return player
    return None

wins=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
n=0
p1_score=0
p2_score=0
wannaplay=1
while wannaplay==1:
    winner=play()
    if(winner):
        print(f"\nCONGRADULATIONS PLAYER {winner}!! YOU WON THE GAME!!")
    else:
        print("\n\nTHE GAME IS A DRAW!")
    line()
    scoreboard()
    line()
    wannaplay=int(input("Enter 1 to Play again : "))
    n+=1
print("Hope you enjoyed the game... Have a good day...")