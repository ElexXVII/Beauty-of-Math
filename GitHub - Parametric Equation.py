import matplotlib.pyplot as plt
import numpy as np
from math import *

#Choose wich equation you want to draw (0 to 3)!
f = 3

#Create a list of value for t to draw each point
t = np.linspace(-100,100,1000000)

#Define all equation
def x0(k):
     return k+1

def y0(k):
     return k-1

def x1(k):
     return sin(k)+cos(k)

def y1(k):
     return sin(k)**3

def x2(k):
     return sin(2*k)

def y2(k):
     return sin(3*k)

def x3(k):
     return k/(1+k**4)

def y3(k):
     return k**3/(1+k**4)

#Create empty list
x = []
y = []

#Fill lists x and y with all points we will draw
for i in t:

     if f==0:
          x.append(x0(i))
          y.append(y0(i))
     
     if f==1:
          x.append(x1(i))
          y.append(y1(i))
          
     if f==2:
          x.append(x2(i))
          y.append(y2(i))
          
     if f==3:
          x.append(x3(i))
          y.append(y3(i))
          
     if f==4:
          x.append(x4(i))
          y.append(y4(i))
          
     if f==5:
          x.append(x5(i))
          y.append(y5(i))

#Plot the geometric figure
plt.plot(x,y)

if f==0:
	#Plot the 3 points in red for the straight line
	plt.scatter([1,2,5],[-1,0,3],color="r")

#Define a specific placement on graph for the straight line
elif f==0:
     plt.axis([-2,6,-2,6])

#Plot Grid or not :
#plt.grid(color='#999999', linewidth=1)
   
#Show Graph
plt.show()



