# importerer nødvendige biblotek
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# importerer funksjoner definert i andre filer
from plot import * #ser ut til å fungere, men mangler def_structure
from readfromfile import * 
from elementfunksjoner import *
from matriseoperasjoner import *

# TO DO:

#  Dobbelsjekk at ALT(!) i matriseoperasjoner.py er riktig


# bestemmer variabler som er nødvendige for testing av funksjoner:
file_path = 'PROSJEKTET/Inputfil4.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)
kp_koordinater, elementer_kp_til_kp = format_data(knutepunkter, elementer)
antall_kp = len(knutepunkter)
elementlengder = lengder(knutepunkter,elementer)

# # __TESTING__

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

# #rør:
# print(I(elementer[0])/(10**6))
# #i-profil:
# print(I(elementer[3])/(10**6))
# #box:
# print(I(elementer[2])/(10**6))

# numbers = 1
# first_index = 0
# fig_init, ax_init, fig_def, ax_def = setup_plots()
# plot_structure(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index)
# plt.show()

# print(lengder(knutepunkter, elementer))

# print(np.round(global_stivhetsmatrise(knutepunkter, elementer, elementlengder),1))
# print(element_stivhetsmatrise(elementer[0], elementlengder))
# print(global_stivhetsmatrise(knutepunkter,elementer,elementlengder))
# print(np.round(trans_matrise(np.pi/2),1))
# print(trans_k(0,element_stivhetsmatrise(elementer[0], elementlengder)))

# print(element_stivhetsmatrise(elementer[0],elementlengder))

# print(lokal_lastvektor(elementlengder, elementer[0],fordelte_laster) - punktlaster_vec(knutepunkter, punktlaster))
# print(np.round(trans_lokal_lastvektor((np.pi/2),lokal_lastvektor(elementlengder, elementer[0],fordelte_laster)),1))
# print(global_lastvektor(knutepunkter,elementer, elementlengder, fordelte_laster, punktlaster))

gsm = global_stivhetsmatrise(knutepunkter, elementer, elementlengder)
glv = global_lastvektor(knutepunkter, elementer, elementlengder, fordelte_laster, punktlaster)
# gsm2 = stivhet(len(elementer),elementer, elementlengder, len(knutepunkter),knutepunkter,elementer)
# gsm3 = global_stivhetsmatrise2(knutepunkter, elementer, elementlengder)
# print((np.round(gsm)))
# print('gsm: ')
# print(gsm)
# print('glv: ')
# print(glv)
# print(np.linalg.det(element_stivhetsmatrise(elementer[0],elementlengder)))
# print(np.allclose(gsm, np.transpose(gsm))) #sjekker om symmetrisk
# print(element_stivhetsmatrise(elementer[0], elementlengder))
# print(løs_deformasjoner(gsm, glv))
# print(np.round(gsm/100000000))

# for n in range(len(knutepunkter)*3):
#         for m in range(len(knutepunkter)*3):
#             if n == m:
#                 print(gsm[n][m]) #printer diagonalen for å sjekke om det er positive verdier

# ll=lokal_lastvektor(elementlengder, elementer[0], fordelte_laster)
# print(ll)

# print(punktlaster)

# print(punktlaster_vec(knutepunkter, punktlaster))