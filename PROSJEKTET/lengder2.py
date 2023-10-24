import numpy as np

def lengder2(knutepunkt, element, nelem):
 
    elementlengder = np.zeros((nelem, 1))
    # Beregner elementlengder med Pythagoras' læresetning
    for i in range (0, nelem):
        # OBS! Grunnet indekseringsyntaks i Python-arrays vil ikke denne funksjonen fungere naar vi bare har ett element.
        dx = knutepunkt[element[i][1]][1] - knutepunkt[element[i][2]][1]
        dy = knutepunkt[element[i][1]][2] - knutepunkt[element[i][2]][2]
        elementlengder[i] = np.sqrt(dx**2 + dy**2)
 
    return elementlengder
