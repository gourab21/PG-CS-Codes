def MERGE_SORT_MODIFY(A,p,r,W,P,I):
    if p>=r:        #zero or one element array
        return;
    q=(p+r)//2      #mid point of A[p....r]
    MERGE_SORT_MODIFY(A,p,q,W,P,I)      #recursively sort A[p..q]
    MERGE_SORT_MODIFY(A,q+1,r,W,P,I)    #recursively sort A[q+1..r]
    #Merge A[p..q] and A[q+1...r] into A[p...r]
    MERGE(A,p,q,r,W,P,I)
    return A,W,P,I

def MERGE(A,p,q,r,W,P,I):
    nL=q-p+1    #Length of A[p….q]
    nR=r-q      #Length of A[q+1….r]
    L=[0]*nL
    R=[0]*nR
    LW=[0]*nL
    RW=[0]*nR
    LP=[0]*nL
    RP=[0]*nR
    LI=[0]*nL
    RI=[0]*nR
    
    for i in range(nL):
        L[i]=A[p+i]     #copy A[p…q] to L[0….nL-1]
        LW[i]=W[p+i]
        LP[i]=P[p+i]
        LI[i]=I[p+i]
    for j in range(nR):
        R[j]=A[q+1+j]      #copy A[q+1…r] to L[0….nR-1]
        RW[j]=W[q+1+j]
        RP[j]=P[q+1+j]
        RI[j]=I[q+1+j]
    
    i = 0		#smallest element remaining in L
    j = 0		#smallest element remaining in R
    k = p		#indexes location in A to fill
    #  As long as there is an element unmerged in L or R, copy smallest element to A. 

    while i<nL and j<nR:
        if L[i]>=R[j]:
            A[k]=L[i]
            W[k]=LW[i]
            P[k]=LP[i]
            I[k]=LI[i]
            i=i+1
            k=k+1
        else:
            A[k]=R[j]
            W[k]=RW[j]
            P[k]=RP[j]
            I[k]=RI[j]
            j=j+1
            k=k+1
    # Having gone through one of L and R completely, copy remaining in A. 
    
    while i<nL:
        A[k]=L[i]
        W[k]=LW[i]
        P[k]=LP[i]
        I[k]=LI[i]
        i=i+1
        k=k+1

    while j<nR:
        A[k]=R[j]
        W[k]=RW[j]
        P[k]=RP[j]
        I[k]=RI[j]
        j=j+1
        k=k+1
    



