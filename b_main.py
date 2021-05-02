from tkinter import *


# 1 == négatif
# 0 == positif


def aff_bizar(x, y, prop, code, canva):
    if type(code) != str:
        print("ERREUR pas de code")
    else:
        droites = [0] * (len(code) - 2)
        i = 1

        while i < len(code) - 1:

            if code[-i] == "0":
                if i % 2 == 1:
                    droites[i - 1] = canva.create_line(x, y, x + i * prop, y)
                    x = x + prop * i
                elif i % 2 == 0:
                    droites[i - 1] = canva.create_line(x, y, x, y + i * prop)
                    y = y + prop * i
            elif code[-i] == "1":
                if i % 2 == 1:
                    droites[i - 1] = canva.create_line(x, y, x - i * prop, y)
                    x = x - prop * i
                elif i % 2 == 0:
                    droites[i - 1] = canva.create_line(x, y, x, y - i * prop)
                    y = y - prop * i
            i += 1


def delim(code):
    i = 0
    x = 0
    y = 0
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    while i < len(code) - 2:
        if code[-i] == "0":
            if i % 2 == 1:
                x += i
            elif i % 2 == 0:
                y += -i
        elif code[-i] == "1":
            if i % 2 == 1:
                x += -i
            elif i % 2 == 0:
                y += i

        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
        i += 1

    chaine = [max_x, min_x, max_y, min_y]
    return chaine


def allign(figures):
    M_x = 0
    M_y = 0
    m_x = 0
    m_y = 0
    max_min = []
    for bizar in figures:
        max_min = delim(bizar)

        if max_min[0] > M_x:
            M_x = max_min[0]
        if max_min[1] < m_x:
            m_x = max_min[1]
        if max_min[2] > M_y:
            M_y = max_min[2]
        if max_min[3] < m_y:
            m_y = max_min[3]
    largeur = M_x - m_x
    hauteur = M_y - m_y
    chaine = [hauteur, largeur]
    return chaine


def recherche(a, b):
    nr_étapes = b
    nr_essai = 2 ** a

    j = 1

    while nr_essai < 2 ** nr_étapes:
        chaine = str(bin(nr_essai))
        n = len(chaine) - 2
        x = 0
        y = 0
        i = 1
        while i <= n:
            if chaine[-i] == "0":
                if i % 2 == 1:
                    x += i
                elif i % 2 == 0:
                    y += i
            elif chaine[-i] == "1":
                if i % 2 == 1:
                    x += -i
                elif i % 2 == 0:
                    y += -i
            i += 1
        if y == 0 and x == 0:
            figures.append(chaine)
            # print(j," ",chaine)
            j += 1
        nr_essai += 1


def branche(c_x, c_y, code, parité):
    i = 1
    x = c_x
    y = c_y
    vecteur = (2 * propr, 1 * propr)
    if parité:
        reste = 1
    else:
        reste = 0
    while i < len(code) - 1:
        if i % 2 == reste:
            if code[-i] == '1':
                canva.create_line(x, y, x + vecteur[0] * i, y + vecteur[1] * i)
                x += vecteur[0] * i
                y += vecteur[1] * i
            elif code[-i] == '0':
                canva.create_line(x, y, x + vecteur[0] * i, y - vecteur[1] * i)
                x += (vecteur[0]) * i
                y -= (vecteur[1]) * i

        i += 1


def arbre(x, y, parité):
    o = 0

    for elem in figures:
        branche(x, y + o, elem, parité)
        # o+=0.1


def construction_listbox():
    i = 0
    while i < len(figures):
        liste.insert(i, figures[i][1:])
        i += 1


def selection(event=None):
    biz.delete(ALL)
    canva.delete(ALL)
    entite_select = liste.curselection()
    print(entite_select)
    aff_bizar(cote_canv / 4, cote_canv / 4, propr, figures[entite_select[0]], biz)
    branche(50, cote_canv / 4, figures[entite_select[0]], True)
    branche(50, cote_canv * 3 / 4, figures[entite_select[0]], False)
    changer_texte(figures[entite_select[0]])


def changer_texte(code):
    i = 1
    x = ''
    y = ''
    while i < len(code) - 1:
        if i % 2 == 1:
            if code[-i] == '1':
                x += ', -' + str(i)
            elif code[-i] == '0':
                x = x + ', ' + str(i)
        i += 1

    i = 1
    while i < len(code) - 1:
        if i % 2 == 0:
            if code[-i] == '1':
                y += ', ' + str(i)
            elif code[-i] == '0':
                y = y + ', -' + str(i)
        i += 1
    cotes_x.set(x)
    cotes_y.set(y)


figures = []
dico_chem = {}
propr = 3
cote_canv = 500
cote_txt = 300

print("intervalle de recherche [a,b]:")
a = int(input("a:"))
b = int(input("b:"))

recherche(a, b)
print(len(figures))

fen = Tk()

cotes_y = StringVar()
cotes_x = StringVar()
cotes_x.set('/')
cotes_y.set('/')

graph_gauche = Frame(fen, width=cote_canv, height=cote_canv)
graph_gauche.pack(side=LEFT)
graph_droite = Frame(fen, width=cote_txt, height=cote_canv)
graph_droite.pack(side=RIGHT)
zone_dessin = Frame(graph_droite, width=cote_txt, height=int(cote_canv / 2))
zone_txt = Frame(graph_droite, height=int(cote_canv / 2))
zone_txt_txt = Frame(zone_txt)
canva = Canvas(graph_gauche, width=cote_canv, height=cote_canv, background='white')
biz = Canvas(zone_dessin, width=cote_canv / 2, height=cote_canv / 2, background='white')
liste = Listbox(zone_txt)

label1 = Label(zone_txt_txt, textvariable=cotes_x)
label1a = Label(zone_txt_txt, text="cotes_x")
label2 = Label(zone_txt_txt, textvariable=cotes_y)
label2a = Label(zone_txt_txt, text="cotes_y")

label1a.pack(side=TOP, pady=5, padx=5)
label1.pack(side=TOP)
label2.pack(side=BOTTOM)
label2a.pack(side=BOTTOM, pady=5, padx=5)

fen.bind("<Return>", selection)
fen.bind("<Button-1>", selection)

zone_txt.pack(side=BOTTOM)
zone_txt_txt.pack(side=TOP)
zone_dessin.pack(side=TOP)
liste.pack(side=BOTTOM)
canva.pack()
biz.pack()

construction_listbox()
arbre(50, cote_canv / 4, True)
arbre(50, cote_canv * 3 / 4, False)
fen.mainloop()
