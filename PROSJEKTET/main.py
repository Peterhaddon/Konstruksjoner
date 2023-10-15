import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import plot
from readfromfile import readfromfile #bør dobbelsjekkes 
from I import I #MÅ DOBBELSJEKKES 



#Tester funksjoner:
file_path = 'PROSJEKTET/Inputfil2.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)

print('\nknutepunkter')
print(len(knutepunkter))
print(knutepunkter)
print('\nelementer')
print(len(elementer))
print(elementer)
# print('\npunktlaster')
# print(len(punktlaster))
# print(punktlaster)
# print('\nfordelte_laster')
# print(len(fordelte_laster))
# print(fordelte_laster)
# print('\npunktlaster')
# print(len(punktlaster))
# print(punktlaster)

#rør:
print(I(elementer[0])/(10**6))
#i-profil:
print(I(elementer[4])/(10**6))
#box:
print(I(elementer[2])/(10**6))

# Example usage
kp_koordinater, elementer_kp_til_kp = format_data(knutepunkter, elementer)
numbers = 1
first_index = 0

# Call the function with the provided random data
fig_init, ax_init, fig_def, ax_def = setup_plots()
plot_structure(ax_init, kp_koordinater, elementer_kp_til_kp, numbers, first_index)

# Display the plots
plt.show()
