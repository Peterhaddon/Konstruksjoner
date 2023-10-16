import numpy as np

def global_stivhetsmatrise(konnektivitets_matrise, antall_kp): #elementdata osv må og inn
    n = antall_kp #må være lik total antall kp! 
    gsm = np.empty((n, n))

    for i in range (len(konnektivitets_matrise)): #tror det blir riktig mengde iterasjoner, lik mengden element

        lokal_stivhetsmatrise = np.array([[4, 2], [2, 4]]) * 1 #ny for hvert nye element. mangler EI/L greiene, må ganges inn for hvert element
            #Legger inn tall fra lokal stivhetsmatrise riktig plass i global stivhetsmatrise
        gsm[konnektivitets_matrise[i,0]  ,  konnektivitets_matrise[i,0]] += lokal_stivhetsmatrise[0,0]
        gsm[konnektivitets_matrise[i,1]  ,  konnektivitets_matrise[i,0]] += lokal_stivhetsmatrise[1,0]
        gsm[konnektivitets_matrise[i,0]  ,  konnektivitets_matrise[i,1]] += lokal_stivhetsmatrise[0,1]
        gsm[konnektivitets_matrise[i,1]  ,  konnektivitets_matrise[i,1]] += lokal_stivhetsmatrise[1,1]


    return gsm
    #får ut noe mystiske verdier, må dobbeltsjekkes