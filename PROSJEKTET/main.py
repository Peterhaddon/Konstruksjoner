# importerer nødvendige biblotek
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# importerer funksjoner definert i andre filer
from plot import * #ser ut til å fungere, men mangler def_structure
from readfromfile import * 
from elementfunksjoner import *
from matriseoperasjoner import *
from plotKrefter import *



# bestemmer variabler som er nødvendige for testing av funksjoner:
file_path = 'PROSJEKTET/Inputfil4.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)
kp_koordinater, elementer_kp_til_kp = format_data(knutepunkter, elementer)
elementlengder = lengder(knutepunkter,elementer)
gsm = global_stivhetsmatrise(knutepunkter, elementer, elementlengder)
glv = global_lastvektor(knutepunkter, elementer, elementlengder, fordelte_laster, punktlaster)
r = (løs_deformasjoner(gsm, glv))
res = S_solve(knutepunkter, elementer, elementlengder, r, fordelte_laster)
M_maks, N_maks = maks_krefter(elementer, elementlengder, res, fordelte_laster)

# # __TESTING__

print("res:", np.round(res,10))

# print("glv:", glv)

element=elementer[0]



# plot_moment(elementer, elementlengder, res, fordelte_laster)
# plot_skjaer(elementer, elementlengder, res, fordelte_laster)
# plot_normal(elementer, elementlengder, res, fordelte_laster)

# print("res:", res)
# print("fordelte_laster:", fordelte_laster)
# print("punktlaster:", punktlaster)
# print("elementer:", elementer)
# print("elementlengder:", elementlengder )


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

# # # Plot:
# numbers = 1
# first_index = 0
# fig_init, ax_init, fig_def, ax_def = setup_plots()
# plot_structure(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index)
# plt.show()
