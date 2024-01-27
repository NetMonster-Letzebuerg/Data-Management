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