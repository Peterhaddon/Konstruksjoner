# importerer nødvendige biblotek
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# importerer funksjoner definert i andre filer
from plot import * #ser ut til å fungere, men mangler def_structure
from readfromfile import * 
from elementfunksjoner import *
from matriseoperasjoner import *



# bestemmer variabler som er nødvendige for testing av funksjoner:
file_path = 'PROSJEKTET/Inputfil4.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)
kp_koordinater, elementer_kp_til_kp = format_data(knutepunkter, elementer)
elementlengder = lengder(knutepunkter,elementer)
gsm = global_stivhetsmatrise(knutepunkter, elementer, elementlengder)
glv = global_lastvektor(knutepunkter, elementer, elementlengder, fordelte_laster, punktlaster)
r = (løs_deformasjoner(gsm, glv))
res = S_solve(knutepunkter, elementer, elementlengder, r, fordelte_laster)


# # __TESTING__

print(res)

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

# #Plot:
# numbers = 1
# first_index = 0
# fig_init, ax_init, fig_def, ax_def = setup_plots()
# plot_structure(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index)
# plt.show()
