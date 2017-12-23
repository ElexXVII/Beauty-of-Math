#   Created by ElexXVII
#   For Github and Utopian.io
#   Enjoy Beauty of Math!
#
###################################################
###################################################
# Import

#Chart drawing methods
import matplotlib.pyplot as plt
#List methods
import numpy as np
#Math fonction
from math import pi, cos, sin

###################################################
###################################################
# Circle Drawing

#500 points circle
lt = [t for t in np.linspace(0,2*pi,500)]
lx = [cos(t) for t in lt]
ly = [sin(t) for t in lt]

#Draw the circle
plt.axis('equal')
plt.plot(lx,ly, c = 'red')

#Refresh the chart
plt.pause(0.00001)
###################################################
###################################################
# Table 2

print("")

#Number of points on the circle
p = 10
#Table used
ta = 4

#Number of loop repetitions
tot = 10000
#Precision of the animation
dtot = tot/100

#Main loop for the animation
for i in range(tot):

    #increase the number of points to make the chart move
    p += 1
    #You can also increase the table used to get an other beautiful animation
    #ta += 1/pas

    #Show the current table and number of points used
    print("table : "+ str(ta))
    print("points : " + str(p))

    #Draw the circle
    plt.axis('equal')
    plt.plot(lx,ly, c = 'red')

    #For each point
    for i in range(int(p)):
        #Draw line
        plt.plot([cos(2*pi/p*i),cos(2*pi/p*i*ta)],
                 [sin(2*pi/p*i),sin(2*pi/p*i*ta)], c = 'gray')

    #Refresh the chart
    plt.pause(0.000001)
    #Clean the chart
    plt.clf()

#Show the final chart
plt.show(0)





