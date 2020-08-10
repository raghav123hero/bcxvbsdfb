import csv

with open('height-weight.csv',newline='') as rag:
    reader = csv.reader(rag)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    number = fileData[i][1]
    newData.append(number)

var1 = len(newData)
newData.sort()

if var1 %2 == 0:
    median1 = float(newData[var1//2])
    median2 = float(newData[var1//2-1])
    median = (median1 + median2)/2

else:
    median = newData[var1//2]


print('The median = ' + str(median))