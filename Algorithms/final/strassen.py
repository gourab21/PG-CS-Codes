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
        
        
