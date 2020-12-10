import numpy as np
####################################################################
####################################################################
#############################Input##################################
alpha2 = 1
L = 1
h = 0.1
k = 0.01
t_end = 0.5                         #j-end
ic_f = lambda x: np.sin(np.pi * x)  #IC
bc_L = lambda t: 0                  #Left BC
bc_R = lambda t: 0                  #Right BC
#Exact Solution
u = lambda x, t: np.exp(-t * np.pi**2) * np.sin(np.pi * x)
####################################################################
####################################################################

n = int(t_end / k)
lambda_new = alpha2 * k / (h**2)
m = int(L / h)
x = []
w_old = []

t = []
for j in range(n + 1):
    t.append(j * k)

for i in range(0, m + 1):
    x.append(i * h)
    w_old.append(ic_f(x[i]))
w_old = np.array(w_old)

A = np.zeros((m - 1, m - 1))
for i in range(m - 1):
    for j in range(m - 1):
        if i == j:
            A[i, j] = 1 + lambda_new
        elif i == j + 1 or i + 1 == j:
            A[i, j] = -lambda_new/2

B = np.zeros((m-1,m-1))
for i in range(m - 1):
    for j in range(m - 1):
        if i == j:
            B[i, j] = 1 - lambda_new
        elif i == j + 1 or i + 1 == j:
            B[i, j] = lambda_new/2

for j in range(1, n + 1):
    v = np.matmul(B,w_old[1:-1])
    w_new = np.linalg.solve(A, v)
    w_old[1:-1] = w_new.copy()

w_new = w_old.copy()

print("Lambda = {:.4f}".format(lambda_new))
print("At t[j = {}] = {}".format(n, t_end))
print("x \t\t u\t\t w\t\t absolute error")
for i in range(m + 1):
    error = abs(u(x[i], t_end) - w_new[i])
    print("{:.2f}\t {:12.8f}\t {:15.8f}\t {:15.3e}".format(
        x[i], u(x[i], t_end), w_old[i], error))
