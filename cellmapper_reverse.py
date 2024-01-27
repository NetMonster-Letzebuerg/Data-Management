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
	print("|1 - Tango            |")
	print("|2 - Orange Luxembourg|")
	print("|3 - POST             |")
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