from json import load, dump

with open('parsed.json') as file:
    data = load(file)

new_data = []
for inst in data:
    name, op = inst.popitem()

    tmp_data = []
    for o in op:
        a, b = o.popitem()
        new_data.append(name)

with open('final.json', 'w') as file:
    dump(new_data, file, ensure_ascii=False)
