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

            if line.startswith('#Antall knutepunkt'):
                antall_knutepunkt = int(lines[i + 1])
                i += 2

            elif line.startswith('#Antall element'):
                antall_element = int(lines[i + 1])
                i += 2
            
            elif line.startswith('#KP-info i rekkefølge:'):
                i+=1
                for _ in range(antall_knutepunkt):
                        i += 1  # Hopp over kommentarlinje
                        data = lines[i].strip().split(', ')
                        if len(data) == 4:
                            knutepunkt_info = [float(value) if value.replace('.', '', 1).isdigit() else value for value in data]
                            knutepunkter.append(knutepunkt_info)
            else:
                    i += 1


    return knutepunkter, elementer, fordelte_laster, punktlaster

# Eksempel på bruk:
file_path = 'PROSJEKTET/Inputfil1.txt'
knutepunkter, elementer, fordelte_laster, punktlaster = read_input_file(file_path)

print(knutepunkter)