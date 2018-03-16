import matplotlib.pyplot as plt
import numpy as np
import time as t

n = [112,120.2,109.2,128.3]
l = [221,302,192,283]

r=0

while True:
    T = np.linspace(-n[r]*np.pi,n[r]*np.pi,l[r])

    X = T*np.cos(T)
    Y = T*np.sin(T)

    plt.axis("equal")

    plt.plot(X,Y,color="#4286f4")

    plt.pause(0.5)

    plt.clf()

    r=(r+1)%len(l)
    
    print(n[r],l[r])

plt.show()
