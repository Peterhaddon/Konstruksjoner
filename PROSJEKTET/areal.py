import numpy as np 

def areal(element): # Regner ut I_y for diverse profiler

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
        arealB = t * b
        return arealB
