#importerer nødvendige biblotek
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

#importerer funksjoner definert i andre filer
from plot import * #ser ut til å fungere, mangler def_structure
from readfromfile import readfromfile #bør dobbelsjekkes når vi begynner med the real deal
from lengder import lengder #Må gjøres, se utdelt kode
from global_stivhetsmatrise import global_stivhetsmatrise
from I import I #MÅ DOBBELSJEKKES 

#TO DO:
 # Diskretisering: få alle kp koordinater, nummerer de, elementnummer. kok?
 # lengder-funksjon
 # sjekk I funksjon opp mot kjente tverrsnitt
 # Lag stivhetsfunksjon: EI, lag også EI/L for lokal stivhetsmatrise
 # Fullfør global_stivhetsmatrise, test for en kjent oppgave så vi ser om d funker


#bestemmer variabler som er nødvendige for testing av funksjoner:
file_path = 'PROSJEKTET/Inputfil2.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)
kp_koordinater, elementer_kp_til_kp = format_data(knutepunkter, elementer)
antall_kp = len(knutepunkter)


# TESTING

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
# print(I(elementer[4])/(10**6))
# #box:
# print(I(elementer[2])/(10**6))

# numbers = 1
# first_index = 0
# fig_init, ax_init, fig_def, ax_def = setup_plots()
# plot_structure(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index)
# plt.show()

# print(lengder(knutepunkter, elementer, len(elementer)))

# print(global_stivhetsmatrise(elementer_kp_til_kp, antall_kp))