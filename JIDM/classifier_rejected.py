from json import load, dump

with open('exact_match.json') as file:
    data_exact = load(file)
with open('null_match.json') as file:
    data_null = load(file)
with open('dblp_api_return.json') as file:
    data = load(file)

names_used = []
for d in data_exact:
    a, b = d.popitem()
    names_used.append(a)
for d in data_null:
    a, b = d.popitem()
    names_used.append(a)

reject = []
for inst in data:
    name, op = inst.popitem()
    if name not in names_used:
        reject.append(name)
for name in reject:
    print(name)
