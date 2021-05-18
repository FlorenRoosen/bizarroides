from math import *


def gen_liste(u1, r, q, n):
    liste = [u1]
    i = 0
    while i < n:
        liste.append(liste[i] * q + r)
        i += 1
    return liste


def gen_generateur(n):
    chaine = bin(n)
    liste = []
    i = 0
    for elem in chaine:
        if i > 1:
            liste.append(int(elem))
        i += 1
    return liste


def verif(matrice):
    i = 0
    ttl = 0
    while i < len(matrice):
        for elem in matrice[i]:
            ttl = elem + ttl
        if ttl != 0:
            return False

        ttl = 0
        i += 1

    return True


def transf_gen_matrice(generateur, liste):
    if len(generateur) != len(liste):
        print('génératrice de taille différente que la suite', len(generateur), len(liste))
    else:
        matrice = [0] * 2
        matrice[0] = []
        matrice[1] = []
        i = 0

        for elem in liste:
            matrice[i % 2].append(elem * (-1) ** generateur[i])
            i += 1
        return matrice


raison = 0
elem_multipl = 1.1
premier_elem = 1
n = 1  # ou les bornes sont du style ]x,y] avec y > x, x et y naturels

total = 0

i = 2 ** (n - 1)

while n < 21:
    while i < 2 ** (n):
        if verif(transf_gen_matrice(gen_generateur(i), gen_liste(premier_elem, raison, elem_multipl, n - 1))):
            total += 1
        i += 1
    print('premier elem =', premier_elem, ' ,raison = ', raison, ' ,n = ', n, ' ,nb_bizar = ', total)
    total = 0
    n += 1
    i = 2 ** (n - 1)
