from mergesort import *

def fracknapsack(p,w,W):
    x=[0]*(len(w)) #x is to store fractional weight of elements selected.
    pro=[0]*len(w) #to store fractional profits.
    profit = 0 #Total Profit Made
    weight = 0 #Weight filled in knapsack
    
    for i in range(len(w)):
        if weight+w[i]<W: #All of element 'i' can be put.
            x[i]=w[i]
            pro[i]=p[i]
            profit+=p[i]
            weight+=w[i]
        else: #fraction of the total available weight of 'i' can be put.
            x[i]=(W-weight) #capacity remaining 
            weight+=x[i] 
            ppp=(p[i]/w[i])*x[i] #calculating profit of the fraction added
            pro[i]=ppp
            profit+=ppp

    return profit,x,pro
            
def copyfiletomatrix(filename):
    """This fucntion creates an Matrix out of the file given.
    	Input - Filename
        Output - Matrix from the elements as entered. """
    try:
        w=[]
        file=open(filename, "r")
        data = file.readlines()
        word = data[0].split()
        for i in word:
            w.append(int(i))
       
        return w
    
    except Exception as e:
        print("Error Occured. ",e)
        return 0            


#W=13
#w=[10, 30, 20, 50]
w=[float(i) for i in input("Enter Weight of elements - ").split()]
#p=[40, 30, 80, 70]
p=[float(i) for i in input("Enter Profit of elements - ").split()]
W=float(input("Enter Total Capacity of Knapsack - "))
pw=[0]*(len(w))
index=[0]*(len(w))
for i in range(len(w)):
    pw[i]=p[i]/w[i]
    index[i]=i+1

print("Element Number     - ",index)
print("Profit of Elements - ",p)
print("Weight of Elements - ",w)
print("-"*65)
(pw,w,p,index)=MERGE_SORT_MODIFY(pw,0,len(pw)-1,w,p,index)

try:
    if len(w)>len(p):
        print("Profit of some items are missing.")
    elif len(w)<len(p):
        print("Weight of some items are missing.")
        
    else:
        
        result=(fracknapsack(p,w,W))
        print("Maximum Profit Generated - ",result[0])
        for i in range(len(index)):
            if result[1][i]!=0:
                print("Element No. %i is taken with weight =  %f  with profit = %f."%(index[i],result[1][i],result[2][i]))
        
except Exception as e:
        print("Error Occured. ",e)
