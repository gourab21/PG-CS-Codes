#from printqueen import drawqueens
#from checksoln import check

def NQueens(k,n):
    for i in range(1,n+1):
        if (Place(k,i)):
            x[k]=i
            if k==n:
                print(x[1:n+1])
                p.append(x[1:n+1])
                
            else:
                NQueens(k+1,n)

def Place(k,i):
    for j in range(1,k):
        if x[j]==i or (abs(x[j]-i) == abs(j-k)) :
            return False
    return True
        

n=int(input("Enter The Number of Queens - "))
p=[]
x=[0]*(n+1)           
NQueens(1,n)
print(len(p))
#print(len(p))
#for i in p:
#    print(check(n,i))
    
