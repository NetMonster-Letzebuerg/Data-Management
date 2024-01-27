import json

list_band=[]

with open("data.json", 'r') as json_file:
	data = json.load(json_file)
	for index, entry in enumerate(data['responseData'], start=1):
		band = entry.get('bandNumbers')
		for i in range(len(band)):
			if band[i] not in list_band:
				list_band.append(band[i])

print(list_band)
print(type(list_band[1]))