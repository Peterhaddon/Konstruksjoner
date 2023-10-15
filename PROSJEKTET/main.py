import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from plot import format_data, setup_plots, plot_structure #ser ut til å fungere, mangler def_structure
from readfromfile import readfromfile #bør dobbelsjekkes når vi begynner med the real deal
from lengder import lengder #Må gjøres, se utdelt kode
from I import I #MÅ DOBBELSJEKKES 



#Tester funksjoner:
file_path = 'PROSJEKTET/Inputfil2.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)

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

# # TESTING
# kp_koordinater, elementer_kp_til_kp = format_data(knutepunkter, elementer)
# numbers = 1
# first_index = 0
# fig_init, ax_init, fig_def, ax_def = setup_plots()
# plot_structure(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index)
# plt.show()

# print(lengder(knutepunkter, elementer, len(elementer)))