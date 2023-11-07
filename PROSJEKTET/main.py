# importerer nødvendige biblotek
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# importerer funksjoner definert i andre filer
from plotStruktur import * 
from readfromfile import * 
from elementfunksjoner import *
from matriseoperasjoner import *
from plotKrefter import *


def main():

    # bestemmer variabler som er nødvendige for kjøring av funksjoner:
    file_path = 'PROSJEKTET/Inputfil_JACKET_2.txt'
    knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)
    kp_koordinater, elementer_kp_til_kp = format_data(knutepunkter, elementer)
    elementlengder = lengder(knutepunkter,elementer)
    gsm = global_stivhetsmatrise(knutepunkter, elementer, elementlengder)
    glv = global_lastvektor(knutepunkter, elementer, elementlengder, fordelte_laster, punktlaster)
    r = (løs_deformasjoner(gsm, glv))
    res = S_solve(knutepunkter, elementer, elementlengder, r, fordelte_laster)
    M_maks, N_maks = maks_krefter(elementer, elementlengder, res, fordelte_laster)
    rotasjoner = r[::3] #Henter ut rotasjoner for hvert knutepunkt

    # __AVKOMMENTER DET DU ØNSKER Å KJØRE NEDENFOR__






    #    # Print element og prosent av flyt
    print_prosent_flyt(elementer, elementlengder, res, fordelte_laster)

    #    # Plotter diagrammer:
    # plot_moment(elementer, elementlengder, res, fordelte_laster)
    # plot_skjaer(elementer, elementlengder, res, fordelte_laster)
    # plot_normal(elementer, elementlengder, res, fordelte_laster)

    #    # Printer array med [N1, Q1, M1, N2, Q2, M2] for alle elementer
    # print( np.round(res,2))

    #    # Plot Struktur: 
    # skalering = 1
    # numbers = 1
    # first_index = 0
    # fig_init, ax_init, fig_def, ax_def = setup_plots()
    # plot_structure_def(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index, skalering*rotasjoner)
    # fig_init, ax_init, fig_def, ax_def = setup_plots()
    # plot_structure(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index)
    # plt.show()

    return()

main()