import numpy as np
from readfromfile import readfromfile #bør dobbelsjekkes 
from I import I #MÅ DOBBELSJEKKES 



#Tester funksjoner:
file_path = 'PROSJEKTET/Inputfil1.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = readfromfile(file_path)

print('\nknutepunkter')
print(len(knutepunkter))
print(knutepunkter)
print('\nelementer')
print(len(elementer))
print(elementer)
print('\npunktlaster')
print(len(punktlaster))
print(punktlaster)
print('\nfordelte_laster')
print(len(fordelte_laster))
print(fordelte_laster)
print('\npunktlaster')
print(len(punktlaster))
print(punktlaster)

#rør:
print(I(elementer[1])/(10**6))
#i-profil:
print(I(elementer[20])/(10**6))
#box:
print(I(elementer[22])/(10**6))