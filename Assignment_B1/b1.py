#solve.py

import json

def isattack(board,r,c):
    
    
    for i in range(r): #r is row value, [for i in range(1) will print, 0 ] 
        if(board[i][c]==1): #1)if board[0][0] or board[1][0] is 1 for i=0 2) [0][0],[1][0]==1,[2][0] 3)[0][1],[1][1],[2][1] 4)[0][2],[1][2],[2][2] 5)[0][0],[1][0]=1,[2][0],[3][0] 6)0 1,1 1,2 1,3 1
            return True
    
    i=r-1 #1)if not present i=1-1=0, j=0-1=-1 3)i=2-1=1,j=1-1=0 4) i=1,j=1 6)i=3-1=2,j=1-1=0
    j=c-1
    while((i>=0) and (j>=0)): #1)skipped 3)not skipped 4)not skipped 6)not skipped
        if(board[i][j]==1): #3)[1][0]==1 4)[1][1]!=1,[0][0]!=1 6)[2][0]!=1
            return True
        i=i-1 #4) i=0,j=0,i=-1,j=-1 6)i=1,j=-1
        j=j-1
    
    i=r-1 #1)i=1-1=0,j=0+1=1 4)i=2-1=1,j=2+1=3 6)i=2,j=2
    j=c+1
    while((i>=0) and (j<8)): #1)not skipped, 4)not skipped 6)not skipped
        if(board[i][j]==1): #1) if board[0][1] is 1  4)[1][3]!=1,[0][4]!=1 6)[2][2]=1
            return True
        i=i-1 #1)else i=0-1=-1,j=1+1=2, i!>=0,break 4)i=0j=4 ,i=-1 j=5 break
        j=j+1
    return False
    
def solve(board,row): #called from main with (board,1) so start with 1st row. queen already placed in 0th row
    i=0 		#represents column number for each new row

    
    while(i<8): #whenever there is false it will execute if loop
        if(not isattack(board, row, i)): #1)here i is column value. will look for isattack(board,1,0) first. 2)isattack(2,0)=true so i+=1 3)call for (board,2,1)=true 4)(board,2,2)=false 5)(board,3,0)=true 6)(board,3,1)
            board[row][i]=1 #1)place queen at 1,0 4)place queen at 2,2
            if(row==7): #1)skipped 4)skipped
                return True
            else:
                if(solve(board, row+1)): #1)call for(board,2) for which 2nd pass will be generated 4)call (board,3) 5th pass  ###this will return false on 7th row if not possible to place queen
                    return True
                else:
                    board[row][i]=0 ###so previous (6th row)placed queen is removed and i is incremented to find the place for queen in next position!!! if cannot place in 6th row either, it will return false at this very step and this is how backtracking works here
        i=i+1
    
    if(i==8):
        return False ###this is where false is returned for every unplacable queen
    
def printboard(board):
    for i in range(8):
        for j in range(8):
            print str(board[i][j])+"  ",
        print "\n"
        
board = [[0 for x in range(8)] for x in range(8)] #initialize board

if __name__ == '__main__':
    data=[] 

    with open('input.json') as f: #take input
        data=json.load(f) #put that input into data
    
    if(data["start"]<0 or data["start"]>7): #input should be between 0 to 7 
        print "Invalid JSON input"
        exit()
    
    board[0][data["start"]]=1 #put 1st queen on board[0][start position] assume queen placed at 0,5
    if(solve(board, 1)):
        print "Queens problem solved!!!"
        print "Board Configuration:"
        printboard(board)
    else:
        print "Queens problem not solved!!!"

#input.json
#{"start":2}
