import csv
import pandas as pd

names, links, set_names = [],{},{}
data = dict()
output = list()

file = open('scraped_data_sorted','r')
for line in file:
    name, link = line.split(' : ')
    names.append(name)
    links[name] = link.replace('\n','')
file.close()
set_names = set(names)

file = open('autores_sbbd','r')
for line in file:
    name = line[:-1]
    if name in set_names:
        output.append({'Nome' : name,
                       'Link' : links[name],
                       'Publicações no SBBD' : str(names.count(name))})
    else:
        output.append({'Nome' : name,
                       'Link' : '',
                       'Publicações no SBBD' : '0'})
file.close()

print('Nome,Link,Publicações no SBBD')
for row in output:
    print(row['Nome']+','+row['Link']+','+row['Publicações no SBBD'])