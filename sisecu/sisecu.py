#Sistemas de ecuaciones lineales
import numpy as np
import matplotlib.pyplot as plt
from sympy import Matrix, Symbol, eye

A = Matrix([[2, 3, 40], [10, 2, 3], [50, 0, 4]])

(x,y)=A.shape

for i in range(x):
	for j in range(y):
		if(i == j):
			if (A[i,j] == 1):
				continue
			else:
				A[i,:] = A[i,:] / (A[i,j]) 
				

print np.matrix(A)

#print A[1,1]
#print np.matrix(A[0,:])*(A[1,1])
print A[0,:]
