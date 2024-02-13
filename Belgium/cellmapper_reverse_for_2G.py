import csv
import json
import os
import requests
import time
import random
socks5_proxies=[
	'',
]

def get_addr(lat,lon):
	#print(lat,lon)
	url = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}' #Use OpenStreetMap API
	response = requests.get(url)
	data = response.json()
	#print(data)
	adr=''
	if 'house_number' in data['address']:
		adr+=data["address"]["house_number"]+', '
	if 'road' in data['address']:
		adr+=data["address"]["road"]+', '
	if 'isolated_dwelling' in data['address']:
		adr+=data["address"]["isolated_dwelling"]+', '
	if 'village' in data['address']:
		if 'city' in data['address']:
			if data['address']["city"] != data["address"]["village"]:
				adr+=data["address"]["village"]+', '
	if 'postcode' in data["address"]:
		adr+="L-"+data["address"]["postcode"]+' '
	if 'city' in data['address']:
		adr+=data['address']['city']+', '
	adr+="Lëtzebuerg"
	return adr

def select_operator(): #Adapt for your country
	print("|"+"-"*21+"|")
	print("|Please select an ISP |")
	print("|"+"-"*21+"|")
	print("|1 - Proximus (00)			|")
	print("|2 - Proxiums (01)			|")
	print("|3 - Proxiums (04)			|")
	print("|4 - Orange Belgium			|")
	print("|5 - Base - Telenet			|")
	print("|"+"-"*21+"|")
	choix=int(input("|Please made a choice |\n|"+"-"*21+"|\n"))
	if choix == 1:
		return "0"
	elif choix == 2:
		return "1"
	elif choix == 3:
		return "4"
	elif choix == 4:
		return "10"
	elif choix == 5:
		return "20"

def convert_tech_to_freq(band): #Convert LTE Band into Data
	if band == 1 : #Utilisé par Tango
		return '1 FDD'
	elif band == -1:
		return "Unk Band"

def get_data_from_cm(site_id,mnc,region):
	url = f'https://api.cellmapper.net/v6/getTowerInformation?MCC=206&MNC={mnc}&Region={region}&Site={site_id}&RAT=GSM' #GSM pour la 2G
	#print(url)
	rnd_proxy_nb=random.randint(0,len(socks5_proxies))
	random_proxy = random.choice(socks5_proxies)
	print(f"Proxy utilisé : {random_proxy}")
	proxies = {
		'http': random_proxy,
		'https': random_proxy,
	}
	response = requests.get(url, proxies=proxies)
	data = response.json()
	#print(data)
	bsic_values = []
	cell_data = data['responseData']['cells']
	#print(cell_data.keys())
	ci_values = list(cell_data.keys())
	typeof2g_value = []
	if 'cells' in data['responseData']:
		cell_data = data['responseData']['cells']
		for cell_info in cell_data.values():
			typeof2g_value.append(str(cell_info.get('SubSystem', '-')))
			bsic_values.append(str(cell_info.get('BSIC','')))

	return bsic_values,ci_values,typeof2g_value


def json_to_csv(json_file,csv_file):
	print("Init")
	with open(json_file, 'r') as json_file: #On récup la data du fichier json
		data = json.load(json_file)
		total_entries = len(data['responseData'])
		
		with open(csv_file, 'a', newline='', encoding='utf-8') as csv_file:
			writer = csv.writer(csv_file, delimiter=';') #; car séparateur de netmonster
			mnc=select_operator()
			for index, entry in enumerate(data['responseData'], start=1):
				enb = entry.get('siteID')
				region = entry.get('regionID')
				bsic_values,ci_values,typeof2g_value = [], [], []
				bsic_values,ci_values,typeof2g_value = get_data_from_cm(enb,mnc,region)
				print("Récupération des info depuis l'API")
				if bsic_values and ci_values:
					print(f"Récupération OK pour {enb}")
				else :
					print(f"Aucune info dispo pour l'antenne en question ({enb})")
					continue
				sleep_time = random.uniform(1,2) #Pour éviter de PT l'API

				print(f"Traitement de l'antenne {index} sur {total_entries}")
				rat_val = "2G"
				mcc = "206"
				tac = entry.get('regionID', '')
				lat = entry.get('latitude', '')
				lon = entry.get("longitude", '')
				address = get_addr(lat,lon)
				print(f"Valeur commune de l'antenne {enb}: RAT={rat_val}, MCC={mcc}, MNC={mnc}, TAC={tac}, Lat={lat}, Lon={lon}, Address={address}")
				try :
					earfcn_value = entry.get('channels', [])
					for i in range(len(earfcn_value)):
						rowcom =str(typeof2g_value[i])+" - "+str(address)
						row_data=[rat_val, mcc, mnc, ci_values[i], tac, "", bsic_values[i], lat, lon, rowcom, earfcn_value[i]]
						writer.writerow(row_data)
						csv_file.flush()
				except Exception as e:
					print(f"CPT : {e}")
				print(f"{index} fait")
				print(f"Attente de {sleep_time:.2f} seconde")
				time.sleep(sleep_time)
	print("Finito")

if __name__ == "__main__":
	json_to_csv("data.json","operator.csv")
