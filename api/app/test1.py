from sources import path, confirmed_US, confirmed_global, deaths_US, deaths_global, recovered_global
import csv
import matplotlib
import matplotlib.pyplot as plt

print(path)

def getData(filename):
    data = []
    with open(path+filename,newline='') as csvfile:
         reader = csv.reader(csvfile,delimiter=',',quotechar='|')
         for row in reader:
             data.append(row)
    return(data)


data = getData(confirmed_US)

print(data[0][6],data[0][11:])
print(data[1][6],data[1][12:]) 

matplotlib.use('Agg')

totalLoc = len(data) - 1
numDates = len(data[0][11:])
dates = data[0][11:]
plt.figure(figsize=[12,8])
for i in range(totalLoc):
    label = '%s' % (data[i+1][5])
    #print(label)
    if data[i+1][6] == 'New York' and data[i+1][5] in ['New York','Rockland','Westchester','Dutchess']:
    #if  in ['New York','New Jersey','Connecticut','Rhode Island','Massachusettes']: 
        print(label)
        print(numDates)
        print(data[i+1][-numDates:])
        ydata = [ int(x) for x in data[i+1][-numDates:]]
        plt.plot(dates,ydata,label=label)

ax = plt.gca()
temp = ax.xaxis.get_ticklabels()
temp = list(set(temp) - set(temp[::7]))
for label in temp:
    label.set_visible(False)
plt.xticks(rotation=45)
plt.legend()
plt.savefig('tmp.png')
