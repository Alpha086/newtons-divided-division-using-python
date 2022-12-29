import numpy as np
import matplotlib.pyplot as plt

S=0
P=1
def Polynomial(t, X,Y):
    A=Y
    B=Y
    n=len(A)
    C = []
    for j in range(1,n):
        A = list(B)
        C.append(B[j-1])
        for i in range(j,n):
            B[i]=(A[i]-A[i-1])/(X[i]-X[i-j])
        C.append(B[n-1])

    for k in range(n):
            S=S+P*C[k]
            P=P*(t-X[k])
    return S



R = 4
X = np.array([2,4.25,5.25,7.81,9.20,10.60])
Y = np.array([7.2,7.1,6.0,5.0,3.5,5.0])
print('\n',X)
print('\n',Y)
#I = np.arange(-2,10,0.1)
poly_fit=np.poly1d(np.polyfit(X,Y,10))

plt.scatter(X,Y)
plt.plot(X,Y)
plt.show()



#points=zip(X,Y)
#points=sorted(points, key=lambda point:point[0])
#X,Y=zip(*points)
#new_length = 25
#new_x = np.linspace(min(X), max(X), new_length)
#new_y = sp.interpolate.interp1d(X, Y, kind='cubic')(new_x)

