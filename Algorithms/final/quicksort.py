def QUICKSORT(A,p,r):
    if p<r:
        # q is the index returned by partition function
        q=PARTITION(A,p,r)
        QUICKSORT(A,p,q-1) # for sorting A[p...q-1]
        QUICKSORT(A,q+1,r) # for sorting A[q+1...r]

def PARTITION(A,p,r):
    pivot=A[r] # chosing pivot element
    i=p-1
    # traverse A[p..r] and move all smaller elements on left side.
    # elements from p to i are smaller after every iteration
    
    for j in range(p,r):
        if A[j]<=pivot:
            i=i+1
            A[i],A[j]=A[j],A[i]
    
    # place the pivot element after smaller elements and return its` index
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

#Main 
A=[]
try:
    n=int(input("Enter Number of ELements - "))
    if (n<1):
        print("Number of Elements can`t be less than 1")
    else:
        # Taking Array Elements from user    
        for i in range(n):
            A.append(float(input("Enter Element -  ")))
        
        print("Input Array  - ",A)
        
        QUICKSORT(A,0,len(A)-1)
        
        print("Sorted Array - ",A)
except Exception as e:
    print("Error Occured. ",e)
