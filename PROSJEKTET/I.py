import numpy as np

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