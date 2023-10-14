import numpy as np

def I(element): # Regner ut Iy for diverse profiler

    if element[3] == 'i': # I-profil
        tf = element[7] # tykkelse flens 
        bf = element[6] # bredde flens
        ts = element[5] # tykkelse steg 
        hs = element[4] # høyde steg
        ey = (tf * 2 + hs) / 2 # arealsenter y
        Iy = ((bf * tf ** 3) / 12 + (ey - (tf / 2)) ** 2 * bf * tf) * 2 + (ts * hs ** 3) / 12
        return Iy

    elif element[3] == 'c': # rørprofil
        d = element[4] # indre diameter
        D = element[5] # ytre diameter
        Iy = (np.pi * ((D / 2) ** 4 - (d / 2) ** 4)) / 4 
        return Iy

    elif element[3] == 'b': # Kvadratisk box-profil
        b = element[4] # ytre bredde/høyde
        t = element[5] # tykkelse
        Iy = ((b ** 4) / 12) - (((b - 2 * t) ** 4) / 12)
        return Iy