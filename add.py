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
    elif inp == 2:
        return "3G"
    elif inp == 3:
        return "4G"
    elif inp == 4:
        return "5G"
    elif inp == 5:
        return "CD2"

def Create4G(networktype):
    mmcmnc=mmcmnccreator()
    ci=input("Cell indentity ?\n")
    tac=input("Tracking Area Code ? (Region sur CM)n")
    eNB=input("eNB ?\n")
    pci=input("PCI ?\n")
    latlon=locinfo()
    earfcn=input("earfcn")
    address=input("Addresse (A prendre sur le cadastre)")
    type4G=input("Fréquence 4G")
    direction=input("Direction (S/N/E/O)")
    directiondeg=input("Direction en °")+"°"
    bp=input("Bande Passante en Hz")
    return networktype+';'+mmcmnc+";"+ci+";"+tac+";"+eNB+";"+pci+";"+latlon+";eNB ID "+eNB+" - LTE "+type4G+" - "+direction+" "+directiondeg+" - "+bp+" - "+address+";"+earfcn

def Create3G(networktype):
    mmcmnc=mmcmnccreator()
    ci=input("Cell indentity ?\n")
    lac=input("Location area code ? (Region sur CM)n")
    rnc=input("RNC ?\n")
    pcs=input("PCS ?\n")
    latlon=locinfo()
    arfcn=input("earfcn")
    address=input("Addresse (A prendre sur le cadastre)")
    type3G=input("Fréquence 3G")
    direction=input("Direction (S/N/E/O)")
    directiondeg=input("Direction en °")+"°"
    bp=input("Bande Passante en Hz")
    return networktype+';'+mmcmnc+";"+ci+";"+lac+";"+rnc+";"+pcs+";"+latlon+";"+"3G "+type3G+" - "+direction+" "+directiondeg+" - "+bp+" - "+address+";"+arfcn

def Create2G(networktype):
    mmcmnc=mmcmnccreator()
    ci=input("Cell indentity ?\n")
    lac=input("Location Area Code ? (Region sur CM)n")
    eNB="XXX"
    bsic=input("BSIC ?\n")
    latlon=locinfo()
    earfcn=input("ARFCN")
    address=input("Addresse (A prendre sur le cadastre)")
    type2G=input("Fréquence 3G")
    direction=input("Direction (S/N/E/O)")
    directiondeg=input("Direction en °")+"°"
    bp=input("Bande Passante en Hz")
    return networktype+';'+mmcmnc+";"+ci+";"+lac+";"+eNB+";"+bsic+";"+latlon+";"+"2G "+type2G+" - "+direction+" "+directiondeg+" - "+bp+" - "+address+";"+earfcn

def Create5G(networktype):
    mmcmnc=mmcmnccreator()
    ci=input("Cell indentity ?\n")
    tac=input("Tracking Area Code ? (Region sur CM)n")
    eNB="XXX"
    pci=input("PCI ?\n")
    latlon=locinfo()
    earfcn=input("ARFCN")
    address=input("Addresse (A prendre sur le cadastre)")
    type5G=input("Fréquence 5G")
    direction=input("Direction (S/N/E/O)")
    directiondeg=input("Direction en °")+"°"
    bp=input("Bande Passante en Hz")
    return networktype+";"+mmcmnc+";"+ci+";"+tac+";"+eNB+";"+pci+";"+latlon+";"+"5G NR "+type5G+" - "+direction+" "+directiondeg+" - "+bp+" - "+address+";"+earfcn

def mmcmnccreator(): #Retourne les mmc/mnc de chaque Opérateur Luxembourgeois ---> A Adapté pour votre cas
    global value
    print("Merci de choisir l'opérateur\n")
    print("1 - Tango") #27077
    print("2 - POST") #27001
    print("3 - Orange") #27099
    print("4 - Luxembourg Online (LOL)") #LOL est le diminutif de Luxembourg Online - 2705
    inp=int(input("Votre choix\n"))
    if inp == 1:
        return "270;77" #mmc;mnc
    elif inp == 2:
        return "270;01"
    elif inp == 3:
        return "270;99"
    elif inp == 4:
        return "270;05"
    else :
        save_in_file(value)
        exit()

def locinfo(): #Longitude/Latitude
    lat=input("Latitude (Coordonnée GPS A prendre sur le cadastre)\n")
    lon=input("Longitude (Coordonnée GPS A prendre sur le cadastre)\n")
    return str(lat)+";"+str(lon)
    

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