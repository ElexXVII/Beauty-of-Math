import matplotlib.pyplot as plt
import numpy as np
import time as t

n = 50.5    # 50.5,
l = [69,76,77]

r=0

while True:
    T = np.linspace(-n*np.pi,n*np.pi,l[r])

    X = T*np.cos(T)
    Y = T*np.sin(T)

    plt.axis("equal")

    plt.plot(X,Y,color="#4286f4")

    plt.pause(0.5)

    plt.clf()

    r=(r+1)%len(l)

plt.show()
