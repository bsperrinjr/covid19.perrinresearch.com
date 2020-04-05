from sources import path, confirmed_US, confirmed_global, deaths_US, deaths_global, recovered_global
import csv
from flask import jsonify


def openData(filename):
    data = []
    with open(path+filename,newline='') as csvfile:
         reader = csv.reader(csvfile,delimiter=',',quotechar='|')
         for row in reader:
             data.append(row)
    return(data)


@app.route('/api/v1/confirmed', methods=['Get'])
def getUSConfirmed():
    data = openData(confirmed_US)
    
    #print(data[0][6],data[0][11:])
    #print(data[1][6],data[1][12:]) 
    
    jsonDataAr = []
    
    totalLoc = len(data) - 1
    numDates = len(data[0][11:])
    dates = data[0][11:]
    for i in range(totalLoc):
        tmpJson = {}
        for j in range(11):
           tmpJson[data[0][j]] = data[i+1][j]
        tmpJson['Dates'] = dates
        tmpJson['ConfirmedCount'] = [ int(x) for x in data[i+1][-numDates:]]
        jsonDataAr.append(tmpJson)
    
    jsonData = {
            'count': len(jsonDataAr),
            'data': jsonDataAr
            }

    return jsonify(jsonData) 
#print(jsonData)
