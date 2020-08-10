import csv

with open('height-weight.csv',newline='') as rag:
    render = csv.reader(rag)
    fileData = list(render)
fileData.pop(0)
newData = []

for i in range(len(fileData)):
    number1 = fileData[i][1]
    newData.append(float(number1))

var1 = len(newData)
total = 0

for x in newData:
    total += x

mean = total/var1

print('The Mean = ' + str(mean))