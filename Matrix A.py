import numpy as np

m = 10
A = np.zeros([m-1,m-1])
alpha2 = 1
h = 0.1
k = 0.0005
lambda_new = alpha2*k/(h**2)
for i in range(0,m-1) :
    A[i,i] = 1-2*lambda_new
for j in range(0,m-2) :
    A[j,j+1] = lambda_new
for k in range(1,m-1) :
    A[k,k-1] = lambda_new
print(A)