import matplotlib.pyplot as plt
import numpy as np

def plot_moment(elementer, elementlengder, res, fordelte_laster):
    #plotter momentfunksjon for alle elementer

    #initialiserer verdier:
    n = int(np.sqrt(len(elementer))+1)
    fig, axes = plt.subplots(n, n, figsize=(10, 8))

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
        x = np.linspace(0, lengde, 1000)
        M1=S[2]
        Q1=S[1]

        # Løser funksjonen numerisk. Lineær fordeling hvis den ikke har fordelt last
        if element[0] in elementer_med_fordeltelaster:
            q1, q2 = hent_q1_og_q2(element[0], fordelte_laster)
            moment = (1/3* q1*x**2+1/6 *(q1 +((q2-q1)/(lengde))*x)*x**2 -Q1*x -M1)
        
        else:
            moment = -M1 -Q1*x
        

        # legger til den høyeste verdien for aktuelt element i listen over høyeste moment for alle element


        # Delplott for gjeldende element
        ax = axes[i // n, i % n]
        # Plotter momentet
        ax.plot(x, moment, color='blue')

        # Add a horizontal line at y=0
        ax.axhline(0, color='red', linestyle='--', label='y=0')
        ax.set_title(f'{element[0]}')

    # Juster layout for å unngå overlappende titler og etiketter.
    plt.tight_layout()
    plt.show()

def hent_q1_og_q2(element_identifikator, fordelte_laster):
    # henter q1 og q2 for aktuelle element
    for fordelt_last in fordelte_laster:
        if fordelt_last[1] == element_identifikator:
            # Returner q1 og q2 for riktig element_identifikator
            return fordelt_last[1], fordelt_last[2]
    
    # Hvis element_identifikator ikke finnes i fordelte_laster, returner 0,0
    return 0, 0

def plot_skjaer(elementer, elementlengder, res, fordelte_laster):
    #plotter skjærfunksjon for alle elementer

    n = int(np.sqrt(len(elementer))+1)
    fig, axes = plt.subplots(n, n, figsize=(10, 8))

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
        x = np.linspace(0, lengde, 1000)
        Q1=S[1]

        # Løser funksjonen numerisk. flat fordeling hvis den ikke har fordelt last
        if element[0] in elementer_med_fordeltelaster:
            q1, q2 = hent_q1_og_q2(element[0], fordelte_laster)
            skjaer = (q1 *x + ((q2 - q1)/(2*lengde))*x**2 - Q1)
        
        else:
            skjaer = x*0-Q1

        # Delplott for gjeldende element
        ax = axes[i // n, i % n]
        # Plotter skjær
        ax.plot(x, skjaer, color='blue')

        # Legger til linje på y=0
        ax.axhline(0, color='red', linestyle='--', label='y=0')
        ax.set_title(f'{element[0]}')

    # Juster layout for å unngå overlappende titler og etiketter.
    plt.tight_layout()
    plt.show()

def plot_normal(elementer, elementlengder, res, fordelte_laster):


    #plotter normalkraft for alle elementer

    n = int(np.sqrt(len(elementer))+1)
    fig, axes = plt.subplots(n, n, figsize=(10, 8))
    
    for i in range(len(elementer)):
        # Itererer gjennom alle elementene
        element = elementer[i]
        lengde = elementlengder[i]
        S = res[i]

        #Henter ut nødvendige verdier
        x = np.linspace(0, lengde, 1000)
        N1=S[0]

        # N konstant for alle element
        normal = x*0 + N1

        # Delplott for gjeldende element
        ax = axes[i // n, i % n]
        # Plotter skjær
        ax.plot(x, normal, color='blue')

        # Legger til linje på y=0
        ax.axhline(0, color='red', linestyle='--', label='y=0')
        ax.set_title(f'{element[0]}')

    # Juster layout for å unngå overlappende titler og etiketter.
    plt.tight_layout()
    plt.show()




