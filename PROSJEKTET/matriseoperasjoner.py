import numpy as np
from elementfunksjoner import *

def element_stivhetsmatrise(element, lengder): # Lager lokal stivhetsmatrise for element

    #Definerer verdier for det aktuelle elementet
    L=lengder[element[0]] 
    E=element[3]
    A=areal(element)
    Iy=I(element)

    # L=E=A=Iy=1


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


def trans_matrise(fi): #Lager matrise fra lokalt til globalt

    cos_fi = np.cos(fi)
    sin_fi = np.sin(fi)
    
    T = np.array([
        [cos_fi, -sin_fi, 0,  0,     0,        0],
        [sin_fi, cos_fi,  0,  0,     0,        0],
        [0,      0,       1,  0,     0,        0],
        [0,      0,       0,  cos_fi, -sin_fi, 0],
        [0,      0,       0,  sin_fi, cos_fi,  0],
        [0,      0,       0,  0,      0,       1]]) 
    return T


def trans_k(fi, k_matrise): # Transformerer k
    
    # Finner k_g med ta transponert(T) x k_matrise x T

    T = trans_matrise(fi)
    k_transformert = np.matmul(np.transpose(T), np.matmul(k_matrise,T))
    return k_transformert


def global_stivhetsmatrise(knutepunkter, elementer, lengder): #adderer inn stivhetsmatriser
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
        node1 = element[1]
        node2 = element[2]

        for j in range(3): #legger det inn riktig plass i global stivhetsmatrise
            for k in range(3):
                gsm[node1*3 + j, node1*3 + k] += k_transformert[j  ][k  ]
                gsm[node1*3 + j, node2*3 + k] += k_transformert[j  ][k+3]
                gsm[node2*3 + j, node1*3 + k] += k_transformert[j+3][k  ]
                gsm[node2*3 + j, node2*3 + k] += k_transformert[j+3][k+3]

    gsm = legg_inn_randbetingelser(knutepunkter,gsm) #legger inn nødvendige høye fjærstivheter som randbetignelser

    return gsm


def lokal_lastvektor(elementlengder, element, fordelte_laster):#lager den lokale lastvektoren

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

            #fastinnspennings-skjærkrefter ved likevekt
            fis_ende2 = (fim_ende1 + fim_ende2 + (1/2 * q1 * l * 1/3 * l) + (1/2 * q2 * l * 2/3 * l))/(l)
            fis_ende1 = (1/2 * q1 * l) + (1/2 * q2 * l) - fis_ende2
            
            #legger inn fastinnspenningskrefter- og momenter
            lastvec = np.array([0, fis_ende1, fim_ende1, 0, fis_ende2, fim_ende2])
  
    return(lastvec) 


def trans_lokal_lastvektor(fi, lokal_lastvektor): #trans lok til glob
    
    # Finner lastvektor i globalt system med ta T x k_matrise
    T = trans_matrise(fi)
    lastvektor_transformert = np.matmul(T,lokal_lastvektor)
    return lastvektor_transformert


def trans_global_lastvektor(fi, global_lastvektor): #trans glob til lok
    
    # Finner lastvektor i globalt system med ta T(transponert) x k_matrise
    T = trans_matrise(-fi)
    lastvektor_transformert = np.matmul(np.transpose(T),global_lastvektor)

    return lastvektor_transformert


def global_lastvektor(knutepunkter, elementer, elementlengder, fordelte_laster, punktlaster): # Oppretter den globale lastvektoren
    antall_kp = len(knutepunkter)
    glv = np.zeros((antall_kp * 3)) #global lastvektor
    # glv = np.transpose(glv) # trengs denne?

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

    glv -= punktlaster_vec(knutepunkter, punktlaster) #legger til bidrag fra punktlaster, med negativt fortegn
    return glv


def legg_inn_randbetingelser(knutepunkter, gsm): #legger inn randbetignelser
    #skjekker betingelse om punkt er fast innspent eller fritt opplagt, ganger inn stivhet på diagonalen som følge
    for i in range(len(knutepunkter)): 
        #1 = fast innspent
        if(knutepunkter[i][3] == 1): 
            gsm[3*i  ][3*i  ] *= 10**6
            gsm[3*i+1][3*i+1] *= 10**6 
            gsm[3*i+2][3*i+2] *= 10**6
        #2 = fritt opplagt
        elif(knutepunkter[i][3] == 2):
            gsm[3*i  ][3*i  ] *= 10**6 
            gsm[3*i+1][3*i+1] *= 10**6
    return gsm


def punktlaster_vec(knutepunkter, punktlaster): #Punktlaster kan kun tas opp i knutepunkt
                                                #Disse legges så direkte inn i den globale lastvektoren
    antall_kp = len(knutepunkter)
    plastvec = np.zeros((antall_kp * 3)) #global lastvektor for punktlaster

    for i in range (len(punktlaster)): #henter ut info for punktlastene

        knutepunkt = punktlaster[i][1]
        retning_deg = punktlaster[i][2]
        lastintensitet = punktlaster[i][3]

        # Konverterer retning fra grader til radianer
        retning_rad = np.radians(retning_deg)

        # Regner ut sin og cos for retningen i radianer
        sin_retning = np.sin(retning_rad)
        cos_retning = np.cos(retning_rad)

        # Beregner x- og y-komponentene av lastintensiteten basert på retningen
        x_komp = np.round(lastintensitet * cos_retning, 10)
        y_komp = np.round(lastintensitet * sin_retning, 10)

        #finner riktig index for komponentene som skal i punktlastvektoren
        x_komp_index = int( 3 * (knutepunkt)    )
        y_komp_index = int( 3 * (knutepunkt) + 1)

        #innadderer lastintensiteten i punktlastvektor
        plastvec[x_komp_index] += x_komp 
        plastvec[y_komp_index] += y_komp

    return(plastvec)


def løs_deformasjoner(gsm, glv): #Løser likningssystemet fra global stivhetsmatrise og global lastvektor,
                                 #svaret vi får ut er deformasjonsvektoren 

    r = np.matmul(np.linalg.inv(gsm),glv) #løser likningen r = K^-1 * R

    return(r) #returnerer vektor med deformasjoner


def S_solve(knutepunkter, elementer, elementlengder, r, fordelte_laster): #løser endekrefter og endemoment

    res = np.empty((len(elementer), 6))  # Oppretter et tomt resultat-array

    for x in range(len(elementer)):
        # Henter ut de aktuelle fastinnspenningskreftene
        fik = lokal_lastvektor(elementlengder, elementer[x], fordelte_laster)

        # Henter så ut tverrsnittsdata
        k_lok = element_stivhetsmatrise(elementer[x], elementlengder)

        knutepunkt_1 = elementer[x][1]
        knutepunkt_2 = elementer[x][2]

        # Henter ut liste med deformasjoner for elementets knutepunkt 1 og 2
        v_1 = r[(knutepunkt_1) * 3:(knutepunkt_1) * 3 + 3]
        v_2 = r[(knutepunkt_2) * 3:(knutepunkt_2) * 3 + 3]

        # Setter sammen de to arrayene i en matrise
        v_tot = np.concatenate((v_1, v_2))

        # Finner elementvinkel fi ift. global x-akse
        dx = knutepunkter[knutepunkt_2][1] - knutepunkter[knutepunkt_1][1]
        dy = knutepunkter[knutepunkt_2][2] - knutepunkter[knutepunkt_1][2]
        fi = np.arctan2(dy, dx)

        # Transformerer deformasjonene tilbake til lokalt koordinatsystem
        v_tot_lokal = trans_global_lastvektor(fi, v_tot)


        # Løser ligningsystemet i lokalt system, og får kreftene som virker i knutepunktene
        S = np.dot(k_lok, v_tot_lokal) - fik

        # Legger så til disse kreftene i resultatarrayet
        res[x] = S

    return res
