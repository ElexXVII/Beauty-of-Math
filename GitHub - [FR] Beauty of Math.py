#   Créé par ElexXVII
#   Pour GitHub
#   Apprécie la beauté des maths xD
#
###################################################
###################################################
# Import

#Methodes de tracer de graph
import matplotlib.pyplot as plt
#Methodes de créations de listes
import numpy as np
#Fonctions maths
from math import pi, cos, sin

###################################################
###################################################
# Tracé du cercle

#Cercle de 500 points
lt = [t for t in np.linspace(0,2*pi,500)]
lx = [cos(t) for t in lt]
ly = [sin(t) for t in lt]

#Trace le cercle
plt.axis('equal')
plt.plot(lx,ly, c = 'red')

#Rafraichi le graph
plt.pause(0.00001)
###################################################
###################################################
# Table 2

print("")

#Nombre de points sur le cercle
p = 10
#Table utilisé
ta = 4

#Nombre de répétitions de la boucle
tot = 10000
#Précision de l'animation
dtot = tot/100

#Boucle principale de l'animation
for i in range(tot):

    #Augmenter le nombre de point pour faire lancer l'animation
    p += 1
    #Vous pouvez aussi augmenter la table utilisé pour obtenir un autre beau graph
    #ta += 1/pas

    #Affiche l'actuel nombre points et table utilisé
    print("table : "+ str(ta))
    print("points : " + str(p))

    #Trace le cerlce
    plt.axis('equal')
    plt.plot(lx,ly, c = 'red')

    #Pour chaque point
    for i in range(int(p)):
        #Tracer la ligne
        plt.plot([cos(2*pi/p*i),cos(2*pi/p*i*ta)],
                 [sin(2*pi/p*i),sin(2*pi/p*i*ta)], c = 'gray')

    #Rafraichi le graph
    plt.pause(0.000001)
    #Efface le graph
    plt.clf()

#Affiche le graph final
plt.show(0)





