import numpy as np
####################################################################
####################################################################
#############################Input##################################
alpha2 = 1
L = 1
h = 0.1
k = 0.01
n = 50                                             #j-end
ic_f = lambda x : np.sin(np.pi*x)                  #IC
bc_L = lambda t : 0                                #Left BC
bc_R = lambda t : 0                                #Right BC
#Exact Solution
u = lambda x,t : np.exp(-t*np.pi**2)*np.sin(np.pi*x)
####################################################################
####################################################################

t_end = n*k
lambda_new = alpha2*k/(h**2)
m = int(L/h)
x = []
w_old = []

t = []
for j in range(n+1) :
    t.append(j*k)

for i in range(0,m+1) :
  x.append(i*h)
  w_old.append(ic_f(x[i]))

print(w_old)
w_old = np.array(w_old)
print(w_old)

'''
print("Lambda = {:.2f}".format(lambda_new))
print("At t[j = {}] = {}".format(n,t_end))
print("x \t u\t\t\t w\t\t absolute error")
for i in range(m+1) :
    error = abs(u(x[i],t_end)-w_new[i])
    print("{:.2f}\t {:12.8e}\t {:15.8e}\t {:15.8e}".format(x[i],u(x[i],t_end),w_new[i],error))
'''