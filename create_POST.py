value = []

def addvalue():
    bands = input("Band ?\n").split()
    enb = input("eNB ?\n")
    region = input("Region ?\n")
    latlon = locinfo()
    try:
        pci = int(input("PCI base ?\n"))
    except ValueError:
        print("PCI doit être un entier.")
        return
    adresse = input("Addresse (A prendre sur le cadastre)\n")
    deg = degretantenne()
    for band in bands:
        id = return_base_id(band)
        earfcn = return_earfcn(band)
        if id is None or earfcn is None:
            print(f"Bande {band} non reconnue.")
            continue
        for i in range(3):
            value.append(f"4G;270;01;{id[i]};{region};{enb};{pci+i};{latlon};eNB ID {enb} - LTE Band {band_info(band)} - {deg[i]} - {adresse};{earfcn}")

def locinfo():
    lat = input("Latitude ?\n")
    lon = input("Longitude ?\n")
    return f"{lat};{lon}"

def degretantenne():
    list_dir = []
    for i in range(3):
        try:
            deg = int(input(f"Degret {i+1} ? (en °)\n"))
            list_dir.append(f"{deg}°")
        except ValueError:
            print("Le degré doit être un entier.")
            list_dir.append("0°")
    return list_dir

def band_info(band):
    band_info_map = {
        "1": "B1 - 2100 MHz",
        "3": "B3 - 1800 MHz",
        "7": "B7 - 2600 MHz",
        "20": "B20 - 800 MHz",
        "28": "B28 - 700 MHz"
    }
    return band_info_map.get(band, "Bande non reconnue")

def return_earfcn(band):
    earfcn_map = {
        "1": "75",
        "3": "1800",
        "7": "2850",
        "20": "6200",
        "28": "9360"
    }
    return earfcn_map.get(band)

def return_base_id(band):
    base_id_map = {
        "1": ["31", "32", "33"],
        "3": ["1", "2", "3"],
        "7": ["21", "22", "23"],
        "20": ["11", "12", "13"],
        "28": ["41", "42", "43"]
    }
    return base_id_map.get(band)

def save_in_file(addtofile):
    filename = "add.csv"
    with open(filename, "w", encoding="utf-8") as file:
        for value in addtofile:
            file.write(value + "\n")

def viewvalue(value):
    for val in value:
        print(f"{val}\n")

def main():
    global value
    choix = 0
    while choix != 3:
        print("1 - Add a new Value\n")
        print("2 - View the Current Value\n")
        print("3 - Write and Exit\n")
        try:
            choix = int(input("Choise\n"))
        except ValueError:
            print("Choix doit être un entier.")
            continue
        if choix == 1:
            addvalue()
        elif choix == 2:
            viewvalue(value)
        elif choix == 3:
            save_in_file(value)
            exit()
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
