import numpy as np
from plotKrefter import *

def lengder(knutepunkter, elementer): # Regner ut lengden til elementer
 
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


def hoyde(element): # Regner ut høyde for diverse profiler

    if element[4] == 'i': # I-profil
        tf = element[8] # tykkelse flens 
        bf = element[7] # bredde flens
        ts = element[6] # tykkelse steg 
        hs = element[5] # høyde steg
        h = hs + 2 * tf
        return h

    elif element[4] == 'c': # rørprofil
        D = element[5] # ytre diameter
        t = element[6] # tykkelse
        d = D - 2 * t  # indre diameter
        h = D
        return h

    elif element[4] == 'b': # Kvadratisk box-profil
        b = element[5] # ytre bredde/høyde
        t = element[6] # tykkelse
        h = b
        return h


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
        arealB = b**2 - (b-2*t)**2      #totalt areal
        return arealB


def maks_krefter(elementer, elementlengder, res, fordelte_laster): # Finner de største kreftene som oppstår i et element
    #lager momentfunksjon for alle elementer

    #initialiserer lister:
    M_max=[]
    N_max=[]

    #Finner elementer med fordelte laster
    elementer_med_fordeltelaster=[]
    for i in range (len(fordelte_laster)):
        elementer_med_fordeltelaster.append(fordelte_laster[i][1])

    for i in range(len(elementer)):
        # Itererer gjennom alle elementene
        element = elementer[i]
        lengde = elementlengder[i]
        S = res[i]

        #Henter ut nødvendige verdier
        x = np.linspace(0, lengde, 100)
        M1=S[2]
        Q1=S[1]
        N1=S[0]

        # Løser funksjonen numerisk. Lineær fordeling hvis den ikke har fordelt last
        if element[0] in elementer_med_fordeltelaster:
            q1, q2 = hent_q1_og_q2(element[0], fordelte_laster)
            moment = -(-M1 -Q1*x) + (((q2-q1)*x/lengde + q1)*x * (x/2))
        
        else:
            moment = -M1 -Q1*x
        
        maks_moment = max(abs(moment)) #henter ut høyeste verdi funnet fra hver ende eller midten
            # Da vi regner for 100 steg blir 50 midtmoment

        # legger til den høyeste verdien for aktuelt element i listen over høyeste moment for alle element
        M_max.append(maks_moment)
        N_max.append(N1)


    return M_max, N_max


def midt_krefter(elementer, elementlengder, res, fordelte_laster): # Finner kreftene som oppstår midt i et element
    #lager momentfunksjon for alle elementer

    #initialiserer lister:
    M_midt=[]

    #Finner elementer med fordelte laster
    elementer_med_fordeltelaster=[]
    for i in range (len(fordelte_laster)):
        elementer_med_fordeltelaster.append(fordelte_laster[i][1])

    for i in range(len(elementer)):
        # Itererer gjennom alle elementene
        element = elementer[i]
        lengde = elementlengder[i]
        S = res[i]

        #Henter ut nødvendige verdier
        x = np.linspace(0, lengde, 100)
        M1=S[2]
        Q1=S[1]
        N1=S[0]

        # Løser funksjonen numerisk. Lineær fordeling hvis den ikke har fordelt last
        if element[0] in elementer_med_fordeltelaster:
            q1, q2 = hent_q1_og_q2(element[0], fordelte_laster)
            moment = -(-M1 -Q1*x) + (((q2-q1)*x/lengde + q1)*x * (x/2))
        
        else:
            moment = -M1 -Q1*x
        
        midt_moment = max(abs(moment[50])) #henter ut høyeste verdi funnet fra hver ende eller midten
            # Da vi regner for 100 steg blir 50 midtmoment

        # legger til den høyeste verdien for aktuelt element i listen over høyeste moment for alle element
        M_midt.append(midt_moment)



    return M_midt


def maks_spenning(M, N_maks, element): #Finner høyeste spenning i bjelken

    #Henter ut Nødvendige verdier for bjelken
    M = M[0]
    N = N_maks
    E = element[3]
    Iy = I(element)
    A = areal(element)
    z = hoyde(element)

    #regner ut bøyespenningen:
    sigma = abs(max([((M / Iy) * z) + (N)/A , ((M / Iy) * -z) + (N)/A , 
    ((M / Iy) * -z) - (N)/A , ((M / Iy) * -z) - (N)/A] , key=abs)) 
    #abs M da vi kun er interessert i absoluttverdien av dette
    
    return sigma


def prosent_flyt(sigma, element): # Hvor mange prosent av flytspenning er maks spenning
    prosent = []
    if element[4] == 'c':
        prosent.append(np.round((abs(sigma)/420) * 100)) #Flytspenning stål
    else:
        prosent.append(np.round((abs(sigma)/250) * 100)) #Flytspenning aluminium
    return prosent


def print_prosent_flyt(elementer, elementlengder, res, fordelte_laster): #Printer alle elementers utnyttelsesgrad

    M_maks, N_maks = maks_krefter(elementer, elementlengder, res, fordelte_laster)
    for i in range(len(elementer)):

        sigma = maks_spenning(M_maks[i], N_maks[i], elementer[i])
        sigma_rounded = int(np.round(sigma))
        prosent = prosent_flyt(sigma, elementer[i])
        prosent_rounded = int(np.round(prosent[0]))
        M_maks_rounded = (np.round(M_maks[i][0],2))
        print(f"Element: {elementer[i][0]:4}   Sigma (N/mm^2): {sigma_rounded:10}     Prosent av flyt: {prosent_rounded:6}  ")


def print_momenter(elementer, elementlengder, res, fordelte_laster): #Printer ende og midtmoment for alle element


    M_midt = midt_krefter(elementer, elementlengder, res, fordelte_laster)

    print(f"Elementnr:   M1:          M2:      M midt:") # moment
    # print(f"Elementnr:   Q1:          Q2:") #skjær


    for i in range(len(elementer)):
       print(f"{elementer[i][0]:4} {round(res[i][2]):12} {round(res[i][5]):12} {round(M_midt[i]):12}") #Moment
    #    print(f"{elementer[i][0]:4} {round(res[i][1]):12} {round(res[i][4]):12} ") #Skjaer

