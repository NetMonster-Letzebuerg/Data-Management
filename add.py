#Adapter pour le réseau Luxembourgeois
print("-"*10+"\n")
print("Add a Value to NTM File\n")
print("-"*10+"\n")
value=[]

def menu():
    choix=0
    while choix != 3 :
        print("1 - Add a new Value\n")
        print("2 - View the Current Value\n")
        print("3 - Write and Exit\n")
        choix=input("Choise")
        if choix == 1 or choix == 2 or choix == 3:
            if choix == 1:
                addvalue()
            elif choix == 2:
                viewvalue()
            else :
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
    inp=input("Choice the type of network\n")
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

def addvalue():
    global value
    typenet=typeofnetwork()
    if typenet == "4G":
        antenna=Create4G(typenet)
        value+=[antenna]