import requests
import gzip
import shutil

filename="MLS-full-cell-export-final.csv" #It's a CSV file
#url_file="https://archive.org/download/Mozilla_Location_Services_Archive/Final%20Export/MLS-full-cell-export-final.csv.gz" #Hosted in Archive.org - No Expiration Date
url_file="https://voxhost.fr/MLS-full-cell-export-final.csv.gz" #Hosted in Cloudflare -No Expiration Date
#If you want to made a mirror without using the Archive.org link, you can use this link (https://www.mediafire.com/file/yxpdql0ebho4pc0/MLS-full-cell-export-final.csv.gz/file or https://pixeldrain.com/u/k1TNyYvv) and made a mirror of the file youself of a different hoster with direct link support
#Or you can use it localy if you have the file already downloaded in the same directory as this script
#just change the "localy" variable to True
localy=False

mmc, mnc =270,77 #Tango
cell2g, cell3g, cell4g= 0,0,0
to_export=[]
def download_file(url):
    print("Downloading file")
    with requests.get(url, stream=True) as r:
        total_length = r.headers.get('content-length')
        if total_length is None:  # no content length header
            with open("MLS-full-cell-export-final.csv.gz", "wb") as f:
                shutil.copyfileobj(r.raw, f)
        else:
            total_length = int(total_length)
            with open("MLS-full-cell-export-final.csv.gz", "wb") as f:
                downloaded = 0
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        done = int(50 * downloaded / total_length)
                        print(f"\r[{'=' * done}{' ' * (50-done)}] {done * 2}%", end='')
    print(f"\nDownloaded from {url}")

def extract_file():
    print("Extracting file")
    with gzip.open("MLS-full-cell-export-final.csv.gz", 'rb') as f_in:
        with open('MLS-full-cell-export-final.csv', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("Extracted")

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
        count=0
        with open(filename, 'r') as file:
            for line in file:
                check_carrier(line.strip())
                count+=1
                print(f"Check line {count}")
        return_data()   
    except FileNotFoundError:
        print(f"The file {filename} is not found")
    except IOError:
        print("An I/O Error occured")

download_file(url_file)
extract_file()
check(filename)
