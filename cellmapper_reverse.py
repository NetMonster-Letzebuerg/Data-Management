import csv
import json
import os
import requests
import time
import random

def get_addr(lat,lon):
	url = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}' #Use OpenStreetMap API
	response = requests.get(url)
	data = response.json()
	adr=''
	if 'house_number' in data['address']:
		adr+=data["address"]["house_number"]+', '
	if 'road' in data['address']:
		adr+=data["address"]["road"]+', '
	if 'isolated_dwelling' in data['address']:
		adr+=data["address"]["isolated_dwelling"]+', '
	if 'village' in data['address']:
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
	print("|1 - Tango			|")
	print("|2 - Orange Luxembourg|")
	print("|3 - POST			 |")
	print("|4 - Luxembourg Online|")
	print("|"+"-"*21+"|")
	choix=int(input("|Please made a choice |\n|"+"-"*21+"|\n"))
	if choix == 1:
		return "77"
	elif choix == 2:
		return "99"
	elif choix == 3:
		return "1"
	elif choix == 4:
		return "5"

def convert_tech_to_freq(band): #Convert LTE Band into Data
	if band == 20 : #Utilisé par Tango
		return '800Mhz B20'
	elif band == 3 : #Utilisé par Tango
		return '1800Mhz B3'
	elif band == 28 : #Utilisé par Tango
		return '700Mhz B28'
	elif band == 7 : #Utilisé par Tango
		return '2600Mhz B7'
	elif band == 1: #Utilisé par Tango
		return '2100Mhz B1'
	elif band == 8: #Utilisé par Tango
		return '900Mhz B8'
	elif band == -1:
		return "Unk Band"

def get_data_from_cm(site_id,mnc,region):
	url = f'https://api.cellmapper.net/v6/getTowerInformation?MCC=270&MNC={mnc}&Region={region}&Site={site_id}&RAT=LTE'
	response = requests.get()
	data = response.json()
	pci_values = []
	ci_values = list(data["cells"].keys())
	bw = []
	band = []
	if 'cells' in data['responseData']:
		cell_data = data['responseData']['cells']
		for cell_info in cells_data.values():
			pci_values.append(str(cell_info.get('PCI', '-')))
	if 'estimatedBandData' in data['responseData']:
		bd_data = data['responseData']['estimatedBandData']
		for i in range(len(bd_data)):
			if 'bandWidth' in bd_data[i]:
				if bd_data[i]['bandWidth'] == 0:
					bw.append("Unk BP")
				else :
					bw.append(str(int(bd_data[i]['bandWidth']))+"MHz")
			if 'bandNumber' in bd_data[i]:
				band.append(convert_tech_to_freq(bd_data[i]['bandNumber']))


	return pci_values, ci_values, bw, band


def json_to_csv(json_file,csv_file):
	print("Init")
	mnc=select_operator()
	with open(input_json_file, 'r') as json_file: #On récup la data du fichier json
		data = json.load(json_file)
		
		with open(output_csv_file, 'a', newline='', encoding='utf-8') as csv_file:
			writer = csv.writer(csv_file, delimiter=';') #; car séparateur de netmonster
			for index, entry in enumerate(data['responseData'], start=1):
				enb = entry.get('siteID')
				region = entry.get('regionID')
				pci_values, ci_values, bw, band = [], [], [], []
				print("Récupération des info depuis l'API")
				if pci_values and ci_values:
					print(f"Récupération OK pour {enb}")
					pci_values, ci_values, bw, band = get_data_from_cm(enc,mnc,region)
				else :
					print(f"Aucune info dispo pour l'antenne en question ({enb})")
					continue
				sleep_time = random.uniform(1,2) #Pour éviter de PT l'API

				print(f"Traitement de l'antenne {index} sur {total_entries}")
				rat_val = entry.get('RAT', '').replace('LTE', '4G')
				mcc = "270"
				tac = entry.get('regionID', '')
				lat = entry.get('latitude', '')
				lon = entry.get("lontitude", '')
				address = get_addr(lat,lon)
				print(f"Valeur commune de l'antenne {enb}: RAT={rat_value}, MCC={mcc}, MNC={mnc}, TAC={tac}, Lat={lat}, Lon={lon}, Address={address}")
				try :
					earfcn_value = entry.get('channels', [])
					for i in range(len(earfcn_value)):
						rowcom ='eNB ID '+str(enb)+" - LTE "+str(band[i])" - BP "+str(bw[i])+" - "+str(address)
						row_data[rat_val, mmc, mnc, ci_values[i], tac, enb, pci_values[i], lat, lon, rowcom, earfcn_value[i]]
						writer.writerow(row_data)
						csv_file.flush()
						pci_cellid_file.flush()
						print(f"{index} fait")
				except Exception as e:
					print(f"CPT : {e}")

				print(f"Attente de {sleep_time.2f} seconde")
				time.sleep(sleep_time)
	print("Finito")

if __name__ == "__main__":
	json_to_csv("data.json","tango.csv")