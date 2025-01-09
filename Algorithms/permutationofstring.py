
x=[]
def permute(a, l, r): 
    if l == r: 
        c=(''.join(a))
        if c not in x:
            x.append(c)
    else: 
        for i in range(l, r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] # backtrack 


 
string = "AABCD"
n = len(string) 
a = list(string) 

permute(a, 0, n)
print(len(x))
for i in x:
    print(i)

