import random

def makefileofmatrix():
    n=int(input("Enter order of Matrices - "))
    file=input("Enter name of file 1 - ")

    f = open(file+'.txt', 'w')
    a=[[0]*n]*n

    for i in range(n):
        for j in range(n):
            a[i][j]=int(input("Enter Element %i,%i - "%(i+1,j+1)))
            f.write(str(a[i][j])+" ")
        if i!=n-1 or j!=n-1:
            f.write("\n")
    f.close()          
                
def makefileofmatrixrandom():
    n=int(input("Enter order of Matrices - "))
    file=input("Enter name of file 1 - ")

    f = open(file+'.txt', 'w')
    a=[[0]*n]*n

    for i in range(n):
        for j in range(n):
            a[i][j]=random.randrange(-50,50)
            f.write(str(a[i][j])+" ")
        if i!=n-1 or j!=n-1:
            f.write("\n")
    f.close()          
             
makefileofmatrixrandom()        
