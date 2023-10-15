
def lengder(knutepunkt, element, nelem):

    #Tror denne skal lage en liste med lengden av alle element i samme rekkefølge som 'elementer'
    #Nedenfor er det vi har fått utdelt fra 'https://www.ntnu.no/wiki/display/imtsoftware/Prosjektoppgave+i+TMR4167+Marin+teknikk+-+Konstruksjoner#ProsjektoppgaveiTMR4167MarinteknikkKonstruksjoner-Utdeltefunksjoner'
 
    elementlengder = np.zeros((nelem, 1))
    # Beregner elementlengder med Pythagoras' læresetning
    for i in range (0, nelem):
        # OBS! Grunnet indekseringsyntaks i Python-arrays vil ikke denne funksjonen fungere naar vi bare har ett element.
        dx = knutepunkt[element[i, 0], 0] - knutepunkt[element[i, 1], 0]
        dy = knutepunkt[element[i, 0], 1] - knutepunkt[element[i, 1], 1]
        elementlengder[i] = np.sqrt(dx*dx + dy*dy)
 
    return elementlengder