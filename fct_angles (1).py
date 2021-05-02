import math
from tkinter import*

def convert(code,amplitude):
    if type(code) != str:
        print("Erreur de chaine")
    else:
        angle = 0
        x = 0
        y = 0
        i = 0
        chaine = [0,1]
        chaine[0] = []
        chaine[1] = []

        amplitude = amplitude*math.pi/180

        for élément in code:
            if élément == "0" and i>1:

                angle = angle - amplitude
                x = x + math.cos(angle)*(i-1)
                y = y + math.sin(angle)*(i-1)
                

            elif élément == "1" and i>1:

                angle = angle + amplitude
                x = x + math.cos(angle)*(i-1)
                y = y + math.sin(angle)*(i-1)

            chaine[0].append(x)
            chaine[1].append(y)

            i+=1
            

            
        return chaine


def affiche(x,y,coord,canva,prop):
    lignes = [0]*len(coord[0])
    i = 0
    while i < len(coord[0])-1:
        lignes[i] = canva.create_line(x+coord[0][i]*prop,y+coord[1][i]*prop,x+coord[0][i+1]*prop,y+coord[1][i+1]*prop)
        i += 1

def delim(coord):
    xM = 0
    xm = 0
    yM = 0
    ym = 0

    for x in coord[0]:
        if x > xM:
            xM = x
        elif x < xm:
            xm = x
    for y in coord[1]:
        if y > yM:
            yM = y
        elif y < ym:
            ym = y

    maxim = [xM,xm,yM,ym]
    return maxim

def run_possib(nr_essai,nr_étapes,amplitude):

    valids = []
    while nr_essai < 2**nr_étapes:

        code = bin(nr_essai)
        liste = convert(code,amplitude)
        if round(liste[0][-1],10) == 0 and round(liste[1][-1],10) == 0:
            valids.append(liste)
            print("bon")
            print(len(code)-2,code,liste[0][-1],liste[1][-1])

        nr_essai += 1

    return valids
