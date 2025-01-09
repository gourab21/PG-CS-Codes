
import numpy as np
import math

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
	# Splitting the matrices into quadrants. This will be done recursively
	# until the base case is reached.
	a, b, c, d = split(x)
	e, f, g, h = split(y)
	
	# Computing the 7 products, recursively (p1, p2...p7)
	p1 = strassen(a, f - h) 
	p2 = strassen(a + b, h)	 
	p3 = strassen(c + d, e)	 
	p4 = strassen(d, g - e)	 
	p5 = strassen(a + d, e + h)	 
	p6 = strassen(b - d, g + h) 
	p7 = strassen(a - c, e + f) 

	# Computing the values of the 4 quadrants of the final matrix c
	c11 = p5 + p4 - p2 + p6 
	c12 = p1 + p2		 
	c21 = p3 + p4		 
	c22 = p1 + p5 - p3 - p7
	 
	# Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
        # vstack and hstack are used to join matrices.
	return c

#a=[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
#b=[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
a=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
b=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]





x=len(a)
p=math.log(x)/math.log(2)

if (p).is_integer():
	u=np.matrix(a,)                
	v=np.matrix(b,)        
	print(strassen(u,v))
else:
	p=math.ceil(p)+1
	p=2**p
	u=[[0]*p]*p
	v=[[0]*p]*p
	for i in range(x):
		tem1=[]
		tem2=[]		
		for j in range(p):
			if j<x:
				tem1.append(a[i][j])
				tem2.append(b[i][j])
			else:
				tem1.append(0)
				tem2.append(0)
		u[i]=tem1
		v[i]=tem2
		
	u=np.matrix(u,)                
	v=np.matrix(v,)
	t=(strassen(u,v))
	i=t[:x,:x]
	#for m in(i[0])
	print(i)
