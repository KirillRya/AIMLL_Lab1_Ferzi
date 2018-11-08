import copy
import time
start_time = time.time()


def setQueen(i,j,num_final,board):
    if board[i][j]==-1:
        for x in range(num):
            if board[x][j]==-1:
                board[x][j]=num_final
            if board[i][x]==-1:    
                board[i][x]=num_final
            diagLeft = x - i + j
            if diagLeft>=0 and diagLeft<num:
                if board[x][diagLeft]==-1:
                    board[x][diagLeft]=num_final
            diagRight = -x + i + j
            if diagRight>=0 and diagRight<num:
                if board[x][diagRight]==-1:
                    board[x][diagRight]=num_final
        board[i][j]=100  
        return True
    else:
        return False    


def printResult(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==100:
                print("0", end=' ')
            else: 
                print("*", end=' ') 
        print()


def solve(num_final,board):
    if num_final==num:
        return True
    for i in range(num_final,num_final+1):
        for j in range(num):
            if board[i][j]==-1:
                bd=copy.deepcopy(board)
                setQueen(i,j,num_final,bd)
                if solve(num_final+1,bd)==True:
                    if num_final==num-1:
                        printResult(bd)
                        print()
                    #return bd
                    return True
    return False      


def main():
    num_final = 0
    board=[]
    for i in range(num):
      board.append([])
      for j in range(num):
        board[i].append(-1)

    solve(num_final,board)
    print("--- %s seconds ---" % (time.time() - start_time))


num=8
main()    
