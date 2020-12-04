import json
import csv

file = open('./Data/epl_prediction_table.json')
data = json.load(file)

with open('./Data/epl_prediction_table.csv') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	first_line = True
	details = []
	for row in data:
		if not first_line:
			print(row)
			if len(row) != 0:
				details.append({'Team_name': row[0], 'Points': row[1], 'Emblem_Location': row[2]})
		else:
			first_line = False
	print(details)
