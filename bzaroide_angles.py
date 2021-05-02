from fct_angles import*
from tkinter import*

nr_essai = 0
amplitude = 120
liste = []
maxim = []
i = 1
j = 1
propr = 5
xM = 0
xm = 0
yM = 0
ym = 0

print("intervalle de recherche [a,b]:")
nr_essai = 2**int(input("a:"))
nr_étapes = int(input("b:"))

fen = Tk()
canva = Canvas(fen,width=1500,height=1200,background='white')

#affiche(100,100,convert("0b110111",amplitude),canva,10)
liste = run_possib(nr_essai,nr_étapes,amplitude)
for elem in liste:
    maxim = delim(elem)
    if maxim[0] > xM:
        xM = maxim[0]
    elif maxim[1] < xm:
        xm = maxim[1]
    if maxim[2] > yM:
        yM = maxim[2]
    elif maxim[3] < ym:
        ym = maxim[3]
    
for elem in liste:
    maxim = delim(elem)
    affiche((xM-xm+2*propr)*i*propr,(yM-ym+2*propr)*j*propr,elem,canva,propr)
    
    #line = canva.create_line((maxim[0]-maxim[1])*i*propr,0,(maxim[0]-maxim[1])*i*propr,(maxim[2]-maxim[3])*j*propr)
    i += 1
    if i >= 1500/((xM-xm)*propr)-3:
        i = 1
        j+= 1
canva.pack()
fen.mainloop()