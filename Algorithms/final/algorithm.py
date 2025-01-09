base=['quicksort1','quicksort2', 'mergesort', 'strassen', 'mcm', 'fractionalknapsack', 'zerooneknapsack', 'nqueen', 'bfs', 'dfs', 'kruskals', 'prims', 'floyd', 'dijkstra', 'bellmanford']

def leba():
    l='''
import algorithm as gd #filename
s=gd.code_name #code_name
question='q1.py'  #to be saved at location
l=int(input("Line No. "))  #line number to start
n=0
e=0
while True:       
    if s[n]=='\n':
        e+=1

    if e>=l-1:    
        a=open(question,'a+') #
        a.write(s[n])
        sw=input()
        a.close()
    n+=1
    '''
    for i in l:
        print(i,end='')


quicksort2='''
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

'''

quicksort1="""
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
"""


mergesort="""
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
    
    i = 0       #smallest element remaining in L
    j = 0       #smallest element remaining in R
    k = p       #indexes location in A to fill
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

"""

strassen='''
import math
import numpy as np
from datetime import datetime

def split(matrix):
	"""
	Splits a given matrix into quarters.
	Input: nxn matrix
	Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
	"""
	row, col = matrix.shape #returns row and column size of a matrix
	row2, col2 = row//2, col//2
	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(x, y):
	"""
	Computes matrix product by divide and conquer approach, recursively.
	Input: nxn matrices x and y
	Output: nxn matrix, product of x and y
	"""

	# Base case when size of matrices is 1x1
	if len(x) == 1:
		return x * y
	n=len(x)
	# Splitting the matrices into quadrants. This will be done recursively
	# until the base case is reached.
	a, b, c, d = split(x)
	e, f, g, h = split(y)
	n=n//2
	# Computing the 7 products, recursively (p1, p2...p7)
	p1 = strassen(a, f - h) 
	p2 = strassen(a + b, h)	 
	p3 = strassen(c + d, e)	 
	p4 = strassen(d, g - e)	 
	p5 = strassen(a + d, e + h)	 
	p6 = strassen(b - d, g + h) 
	p7 = strassen(a - c, e + f) 

	# Computing the values of the 4 quadrants of the final matrix c
	if n==1:
		r=np.matrix([0],)
	else:
		r=np.matrix([[0]*n]*n,)
	c11 = p5 + p4 - p2 + p6 
	c12 = p1 + p2		 
	c21 = p3 + p4		 
	c22 = p1 + p5 - p3 - p7
	 
	

	# Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
    # vstack and hstack are used to join matrices.
	return c

def copyfiletomatrix(filename):
    """This fucntion creates an Matrix out of the file given.
    	Input - Filename
        Output - Matrix from the elements as entered. """
    try:
        w=[]
        with open(filename, "r") as file:
            data = file.readlines()
            for line in data:
                t=[]
                word = line.split()
                for i in word:
                    t.append(int(i))
                w.append(t)
        
        return np.matrix(w,)
    except Exception as e:
        print("Error Occured. ",e)
        return 0

a=copyfiletomatrix("strassennormalmatrix1.txt")
b=copyfiletomatrix("strassennormalmatrix2.txt")
try:
        x=len(a) 
        p=math.log(x)/math.log(2)
        if p.is_integer(): #checking if the matrices are order of power of 2.
                #print("Multiplication of the Matrices results in - ")

                start = datetime.now() 
                 
                x=(strassen(a,b)) # x stores the product of the matrices

                end = datetime.now()
                difference = end - start 
                seconds = difference.total_seconds()
                print(seconds)
                #now we write the output in file and also print it
                x=np.array(x).tolist()
                f = open('resultmatrixstrassennormal.txt', 'w')
                for i in x:
                        for j in i:
                                p=str(j)
                                f.write(p+" ")
                                #print(p,end="  ")
                        f.write("\n")
                        #print()
                f.close()
                print("DOne Computing")
                input()
        else:
                print("Matrices are not in order of - 2 ^ n.")

except Exception as e:
        print("Error Occured. ",e)

       
-23 13 42 45
15 -17 -6 10
-4 -13 -23 15
4 5 9 33       

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1

-23 13 42 45 
15 -17 -6 10 
-4 -13 -23 15 
4 5 9 33 
        
'''


mcm='''
def matrix_chain_order(dimensions):
    """
    Computes the optimal parenthesization of a matrix chain product
    and the minimum number of scalar multiplications needed.

    Parameters:
    dimensions (list): List of dimensions of matrices such that
                       the ith matrix has dimensions dimensions[i-1] x dimensions[i].

    Returns:
    tuple: A tuple containing the following:
           - Minimum number of scalar multiplications.
           - Table of costs (m).
           - Table for optimal splits (s).
    """
    n = len(dimensions) - 1  # Number of matrices
    # m[i][j] will store the minimum number of scalar multiplications for A_i..A_j
    m = [[0] * n for _ in range(n)]
    # s[i][j] will store the index k at which the optimal split occurs
    s = [[0] * n for _ in range(n)]

    # L is chain length
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')  # Initialize with infinity
            for k in range(i, j):
                # Compute cost
                q = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[0][n - 1], m, s


def print_optimal_parenthesization(s, i, j):
    """
    Prints the optimal parenthesization of matrices.

    Parameters:
    s (list): The table for optimal splits.
    i (int): Starting index.
    j (int): Ending index.
    """
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")


# Example usage
if __name__ == "__main__":
    print("""Input: The dimensions list specifies the dimensions of the matrices. For instance, if dimensions = [30, 35, 15], the matrices are:
    A1 : 30 x 35
    A2 : 35 x 15
    """)
    dimensions = [int(i) for i in input("Enter the space separated dimensions matrix - ").split()]
    min_cost, m, s = matrix_chain_order(dimensions)
    print(f"Minimum number of multiplications: {min_cost}")
    print("Optimal parenthesization: ", end="")
    print_optimal_parenthesization(s, 0, len(dimensions) - 2)
    print()


'''


fractionalknapsack='''
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

'''


zerooneknapsack='''
def knapsack_01(weights, profit, capacity):
    """
    Solves the 0/1 Knapsack Problem using dynamic programming.
    Parameters:
    weights (list): List of item weights.
    profit (list): List of item profit.
    capacity (int): Maximum weight capacity of the knapsack.
    Returns:
    tuple: A tuple containing:
           - Maximum value that can be achieved.
           - List of items included in the knapsack.
    """
    n = len(profit)  # Number of items
    # dp[i][w] will store the maximum value for the first i items with weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + profit[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items included
    w = capacity
    included_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)  # Include the item (indexing starts from 0)
            w -= weights[i - 1]

    return dp[n][capacity], included_items

# Example usage
if __name__ == "__main__":
    #profit = [60, 100, 120]  # profit of items
    #weights = [10, 20, 30]  # Weights of items
    #capacity = 25  # Capacity of knapsack

    profit=[int(i) for i in input("Enter Profit of elements - ").split()]
    weights=[int(i) for i in input("Enter Weight of elements - ").split()]
    capacity=int(input("Enter Total Capacity of Knapsack - "))

    max_value, included_items = knapsack_01(weights, profit, capacity)
    print(f"Maximum Profit: {max_value}")
    included_items=[i+1 for i in included_items]
    print("Items included - ")
    for i in included_items:
        print("Item No. ",i," weight = ",weights[i])
        
'''

nqueen='''
def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()


def is_safe(board, row, col, n):
    # Check the column
    i = 0
    while i < row:
        if board[i][col]:
            return False
        i += 1

    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True



def solve_n_queens_util(board, row, n, solutions):
    # If all queens are placed, add the solution to the list
    if row == n:
        solutions.append([row[:] for row in board])
        return

    # Try placing a queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            solve_n_queens_util(board, row + 1, n, solutions)  # Recurse
            board[row][col] = 0  # Backtrack


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]  # Initialize the chessboard
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)  # Solve the problem
    return solutions


# Example usage
n = int(input("Enter number of Queens - ")) 
solutions = solve_n_queens(n)

print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
for index, solution in enumerate(solutions, start=1):
    print(f"Solution {index}:")
    print_solution(solution)

'''


bfs='''
def bfs(graph,start_vertex):
        
    # Initialize BFS structures
    visited = set()  # To track visited vertices
    queue = [start_vertex]  # Regular list for the queue
    bfs_order = []  # To store the BFS traversal order

    # Perform BFS
    while queue:
        current = queue.pop(0)  # Dequeue the first element
        if current not in visited:
            visited.add(current)  # Mark it as visited
            bfs_order.append(current)  # Add to BFS order

            # Enqueue all unvisited neighbors
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order


# Input the graph details

graph = {}

lol=int(input("1. Directed   2. Undirected Graph. - "))
n = int(input("Enter the number of edges - "))
print("Enter Edges as vertex 1, vertex 2 ")
for i in range(n):
    x = input(f"Enter edge {i + 1} - ").split()
    i,j=x[0],x[1]
    if i not in graph:
        graph[i]=[]
    if j not in graph:
        graph[j]=[]
    graph[i].append(j)
    if lol==2:
        graph[j].append(i)
    

# Input starting vertex for BFS
start_vertex = input("Enter the starting vertex for BFS - ")

# Perform BFS and output the traversal order
bfs_result = bfs(graph, start_vertex)
print("BFS Traversal Order:", bfs_result)

'''

dfs='''
def dfs(graph,vertex):
    visited = set()
    dfs_order = []
    dfs_recursive(graph, vertex, visited, dfs_order)
    return dfs_order

def dfs_recursive(graph, vertex, visited, dfs_order):
    # Initialize visited set and DFS order list
    
    visited.add(vertex)  # Mark the current vertex as visited
    dfs_order.append(vertex)  # Add the vertex to the DFS order

    # Recur for all neighbors of the current vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, dfs_order)
    

# Input the graph details
graph = {}

lol=int(input("1. Directed   2. Undirected Graph. - "))
n = int(input("Enter the number of edges - "))
print("Enter Edges as vertex 1, vertex 2 ")
for i in range(n):
    x = input(f"Enter edge {i + 1} - ").split()
    i,j=x[0],x[1]
    if i not in graph:
        graph[i]=[]
    if j not in graph:
        graph[j]=[]
    graph[i].append(j)
    if lol==2:
        graph[j].append(i) #undirected graph
    

# Input the starting vertex for DFS
start_vertex = input("Enter the starting vertex for DFS - ")

#global Variables.


# Perform DFS
dfs_order=dfs(graph, start_vertex)

# Output the DFS traversal order
print("DFS Traversal Order:", dfs_order)

'''

kruskals='''
class DisjointSet:
    """
    Implements the Disjoint Set Union (DSU) data structure
    for Kruskal's Algorithm with path compression and union by rank.
    """
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}  # Each vertex points to itself
        self.rank = {v: 0 for v in vertices}    # Initial rank is 0 for all vertices

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    """
    Implements Kruskal's Algorithm to find the MST of a graph.
    Parameters:
    vertices (list): List of vertices in the graph.
    edges (list): List of edges, where each edge is represented as
                  (weight, u, v).
    Returns:
    tuple: A tuple containing:
           - The total weight of the MST.
           - The list of edges in the MST.
    """
    # Sort edges by weight
    edges.sort()

    dsu = DisjointSet(vertices)
    mst = []
    mst_weight = 0

    for weight, u, v in edges:
        # If u and v are in different components, include this edge in the MST
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst_weight, mst

# Example usage
if __name__ == "__main__":
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edges = [(1, 'g', 'h'),
            (2, 'c', 'i'),
            (2, 'f', 'g'),
            (4, 'a', 'b'),
            (4, 'c', 'f'),
            (6, 'g', 'i'),
            (7, 'c', 'd'),
            (7, 'h', 'i'),
            (8, 'a', 'h'),
            (8, 'b', 'c'),
            (9, 'd', 'e'),
            (10, 'e', 'f'),
            (11, 'b', 'h'),
             (14,'d','f')
            
    ]
    edges=[]
    vertices=[i for i in input("Enter the vertices - ").split()]
    n=int(input("Enter the number of edges - "))
    print("Enter Edges as weight, vertex 1, vertex 2 ")
    for i in range(n):
        x=input("Enter edge %i - "%(i+1)).split()
        edges.append([int(x[0]),x[1],x[2]])

    mst_weight, mst = kruskal(vertices, edges)
    print(f"Total weight of MST: {mst_weight}")
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"({u}, {v}) with weight {weight}")

'''

prims='''
import heapq

def prims_algorithm(vertices, edges):
    """
    Implements Prim's Algorithm to find the MST of a graph using a min-heap.
    
    Parameters:
    vertices (list): List of vertices in the graph.
    edges (list): List of edges, where each edge is represented as
                  (weight, u, v).
    
    Returns:
    tuple: A tuple containing:
           - The total weight of the MST.
           - The list of edges in the MST.
    """
    # Build the adjacency list
    graph = {v: [] for v in vertices}
    for weight, u, v in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    # Initialize structures
    visited = set()
    mst = []
    mst_weight = 0

    # Min-heap to pick the smallest edge
    min_heap = [(0, vertices[0], None)]  # (weight, current_vertex, parent)

    while min_heap and len(visited) < len(vertices):
        weight, current, parent = heapq.heappop(min_heap)  # Extract the minimum edge

        if current in visited:
            continue

        visited.add(current)

        # If the edge is part of the MST, add it
        if parent is not None:
            mst.append((parent, current, weight))
            mst_weight += weight

        # Add all edges from the current vertex to the min-heap
        for edge_weight, neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst_weight, mst


# Example usage
if __name__ == "__main__":
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edges = [(1, 'g', 'h'),
             (2, 'c', 'i'),
             (2, 'f', 'g'),
             (4, 'a', 'b'),
             (4, 'c', 'f'),
             (6, 'g', 'i'),
             (7, 'c', 'd'),
             (7, 'h', 'i'),
             (8, 'a', 'h'),
             (8, 'b', 'c'),
             (9, 'd', 'e'),
             (10, 'e', 'f'),
             (11, 'b', 'h'),
             (14, 'd', 'f')
    ]
    edges = []
    vertices = [i for i in input("Enter the vertices - ").split()]
    n = int(input("Enter the number of edges - "))
    print("Enter Edges as weight, vertex 1, vertex 2 ")
    for i in range(n):
        x = input(f"Enter edge {i + 1} - ").split()
        edges.append([int(x[0]), x[1], x[2]])
        
    mst_weight, mst = prims_algorithm(vertices, edges)
    print(f"Total weight of MST: {mst_weight}")
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"({u}, {v}) with weight {weight}")

'''

floyd='''
def floyd_warshall_with_input(vertices, edges):
    """
    Implements the Floyd-Warshall algorithm using edge-based input.
    
    Parameters:
    vertices (set): Set of vertices in the graph.
    edges (list): List of edges where each edge is represented as (source, destination, weight).
    
    Returns:
    dict: Dictionary of shortest distances between all pairs of vertices.
          If a negative weight cycle exists, returns None.
    """
    # Initialize the distance dictionary
    INF = float('inf')
    dist = {u: {v: INF for v in vertices} for u in vertices}
    
    # Distance to self is 0
    for v in vertices:
        dist[v][v] = 0
    
    # Initialize distances based on edges
    for u, v, weight in edges:
        dist[u][v] = weight

    # Apply Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Check for negative weight cycles
    for v in vertices:
        if dist[v][v] < 0:
            print("Graph contains a negative weight cycle")
            return None

    return dist


# Input the graph details using edges
edges = []
vertices = set()
n = int(input("Enter the number of edges: "))
print("Enter Edges as source, destination, weight")
for i in range(n):
    edge_input = input(f"Enter edge {i + 1}: ").split()
    source, destination, weight = edge_input[0], edge_input[1], int(edge_input[2])
    edges.append((source, destination, weight))
    vertices.add(source)
    vertices.add(destination)

# Running Floyd-Warshall algorithm on the graph
shortest_paths = floyd_warshall_with_input(vertices, edges)

# Output the result
if shortest_paths:
    print("Shortest path distances between all pairs of vertices:")
    for u in vertices:
        for v in vertices:
            if shortest_paths[u][v] == float('inf'):
                print(f"Distance from {u} to {v}: INF")
            else:
                print(f"Distance from {u} to {v}: {shortest_paths[u][v]}")

'''

dijkstra='''
import heapq

def add_edge(graph, weight, source, destination):
    # Adds an edge to the graph with characters as nodes
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append((destination, weight))

def dijkstra(graph, source):
    # Step 1: Initialize distances and priority queue
    dist = {node: float('inf') for node in graph}  # Distance to all nodes is infinity
    dist[source] = 0  # Distance to source node is 0
    priority_queue = [(0, source)]  # Min-heap (distance, node)

    while priority_queue:
        # Step 2: Extract the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Step 3: Skip if we've already found a shorter path to this node
        if current_distance > dist[current_node]:
            continue

        # Step 4: Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Step 5: Relaxation - Update distance if a shorter path is found
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Add neighbor to queue with updated distance

    return dist  # Return the shortest distances from source

# Example of adding edges using add_edge function with characters
graph = {}

# Add edges to the graph: add_edge(weight, source, destination)
add_edge(graph, 1, 'A', 'B')
add_edge(graph, 4, 'A', 'C')
add_edge(graph, 2, 'B', 'C')
add_edge(graph, 5, 'B', 'D')
add_edge(graph, 1, 'C', 'D')
example=[(10, 's', 't'),
    (5, 's', 'y'),
    (1, 't', 'x'),
    (2,'t','y'),
    (9, 'y', 'x'),
    (3, 'y', 't'),
    (2, 'y', 'z'),
    (6, 'z', 'x'),
    (4,'x','z'),
    (7, 'z', 's')]

graph = {}
n = int(input("Enter the number of edges - "))
print("Enter Edges as weight, source, destination ")
for i in range(n):
    x = input(f"Enter edge {i + 1} - ").split()
    add_edge(graph,int(x[0]), x[1], x[2])

# Running Dijkstra's algorithm on the graph starting from node.
source = input("Enter Starting Node - ")
shortest_paths = dijkstra(graph, source)

print("Shortest distances from node", source, ":")
for node in shortest_paths:
    print(f"Node {node}: {shortest_paths[node]}")

'''


bellmanford='''
def bellman_ford(edges, vertices, source):
    # Initialize distances to all vertices as infinity
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0  # Distance to the source is 0

    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Check for negative weight cycles
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            print("Graph contains a negative weight cycle")
            return None

    return dist


# Input the graph details using edges
edges = []
vertices = set()
n = int(input("Enter the number of edges: "))
print("Enter Edges as source, destination, weight")
for i in range(n):
    edge_input = input(f"Enter edge {i + 1}: ").split()
    source, destination, weight = edge_input[0], edge_input[1], int(edge_input[2])
    edges.append((source, destination, weight))
    vertices.add(source)
    vertices.add(destination)

# Running Bellman-Ford algorithm on the graph starting from a given source node
source = input("Enter Starting Node: ")
shortest_paths = bellman_ford(edges, vertices, source)

# Output the result
if shortest_paths:
    print("Shortest distances from node", source, ":")
    for node in shortest_paths:
        print(f"Node {node}: {shortest_paths[node]}")

'''



'''
# Safely iterate over global variables
print("Global Variables:")
a=[]
for name, value in list(globals().items()):  # Make a copy using list()
    if not name.startswith("__"):  # Ignore built-in variables
        a.append(f"{name}")
print(a)'''