from flask import Flask, render_template, jsonify, request
from sources import path, confirmed_US, confirmed_global, deaths_US, deaths_global, recovered_global
import csv

app = Flask(__name__)

@app.route("/test/")
def hello():
	return render_template('index.html')


def openData(filename):
    data = []
    with open(path+filename,newline='') as csvfile:
         reader = csv.reader(csvfile,delimiter=',',quotechar='|')
         for row in reader:
             data.append(row)
    return(data)


def getState(data,i,dates,numDates): 
    tmpJson = {}
    for j in range(11):
        tmpJson[data[0][j]] = data[i+1][j]
    tmpJson['Dates'] = dates
    tmpJson['ConfirmedCount'] = [ int(x) for x in data[i+1][-numDates:]]
    return tmpJson

@app.route('/api/v1/confirmed', methods=['Get'])
def getUSConfirmed():
    if 'state' in request.args:
        state = request.args['state'].replace('%20',' ')
    else:
        state = False

    data = openData(confirmed_US)
    
    jsonDataAr = []
    
    totalLoc = len(data) - 1
    numDates = len(data[0][11:])
    dates = data[0][11:]
    for i in range(totalLoc):
        if state:
            if state == data[i+1][6]:
                stateData = getState(data,i,dates,numDates)
                jsonDataAr.append(stateData)
        else:
            stateData = getState(data,i,dates,numDates)
#        tmpJson = {}
#        for j in range(11):
#           tmpJson[data[0][j]] = data[i+1][j]
#        tmpJson['Dates'] = dates
#        tmpJson['ConfirmedCount'] = [ int(x) for x in data[i+1][-numDates:]]
            jsonDataAr.append(stateData)
    
    jsonData = {
            'count': len(jsonDataAr),
            'data': jsonDataAr
            }

    return jsonify(jsonData) 

@app.route('/api/v1/options/<optType>', methods=['Get'])
def getOptions(optType):

    data = openData(confirmed_US)

    jsonDataAr = []

    if optType == 'states' or optType == 'state':
        column = 6
    if optType == 'locality' or optType == 'localities':
        column = data[0].index('Admin2')
    if optType == 'country' or optType == 'countries':
        column = 6 

    totalLoc = len(data) - 1
    for i in range(totalLoc):
        option = data[i+1][column]
        if option not in jsonDataAr:
            jsonDataAr.append(option)

    jsonData = {
            'count': len(jsonDataAr),
            'data': jsonDataAr
            }

    return jsonify(jsonData)

if __name__ == "__main__":
    MyApp.run()

