def MERGE_SORT(A,p,r):
    if p>=r:        #zero or one element array
        return;
    q=(p+r)//2      #mid point of A[p....r]
    MERGE_SORT(A,p,q)      #recursively sort A[p..q]
    MERGE_SORT(A,q+1,r)    #recursively sort A[q+1..r]
    #Merge A[p..q] and A[q+1...r] into A[p...r]
    MERGE(A,p,q,r)         

def MERGE(A,p,q,r):
    nL=q-p+1    #Length of A[p….q]
    nR=r-q      #Length of A[q+1….r]
    L=[0]*nL
    R=[0]*nR

    for i in range(nL):
        L[i]=A[p+i]     #copy A[p…q] to L[0….nL-1]
    for j in range(nR):
        R[j]=A[q+1+j]      #copy A[q+1…r] to L[0….nR-1]
    
    i = 0		#smallest element remaining in L
    j = 0		#smallest element remaining in R
    k = p		#indexes location in A to fill
    #  As long as there is an element unmerged in L or R, copy smallest element to A. 

    while i<nL and j<nR:
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
            k=k+1
        else:
            A[k]=R[j]
            j=j+1
            k=k+1
    # Having gone through one of L and R completely, copy remaining in A. 
    while i<nL:
        A[k]=L[i]
        i=i+1
        k=k+1
    while j<nR:
        A[k]=R[j]
        j=j+1
        k=k+1


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
        
        MERGE_SORT(A,0,len(A)-1)
        
        print("Sorted Array - ",A)
except Exception as e:
    print("Error Occured. ",e)
