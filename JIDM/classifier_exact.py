from json import load, dump

with open('dblp_api_return.json') as file:
    data = load(file)

new_data = []
nulls = 0
reject = []
for inst in data:
    name, op = inst.popitem()
    if op == 'null':
        continue

    if len(op) == 1:
        print(name, '\n', op)
        if input():
            a, b = op[0].popitem()
            new_data.append({name: b})
    else:
        reject.append({name: op})
with open('exact_match.json', 'w') as file:
    dump(new_data, file, ensure_ascii=False)
with open('rejected.json', 'w') as file:
    dump(reject, file, ensure_ascii=False)
