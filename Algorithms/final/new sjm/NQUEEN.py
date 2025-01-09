
def addsoln(board,ans,n):
    temp=[]
    for i in range(n):
        for j in range(n):
            temp.append(board[i][j])
    print(temp)
    ans.append(temp)


def safe(row,col,board,n):
    x=row
    y=col
    while y>=0:
        if board[x][y]==1:
            return False
        y=y-1
    
    x=row
    y=col
    while x>=0 and y>=0:
        if board[x][y]==1:
            return False
        y=y-1
        x=x-1
    
    x=row
    y=col
    while x<n and y>=0:
        if board[x][y]==1:
            return False
        y=y-1
        x=x+1
    return True



def solve(col,ans,board,n):
    #base
    if col==n:
        addsoln(board,ans,n)
        return
    #solve one case
    for row in range(n):
        if safe(row,col,board,n):
            board[row][col]=1
            solve(col+1,ans,board,n)
            board[row][col]=0


def nqueen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    ans=[]
    
    solve(0,ans,board,n)
    return ans

print(nqueen(4))