#importerer nødvendige biblotek
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

#importerer funksjoner definert i andre filer
from plot import * #ser ut til å fungere, men mangler def_structure
from readfromfile import * 
from elementfunksjoner import *
from matriseoperasjoner import *

#TO DO:

 # Dobbelsjekk at ALT(!) i matriseoperasjoner.py er riktig


#bestemmer variabler som er nødvendige for testing av funksjoner:
file_path = 'PROSJEKTET/Inputfil.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)
kp_koordinater, elementer_kp_til_kp = format_data(knutepunkter, elementer)
antall_kp = len(knutepunkter)
elementlengder = lengder(knutepunkter,elementer)

# __TESTING__

# print('\nknutepunkter')
# print(len(knutepunkter))
# print(knutepunkter)
# print('\nelementer')
# print(len(elementer))
# print(elementer)
# print('\npunktlaster')
# print(len(punktlaster))
# print(punktlaster)
# print('\nfordelte_laster')
# print(len(fordelte_laster))
# print(fordelte_laster)

#rør:
# print(I(elementer[0])/(10**6))
# #i-profil:
# print(I(elementer[4])/(10**6))
# #box:
# print(I(elementer[2])/(10**6))

# numbers = 1
# first_index = 0
# fig_init, ax_init, fig_def, ax_def = setup_plots()
# plot_structure(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index)
# plt.show()

# print(lengder(knutepunkter, elementer, len(elementer)))

# print(np.round(global_stivhetsmatrise(knutepunkter, elementer),1))
# print(np.round(trans_matrise(np.pi/2),1))
# print(trans_k(0,element_stivhetsmatrise(elementer[0])))

# print(element_stivhetsmatrise(elementer[0],elementlengder))

# print(lokal_lastvektor(elementer[0]))
# print(np.round(trans_lokal_lastvektor((np.pi/2),lokal_lastvektor(elementer[0])),1))
# print(global_lastvektor(knutepunkter,elementer))

# gsm = global_stivhetsmatrise(knutepunkter, elementer, elementlengder)
# glv = global_lastvektor(knutepunkter, elementer)
# print(løs_deformasjoner(gsm, glv))

ll=lokal_lastvektor(elementlengder, elementer[8], fordelte_laster)
print(ll)

print(punktlaster)

print(punktlaster_vec(elementlengder, elementer, punktlaster))