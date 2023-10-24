import numpy as np

def lengder(knutepunkter, elementer):
 
    elementlengder = np.zeros((len(elementer), 1))
    # Beregner elementlengder med Pythagoras' læresetning
    for i in range (0, len(elementer)):
        # OBS! Grunnet indekseringsyntaks i Python-arrays vil ikke denne funksjonen fungere naar vi bare har ett element.
        dx = knutepunkter[elementer[i][1]][1] - knutepunkter[elementer[i][2]][1]
        dy = knutepunkter[elementer[i][1]][2] - knutepunkter[elementer[i][2]][2]
        elementlengder[i] = np.sqrt(dx**2 + dy**2)
 
    return elementlengder


def I(element): # Regner ut I_y for diverse profiler

    if element[4] == 'i': # I-profil
        tf = element[8] # tykkelse flens 
        bf = element[7] # bredde flens
        ts = element[6] # tykkelse steg 
        hs = element[5] # høyde steg
        ey = (tf * 2 + hs) / 2 # arealsenter y
        Iy = ((bf * tf ** 3) / 12 + (ey - (tf / 2)) ** 2 * bf * tf) * 2 + (ts * hs ** 3) / 12
        return Iy

    elif element[4] == 'c': # rørprofil
        D = element[5] # ytre diameter
        t = element[6] # tykkelse
        d = D - 2 * t  # indre diameter
        Iy = (np.pi * ((D / 2) ** 4 - (d / 2) ** 4)) / 4 
        return Iy

    elif element[4] == 'b': # Kvadratisk box-profil
        b = element[5] # ytre bredde/høyde
        t = element[6] # tykkelse
        Iy = ((b ** 4) / 12) - (((b - 2 * t) ** 4) / 12)
        return Iy


def areal(element): # Regner ut areal for diverse profiler

    if element[4] == 'i': # I-profil
        tf = element[8] # tykkelse flens 
        bf = element[7] # bredde flens
        ts = element[6] # tykkelse steg 
        hs = element[5] # høyde steg
        arealI = 2 * (tf * bf) + (ts * hs)
        return arealI

    elif element[4] == 'c':      # rørprofil
        D = element[5]           # ytre diameter
        t = element[6]           # tykkelse
        d = D - 2 * t            # indre diameter
        R = D/2                  #ytre radius
        r = d/2                  #indre radius
        arealY = np.pi * R**2    #areal ytre
        areali = np.pi * r**2    #areal indre
        arealC = arealY - areali #totalt areal
        return arealC

    elif element[4] == 'b': # Kvadratisk box-profil
        b = element[5]      # ytre bredde/høyde
        t = element[6]      # tykkelse
        arealB = t * b      #totalt areal
        return arealB
