def read_input_file(file_path):

    #Tomme lister som skall fylles
    knutepunkter = []
    elementer = []
    fordelte_laster = []
    punktlaster = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            #Funksjonen krever at oppsettet av inputfil følger rekkefølgen

            if line.startswith('#Antall knutepunkt'):
                antall_knutepunkt = int(lines[i + 1])
                i += 2

            elif line.startswith('#Antall element'):
                antall_element = int(lines[i + 1])
                i += 2

            elif line.startswith('#KP-info i rekkefølge:'):
                i+=1 # Hopp over kommentarlinje
                for _ in range(antall_knutepunkt):
                        i += 1 
                        data = lines[i].strip().split(', ')
                        if len(data) == 4:
                            knutepunkt_info = [float(value) if value.replace('.', '', 1).isdigit() else value for value in data]
                            knutepunkter.append(knutepunkt_info)

            elif line.startswith('#Element-info i rekkefølge:'):
                i+=1 # Hopp over kommentarlinje
                for _ in range(antall_element):
                        i += 1  
                        data = lines[i].strip().split(', ')
                        if len(data) == 6:
                            element_info = [float(value) if value.replace('.', '', 1).isdigit() else value for value in data]
                            elementer.append(element_info)
                        elif len(data) == 8:
                            element_info = [float(value) if value.replace('.', '', 1).isdigit() else value for value in data]
                            elementer.append(element_info)
            
            elif line.startswith('#Antall fordelte laster:'):
                antall_fordelte_laster = int(lines[i + 1])
                i += 2

            elif line.startswith('#Info om de fordelte lastene i rekkefølge:'):
                i+=1 # Hopp over kommentarlinje
                for _ in range(antall_fordelte_laster):
                        i += 1  
                        data = lines[i].strip().split(', ')
                        if len(data) == 4:
                            fordelte_laster_info = [float(value) if value.replace('.', '', 1).isdigit() else value for value in data]
                            fordelte_laster.append(fordelte_laster_info)

            elif line.startswith('#Antall punktlaster:'):
                antall_punktlaster = int(lines[i + 1])
                i += 2

            elif line.startswith('#Info om punktlastene i rekkefølge:'):
                i+=1 # Hopp over kommentarlinje
                for _ in range(antall_punktlaster):
                        i += 1  
                        data = lines[i].strip().split(', ')
                        if len(data) == 4:
                            punktlaster_info = [float(value) if value.replace('.', '', 1).isdigit() else value for value in data]
                            punktlaster.append(punktlaster_info)

            else:
                    i += 1





    return knutepunkter, elementer, fordelte_laster, punktlaster

# Eksempel på bruk:
file_path = 'PROSJEKTET/Inputfil1.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = read_input_file(file_path)

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