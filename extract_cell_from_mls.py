filename="Yourfilename" #It's a CSV file
mmc, mnc =0,0
cell2g, cell3g, cell4g= 0,0,0
to_export=[]
def techno(cell):
    global cell2g, cell3g, cell4g
    if cell[:3] == "GSM":
        return "2g"
    elif cell[:4] == "UMTS":
        return '3g'
    elif cell[:3] == "LTE":
        return "4g"
    else :
        print(f"Not determined for {cell}")

def check_carrier(cell):
    global cell2g, cell3g, cell4g
    type_network=techno(cell)
    if type_network == "2g" or type_network == "4g":
        decal=4
    elif type_network == "3g":
        decal=5
    if cell[decal:decal+3] == mmc and cell[decal+4:decal+6] == mnc:
        to_export.append()
        if decal == 5:
            cell3g+=1
        else :
            if cell[decal] == "GSM,":
                cell2g+=1
            else :
                cell4g+=1

def return_data():
    with open("result.txt","w") as file:
        for line in to_export:
            file.write(f"{line}\n")
    print(f"Il y a {len(to_export)} towers")
    print(f"\nIl y a {cell2g} 2G Towers, {cell3g} 3G Towers, {cell4g} 4G Towers")

def check(filename):
    try :
        with open(filename, 'r') as file:
            for line in file:
                check_carrier(line.strip)
        return_data()   
    except FileNotFoundError:
        print(f"The file {filename} is not found")
    except IOError:
        print("An I/O Error occured")

check(filename)