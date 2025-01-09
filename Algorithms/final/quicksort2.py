def partition(arr, low, high):
    """
    Partition the array around the pivot.
    Elements smaller than the pivot go to its left,
    and elements greater than the pivot go to its right.
    """
    pivot = arr[low]  # Choosing the first element as pivot
    i = low  # Index for placing smaller elements

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements smaller than pivot

    # Place the pivot in its correct position
    arr[low], arr[i] = arr[i], arr[low]
    return i  # Return the pivot index


def quick_sort(arr, low, high):
    """
    The main Quick Sort function that recursively sorts the array.
    """
    if low < high:
        pivot_index = partition(arr, low, high)  # Partition the array
        quick_sort(arr, low, pivot_index - 1)   # Sort left subarray
        quick_sort(arr, pivot_index + 1, high)  # Sort right subarray

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
        
        quick_sort(A,0,len(A)-1)
        
        print("Sorted Array - ",A)
except Exception as e:
    print("Error Occured. ",e)