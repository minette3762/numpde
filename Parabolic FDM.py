import math
####################################################################
####################################################################
#############################Input##################################
alpha2 = 1
L = 1
h = 0.1
k = 0.01
n = 50                                             #j-end
ic_f = lambda x : math.sin(math.pi*x)              #IC
bc_L = lambda t : 0                                #Left BC
bc_R = lambda t : 0                                #Right BC
#Exact Solution
u = lambda x,t : math.exp(-t*math.pi**2)*math.sin(math.pi*x)
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

for j in range(1,n+1) :
    w_new = [bc_L(t[j])]
    for i in range(1,m) :
        w = (1-2*lambda_new)*w_old[i]+lambda_new*(w_old[i+1]+w_old[i-1])
        w_new.append(w)
     
    w_new.append(bc_R(t[j]))
    
    #update w_old
    w_old = w_new.copy()

print("Lambda = {:.2f}".format(lambda_new))
print("At t[j = {}] = {}".format(n,t_end))
print("x \t u\t\t\t w\t\t absolute error")
for i in range(m+1) :
    error = abs(u(x[i],t_end)-w_new[i])
    print("{:.2f}\t {:12.8e}\t {:15.8e}\t {:15.8e}".format(x[i],u(x[i],t_end),w_new[i],error))