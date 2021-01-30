import json

with open(input()) as file:
    data = json.load(file)

names, links = [], []
for inst in data:
    name, link = inst.popitem()
    names.append(name)
    links.append(link)

print(names)

print('---')

print(links)
