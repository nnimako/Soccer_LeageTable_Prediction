from flask import Flask, render_template
import json
import csv

app = Flask(__name__)

with open('./Data/epl_prediction_table.json', 'r') as file:
     table_data = file.read()

@app.route('/')
def hello():
    with open('./Data/epl_prediction_table.csv') as csvfile:
         data = csv.reader(csvfile, delimiter=',')
         first_line = True
         details = []
         for row in data:
             if not first_line: 
                 # print("===========")
                 # print(row)
                 # print("===========")
                 if len(row)!=0:
                     
                     details.append({'Team_name': row[0], 'Points': row[1], 'Emblem_Location': row[2]})
             else:
                first_line = False
    # print(details)
    return render_template('build_epl_table.html', details=details)
 
if __name__ == '__main__':
  app.run(host='0.0.0.0')