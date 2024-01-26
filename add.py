#Adapter pour le réseau Luxembourgeois
print("-"*10+"\n")
print("Add a Value to NTM File\n")
print("-"*10+"\n")
value=[]

def menu():
    global value
    choix=0
    while choix != 3 :
        print("1 - Add a new Value\n")
        print("2 - View the Current Value\n")
        print("3 - Write and Exit\n")
        choix=int(input("Choise\n"))
        if choix == 1 or choix == 2 or choix == 3:
            if choix == 1:
                addvalue()
            elif choix == 2:
                viewvalue(value)
            else :
                save_in_file(value)
                exit()
    else :
        choix=0

def typeofnetwork():
    print("Please select the Type of network\n")
    print("1- GSM\n")
    print("2- WCDMA\n")
    print("3- LTE\n")
    print("4- NR\n")
    print("5- CDMA")
    inp=int(input("Choice the type of network\n"))
    if inp == 1:
        return "2G"
    if inp == 2:
        return "3G"
    if inp == 3:
        return "4G"
    if inp == 4:
        return "5G"
    if inp == 5:
        return "CD2"

def Create4G(networktype):
    ant=networktype+';'
    mmc=input("MMC?\n")
    mnc=input("MNC?\n")
    ci=input("Cell indentity ?\n")
    tac=input("Tracking Area Code ? (Region sur CM)n")
    eNB=input("eNB ?\n")
    pci=input("PCI ?\n")
    lat=input("Latitude (Coordonnée GPS A prendre sur le cadastre)")
    lon=input("Longitude (Coordonnée GPS A prendre sur le cadastre)")
    earfcn=input("earfcn")
    address=input("Addresse (A prendre sur le cadastre)")
    type4G=input("Fréquence 4G")
    direction=input("Direction (S/N/E/O)")
    directiondeg=input("Direction en °")+"°"
    bp=input("Bande Passante en Hz")
    loc="eNB ID "+eNB+" - LTE "+type4G+" - "+direction+" "+directiondeg+" - "+bp+" - "+address
    ant=ant+mmc+";"+mnc+";"+ci+";"+tac+";"+eNB+";"+pci+";"+lat+";"+lon+";"+loc+";"+earfcn
    return ant

def Create3G(networktype):
    ant=networktype+';'
    mmc=input("MMC?\n")
    mnc=input("MNC?\n")
    ci=input("Cell indentity ?\n")
    lac=input("Location area code ? (Region sur CM)n")
    rnc=input("RNC ?\n")
    pcs=input("PCS ?\n")
    lat=input("Latitude (Coordonnée GPS A prendre sur le cadastre)")
    lon=input("Longitude (Coordonnée GPS A prendre sur le cadastre)")
    arfcn=input("earfcn")
    address=input("Addresse (A prendre sur le cadastre)")
    type3G=input("Fréquence 3G")
    direction=input("Direction (S/N/E/O)")
    directiondeg=input("Direction en °")+"°"
    bp=input("Bande Passante en Hz")
    loc="3G "+type3G+" - "+direction+" "+directiondeg+" - "+bp+" - "+address
    ant=ant+mmc+";"+mnc+";"+ci+";"+lac+";"+rnc+";"+pcs+";"+lat+";"+lon+";"+loc+";"+arfcn
    return ant

def Create2G(networktype):
    ant=networktype+';'
    mmc=input("MMC?\n")
    mnc=input("MNC?\n")
    ci=input("Cell indentity ?\n")
    lac=input("Location Area Code ? (Region sur CM)n")
    eNB="XXX"
    bsic=input("BSIC ?\n")
    lat=input("Latitude (Coordonnée GPS A prendre sur le cadastre)")
    lon=input("Longitude (Coordonnée GPS A prendre sur le cadastre)")
    earfcn=input("ARFCN")
    address=input("Addresse (A prendre sur le cadastre)")
    type2G=input("Fréquence 3G")
    direction=input("Direction (S/N/E/O)")
    directiondeg=input("Direction en °")+"°"
    bp=input("Bande Passante en Hz")
    loc="2G "+type2G+" - "+direction+" "+directiondeg+" - "+bp+" - "+address
    ant=ant+mmc+";"+mnc+";"+ci+";"+lac+";"+eNB+";"+bsic+";"+lat+";"+lon+";"+loc+";"+earfcn
    return ant

def Create5G(networktype):
    ant=networktype+";"
    mmc=input("MMC?\n")
    mnc=input("MNC?\n")
    ci=input("Cell indentity ?\n")
    tac=input("Tracking Area Code ? (Region sur CM)n")
    eNB="XXX"
    pci=input("PCI ?\n")
    lat=input("Latitude (Coordonnée GPS A prendre sur le cadastre)")
    lon=input("Longitude (Coordonnée GPS A prendre sur le cadastre)")
    earfcn=input("ARFCN")
    address=input("Addresse (A prendre sur le cadastre)")
    type5G=input("Fréquence 5G")
    direction=input("Direction (S/N/E/O)")
    directiondeg=input("Direction en °")+"°"
    bp=input("Bande Passante en Hz")
    loc="5G NR "+type5G+" - "+direction+" "+directiondeg+" - "+bp+" - "+address
    ant=ant+mmc+";"+mnc+";"+ci+";"+tac+";"+eNB+";"+pci+";"+lat+";"+lon+";"+loc+";"+earfcn
    return ant

def mmcmnccreator(): #Retourne les mmc/mnc de chaque Opérateur Luxembourgeois ---> A Adapté pour votre cas
    inp=0
    while 1<= inp <=5:
        print("Merci de choisir l'opérateur\n")
        print("1 - Tango")
        print("2 - POST")
        print("3 - Orange")
        print("4 - Luxembourg Online (LOL)") #LOL est le diminutif de Luxembourg Online
        inp=int(input("Votre choix"))
    if inp == 1:
        return "270;77" #mmc;mnc
    elif inp == 2:
        return "270;01"
    elif inp == 3:
        return "270;99"
    elif inp == 4:
        return "270;05"

    

def addvalue():
    global value
    typenet=typeofnetwork()
    if typenet == "4G":
        antenna=Create4G(typenet)
        value+=[antenna]
    elif typenet == "3G":
        antenna=Create3G(typenet)
        value+=[antenna]
    elif typenet == "2G":
        antenna=Create2G(typenet)
        value+=[antenna]
    elif typenet == "5G":
        antenna=Create2G(typenet)
        value+=[antenna]

def save_in_file(addtofile):
    filename = "add.csv"
    with open(filename, "w") as file:
        for value in addtofile:
            file.write(str(value) + "\n")

def viewvalue(value):
    for i in range(len(value)):
        print(value[i]+"\n")

menu()