import numpy as np
from elementfunksjoner import *

def element_stivhetsmatrise(element, lengder):

    #Definerer verdier for det aktuelle elementet
    L=lengder[element[0]] 
    E=element[3]
    A=areal(element)
    Iy=I(element)

    #setter opp tim 6x6 matrise, og adderer inn stivheter 
    k_lokal_matrise = np.zeros((6, 6)) 
    k_lokal_matrise [0][0] += E*A/L
    k_lokal_matrise [3][3] += E*A/L 
    k_lokal_matrise [0][3] += -E*A/L
    k_lokal_matrise [3][0] += -E*A/L 
    k_lokal_matrise [1][1] += 12*E*Iy/(L**3)
    k_lokal_matrise [4][4] += 12*E*Iy/(L**3) 
    k_lokal_matrise [1][4] += -12*E*Iy/(L**3)
    k_lokal_matrise [4][1] += -12*E*Iy/(L**3) 
    k_lokal_matrise [1][2] += -6*E*Iy/(L**2)
    k_lokal_matrise [1][5] += -6*E*Iy/(L**2) 
    k_lokal_matrise [2][1] += -6*E*Iy/(L**2)
    k_lokal_matrise [5][1] += -6*E*Iy/(L**2) 
    k_lokal_matrise [4][2] += 6*E*Iy/(L**2)
    k_lokal_matrise [2][4] += 6*E*Iy/(L**2)
    k_lokal_matrise [5][4] += 6*E*Iy/(L**2) 
    k_lokal_matrise [4][5] += 6*E*Iy/(L**2)
    k_lokal_matrise [2][2] += 4*E*Iy/L 
    k_lokal_matrise [5][5] += 4*E*Iy/L
    k_lokal_matrise [5][2] += 2*E*Iy/L 
    k_lokal_matrise [2][5] += 2*E*Iy/L

    return k_lokal_matrise

def trans_matrise(fi):

    cos_fi = np.cos(fi)
    sin_fi = np.sin(fi)
    
    T = np.array([
        [cos_fi, -sin_fi, 0, 0, 0, 0],
        [sin_fi, cos_fi,  0, 0, 0, 0],
        [0,      0,       1, 0, 0, 0],
        [0,      0,       0, cos_fi, -sin_fi, 0],
        [0,      0,       0, sin_fi, cos_fi,  0],
        [0,      0,       0, 0,      0,       1]
    ]) #ER DENNE RIKTIG? BOKA/koken HADDE FORSKJELLIG!!!!!!!!!-------------------OBSOBSOBS
    #ER DENNE RIKTIG? BOKA HADDE FORSKJELLIG!!!!!!!!!-------------------OBSOBSOBS
    #ER DENNE RIKTIG? BOKA HADDE FORSKJELLIG!!!!!!!!!-------------------OBSOBSOBS
    #ER DENNE RIKTIG? BOKA HADDE FORSKJELLIG!!!!!!!!!-------------------OBSOBSOBS
    #ER DENNE RIKTIG? BOKA HADDE FORSKJELLIG!!!!!!!!!-------------------OBSOBSOBS
    #ER DENNE RIKTIG? BOKA HADDE FORSKJELLIG!!!!!!!!!-------------------OBSOBSOBS
    return T


def trans_k(fi, k_matrise):
    
    # Finner k_g med ta transponert(T) x k_matrise x T
    T = trans_matrise(fi)
    k_transformert = np.matmul(np.matmul(np.transpose(T),k_matrise),T)
    return k_transformert



def global_stivhetsmatrise(knutepunkter, elementer, lengder):
    antall_kp = len(knutepunkter)
    gsm = np.zeros((antall_kp * 3, antall_kp * 3))

    # Går gjennom hvert element
    for i in range(len(elementer)):

        # Finner vinkel fi ift. global x-akse
        dx = knutepunkter[elementer[i][2]][1] - knutepunkter[elementer[i][1]][1]
        dy = knutepunkter[elementer[i][2]][2] - knutepunkter[elementer[i][1]][2] 
        fi = np.arctan2(dy, dx)

        # Bestemmer, så transformerer lokal stivhetsmatrise til globale koordinater
        k_lokal = element_stivhetsmatrise(elementer[i], lengder) 
        k_transformert = trans_k(fi, k_lokal)
        
        # Finner aktuelle knutepunktene
        element = elementer[i]
        nj1 = element[1]
        nj2 = element[2]

        # Går igjennom radene til den lokale stivhetsmatrisen
        for row in range(k_transformert.shape[0]):
            if row < 3:
                n =   int( 3 * (nj1 - 1) + row)
                m_1 = int( 3 * (nj1 - 1))
                m_2 = int( 3 * (nj1 - 1) + 1)
                m_3 = int( 3 * (nj1 - 1) + 2)
                m_4 = int( 3 * (nj2 - 1))
                m_5 = int( 3 * (nj2 - 1) + 1)
                m_6 = int( 3 * (nj2 - 1) + 2)

            else:
                n =   int( 3 * (nj2 - 1) + (row - 3))
                m_1 = int( 3 * (nj1 - 1))
                m_2 = int( 3 * (nj1 - 1) + 1)
                m_3 = int( 3 * (nj1 - 1) + 2)
                m_4 = int( 3 * (nj2 - 1))
                m_5 = int( 3 * (nj2 - 1) + 1)
                m_6 = int( 3 * (nj2 - 1) + 2)

            # Legger til bidraget i global stivhetsmatrise 
            gsm[n, m_1] += k_transformert[row, 0]
            gsm[n, m_2] += k_transformert[row, 1]
            gsm[n, m_3] += k_transformert[row, 2]
            gsm[n, m_4] += k_transformert[row, 3]
            gsm[n, m_5] += k_transformert[row, 4]
            gsm[n, m_6] += k_transformert[row, 5]

    return gsm




def lokal_lastvektor(elementlengder, element, fordelte_laster):

    element_index = element[0]
    lastvec = np.zeros(6)
    for i in range (len(fordelte_laster)): #sjekker om det aktuelle elementet har en fordelt last

        if fordelte_laster[i][1] == element_index:
            q1 = fordelte_laster[i][2]
            q2 = fordelte_laster[i][3]
            l = float(elementlengder[element_index])

            # deler opp lasten i to trekantlaster
            fim_ende1 = (-1/20) * (q1*l**2) + (-1/30) * (q2*l**2)
            fim_ende2 = ( 1/30) * (q1*l**2) + ( 1/20) * (q2*l**2)

            #fastinnspenningskrefter ved likevekt
            fis_ende2 = (fim_ende1 + fim_ende2 + (1/2 * q1 * l * 1/3 * l) + (1/2 * q2 * l * 2/3 * l))/(l)
            fis_ende1 = (1/2 * q1 * l) + (1/2 * q2 * l) - fis_ende2
            
            #legger fastinnspenningskrefter- og momenter i riktig rekkefølge
            lastvec = np.array([[0], [fis_ende1], [fim_ende1], [0], [fis_ende2], [fim_ende2]])
  
    return(lastvec)




def trans_lokal_lastvektor(fi, lokal_lastvektor):
    
    # Finner lastvektor i globalt system med ta T x k_matrise
    T = trans_matrise(fi)
    lastvektor_transformert = np.matmul(T,lokal_lastvektor)
    return lastvektor_transformert


def global_lastvektor(knutepunkter, elementer, elementlengder, fordelte_laster, punktlaster):
    antall_kp = len(knutepunkter)
    glv = np.zeros((antall_kp * 3)) #global lastvektor
    glv = np.transpose(glv) # trengs denne?

    # Går gjennom hvert element
    for i in range(len(elementer)):

        # Finner vinkel fi ift. global x-akse
        dx = knutepunkter[elementer[i][2]][1] - knutepunkter[elementer[i][1]][1]
        dy = knutepunkter[elementer[i][2]][2] - knutepunkter[elementer[i][1]][2] 
        fi = np.arctan2(dy, dx)

        # Bestemmer, så transformerer lokal lastvektor til globale koordinater
        lastvektor_lokal = lokal_lastvektor(elementlengder, elementer[i], fordelte_laster ) 
        lastvektor_transformert = trans_lokal_lastvektor(fi, lastvektor_lokal)
        
        # Finner aktuelle knutepunktene
        element = elementer[i]
        nj1 = element[1]
        nj2 = element[2]

        # Går igjennom radene til den lokale lastvektoren
        m_1 = int( 3 * (nj1))
        m_2 = int( 3 * (nj1) + 1)
        m_3 = int( 3 * (nj1) + 2)
        m_4 = int( 3 * (nj2))
        m_5 = int( 3 * (nj2) + 1)
        m_6 = int( 3 * (nj2) + 2)

        # Legger til bidraget i global lastvektor 
        glv[m_1] += lastvektor_transformert[0]
        glv[m_2] += lastvektor_transformert[1]
        glv[m_3] += lastvektor_transformert[2]
        glv[m_4] += lastvektor_transformert[3]
        glv[m_5] += lastvektor_transformert[4]
        glv[m_6] += lastvektor_transformert[5]

    glv -= punktlaster_vec(knutepunkter, punktlaster) #legger til bidrag fra punktlaster, med negativt fortegn?!
   
    return glv


def løs_deformasjoner(gsm, glv): #Løser likningssystemet fra global stivhetsmatrise og global lastvektor,
                                 #svaret vi får ut er deformasjonsvektoren 

    def_vec = np.matmul(np.linalg.inv(gsm),np.transpose(glv))

    return(def_vec)



def punktlaster_vec(knutepunkter, punktlaster): #Punktlaster kan kun tas opp i knutepunkt
                                                #Disse legges så direkte inn i den globale lastvektoren
    antall_kp = len(knutepunkter)
    plastvec = np.zeros((antall_kp * 3)) #global lastvektor for punktlaster

    for i in range (len(punktlaster)): #henter ut info for punktlastene

        knutepunkt = punktlaster[i][1]
        retning = punktlaster[i][2]
        lastintensitet = punktlaster[i][3]

# MÅ ENDRES
# MÅ ENDRES
# MÅ ENDRES
# MÅ ENDRES
# MÅ ENDRES


        x_komp = 0
        y_komp = -lastintensitet

# MÅ ENDRES
# MÅ ENDRES
# MÅ ENDRES
# MÅ ENDRES
# MÅ ENDRES
# MÅ ENDRES, alle punktlaster funker nå kun nedover! Må bruke retning til noe fornuftig, dekomponere til x og y komponenter...


        x_komp_index = int( 3 * (knutepunkt))
        y_komp_index = int( 3 * (knutepunkt) + 1)

        #innadderer lastintensiteten riktig plass i punktlastvektor
        plastvec[x_komp_index] += x_komp 
        plastvec[y_komp_index] += y_komp
        


    return(plastvec)


def lokale_deformasjoner():

    return()


def lokale_endekrefter():
    
    return()