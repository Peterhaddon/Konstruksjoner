import numpy as np

def element_stivhetsmatrise(element):

    #Må bestemmes for aktuelt element
    L=1
    E=1
    A=1
    Iy=1

    #setter opp tim 6x6 matrise, og adderer inn stivheter 

    #ER FORTEGN osv RIKTIG???

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




#Lager en stor liste med matriser av lokale stivhetsmatriser 
def element_stivhetsmatriser(elementer):
    element_stivhetsmatriser = np.empty(len(elementer)) #lag en tom array
    for i in range(len(elementer)):
        element_stivhetsmatriser[i] = element_stivhetsmatrise(elementer[i])
    return element_stivhetsmatriser










def global_stivhetsmatrise(konnektivitets_matrise, antall_kp, element_stivhetsmatriser): #elementdata osv må og inn
    
    #lager en tom totalstivhetsmatrise med 3*npunk fordi vi har 3 frihetsgrader
    gsm = np.zeros((antall_kp*3, antall_kp*3))
    print(gsm)

    for i in range (len(konnektivitets_matrise)): #tror det blir riktig mengde iterasjoner, lik mengden element
    # for i in range (0):

        #FEIL: HUSK Å ENDRE
        lokal_stivhetsmatrise = np.array([[4, 2], [2, 4]]) * 1 #ny for hvert nye element. mangler EI/L greiene, må ganges inn for hvert element
           
        #Legger inn tall fra lokal stivhetsmatrise riktig plass i global stivhetsmatrise
        node1, node2 = konnektivitets_matrise[i]  # Global node indekser for nåværende element
    
        #Legger inn tall fra lokal stivhetsmatrise riktig plass i global stivhetsmatrise

        #Her har jeg bare brukt 2 frihetsgrader, skal ha 6... OBS OBS må endres

        gsm[node1, node1] += lokal_stivhetsmatrise[0, 0]
        gsm[node1, node2] += lokal_stivhetsmatrise[0, 1]
        gsm[node2, node1] += lokal_stivhetsmatrise[1, 0]
        gsm[node2, node2] += lokal_stivhetsmatrise[1, 1]

        #Uryddig men forståelig variant av det samme:
        # gsm[konnektivitets_matrise[i,0]  ,  konnektivitets_matrise[i,0]] += lokal_stivhetsmatrise[0,0]
        # gsm[konnektivitets_matrise[i,1]  ,  konnektivitets_matrise[i,0]] += lokal_stivhetsmatrise[1,0]
        # gsm[konnektivitets_matrise[i,0]  ,  konnektivitets_matrise[i,1]] += lokal_stivhetsmatrise[0,1]
        # gsm[konnektivitets_matrise[i,1]  ,  konnektivitets_matrise[i,1]] += lokal_stivhetsmatrise[1,1]


    return gsm
    #får ut noe mystiske verdier, må dobbeltsjekkes