from json import load, dump

with open('dblp_api_return.json') as file:
    data = load(file)

new_data = []
nulls = 0
reject = []
names = []
for inst in data:
    name, op = inst.popitem()
    if op == 'null':
        reject.append({name: op})
    elif len(op) > 1:
        names.append(name)
        new_data.append({name: op})
with open('rejected_match.json', 'w') as file:
    dump(new_data, file, ensure_ascii=False)
with open('null_match.json', 'w') as file:
    dump(reject, file, ensure_ascii=False)
for name in names:
    print(name)
