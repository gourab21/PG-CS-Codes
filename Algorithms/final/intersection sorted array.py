def f(arr1,arr2):
    a=[None]
    i=j=0
    k=-1
    while i<(len(arr1)) and j<(len(arr2)):
        if (arr1[i]==arr2[j]) and a[k]!=arr1[i] :
            if k==-1:
                k+=1
                a[k]=arr1[i]
            else:
                k+=1
                a.append(arr1[i])
            i=i+1
            j=j+1
        elif arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        
    if a[0]==None:
        return -1            
    else:
        return a

arr1=[10,33,61,61,75,100,120,150]
arr2=[40,46,47,120]

print(f(arr1,arr2))
