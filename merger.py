import csv

dataset1=[]
dataset2=[]

with open('dwarf_planets.csv','r')as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset1.append(f)

with open('dataset_2_sorted.csv','r')as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset2.append(f)



header1=dataset1[0]
dwarf_planet_data1=dataset1[1:]

header2=dataset2[0]
dwarf_planet_data2=dataset2[1:]

headers=header1+header2

dwarf_planet_data=[]

for index,data_row in enumerate(dwarf_planet_data1):
    dwarf_planet_data.append(dwarf_planet_data1[index]+dwarf_planet_data2[index])

with open('main.csv', 'a+') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(dwarf_planet_data)

