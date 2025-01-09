#n=8
#r=[1, 2, 3, 4, 5, 6, 7, 8]
#a=[2, 6, 1, 7, 4, 8, 5, 3]
#x=[]

def check(n,a):
    x=[]
    for k in range(n):
        e=a[k]
        if e in x:
            print("Same Column.")
            return False
        x.append(e)
        i=k
        j=a[k]-1
        while j<(n-1) and i<(n-1): #i=6 j=1
            if a[j+1]==j+2:
                print(a[k])
                print("Diagonal")
                return False
            i=i+1
            j=j+1

        i=k
        j=a[k]-1
        while j>0 and i<(n-1): 
            #print(k)
            if a[i+1]==j:
                #print(a[k])
                print("Diagonal")
                return False
            i=i+1
            j=j-1

    
    
    print("True")
    return True
    


    
#check(n,a)
