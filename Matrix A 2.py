import numpy as np

m = 10
alpha = 1
h = 0.1
k = 0.0005
lamb = (k/h**2)*alpha**2
A = np.zeros((m-1,m-1))

for i in range(m-1) :
    for j in range(m-1) :
        if i == j :
            A[i,j] = 1-2*lamb
        elif i == j+1 or i+1 == j :
            A[i,j] = lamb
print(A)