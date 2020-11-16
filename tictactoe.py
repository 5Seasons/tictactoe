import numpy as np
from numpy.core.defchararray import isnumeric

gameboard = np.zeros((3,3),dtype='int')
turn_num = 0

def checkWin():
    # 竖 或者 横
    if(3 in gameboard.sum(0) or 3 in gameboard.sum(1)):
        return 1
    if(-3 in gameboard.sum(0) or -3 in gameboard.sum(1)):
        return -1
    # 斜线
    if((gameboard[0,0] + gameboard[1,1] + gameboard[2,2] == 3) or (gameboard[0,2] + gameboard[1,1] + gameboard[2,0] == 3)):
        return 1
    if((gameboard[0,0] + gameboard[1,1] + gameboard[2,2] == -3) or (gameboard[0,2] + gameboard[1,1] + gameboard[2,0] == -3)):
        return -1
    else :
        return 0

def showResults():
    valueMap = {-1:'O',    0:' ',    1:'X'}
    print('-------')
    for a in gameboard:
        print('|',end='')
        for b in a:
            print(valueMap.get(b), end='|')
        print()
    print()

if __name__ == "__main__":
    while (checkWin() == 0):
        pos_x,pos_y = input("Please enter two numbers to put your mark, use ',' to split").split(',')
        # Check the input is valid
        while(not pos_x.isnumeric() or not pos_y.isnumeric() or int(pos_x) < 1 or int(pos_y) < 1 or int(pos_x) > 3 or int(pos_y) > 3 or not gameboard[int(pos_x) - 1,int(pos_y)-1] == 0):
            # If input is not number
            if(not pos_x.isnumeric() or not pos_y.isnumeric):
                pos_x,pos_y = input("Please enter valid numbers to put your mark, use ',' to split").split(',')
            # If input is out of range
            if(int(pos_x) < 1 or int(pos_y) < 1 or int(pos_x) > 3 or int(pos_y) > 3):
                pos_x,pos_y = input("Please enter numbers between 0-3 to put your mark, use ',' to split").split(',')
            # If the place is taken.
            if(not gameboard[int(pos_x) - 1,int(pos_y)-1] == 0):
                pos_x,pos_y = input("The place is take, please re-enter, use ',' to split").split(',')
        pos_x,pos_y = int(pos_x),int(pos_y)
        if(turn_num%2 == 0):
            gameboard[pos_x-1,pos_y-1] = 1
        else:
            gameboard[pos_x-1,pos_y-1] = -1
        turn_num = turn_num + 1
        showResults()
        
    if(checkWin() == 1):
        print("The first player win.")
    
    if(checkWin() == -1):
        print("The second player win.")