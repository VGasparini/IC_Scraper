import json
from fuzzywuzzy import fuzz, process


def count_simple():
    with open('count.json', 'r') as file:
        data = json.load(file)

    only_names = []
    for item in data:
        only_names.append(item['name'])

    info = []
    for name in set(sorted(only_names)):
        info.append({name: only_names.count(name)})

    with open('count_simple.json', 'w') as file:
        file.write(json.dumps(info, ensure_ascii=False))


def count_complete():
    with open('count.json', 'r') as file:
        data = json.load(file)

    only_names = set()
    for item in data:
        only_names.add(item['name'])
    only_names = sorted(list(only_names))

    info = []
    for name in only_names:
        tmp_data = []
        cont = 0
        for inst in data:
            if name == inst['name']:
                url = inst['url']
                year = inst['year']
                category = inst['category']
                tmp_data.append({category: year})
                cont += 1
        info.append({
            'name': name,
            'url': url,
            'count': cont,
            'publishes': tmp_data
        })
        del tmp_data

    with open('count_complete.json', 'w') as file:
        file.write(json.dumps(info, ensure_ascii=False))


def correlation_duplicated():

    # Ref.: https://www.datacamp.com/community/tutorials/fuzzy-string-python

    with open('count.json', 'r') as file:
        data = json.load(file)

    only_names = set()
    for item in data:
        only_names.add(item['name'])
    only_names = sorted(list(only_names))

    correlation = []
    for name in only_names:
        only_names_tmp = only_names.copy()
        del only_names_tmp[only_names.index(name)]
        high = process.extract(name, only_names_tmp)
        correlation.append({name: high})

    with open('correlation.json', 'w') as file:
        file.write(json.dumps(correlation, ensure_ascii=False))


def correlation_selected_names():

    # Ref.: https://www.datacamp.com/community/tutorials/fuzzy-string-python

    with open('list_name', 'r') as file:
        to_seek = []
        for line in file:
            to_seek.append(line)
    to_seek.sort()

    with open('count.json', 'r') as file:
        data = json.load(file)

    only_names = set()
    for item in data:
        only_names.add(item['name'])
    only_names = sorted(list(only_names))

    correlation = []
    for name in to_seek:
        high = process.extract(name, only_names)
        tmp = [i[1] for i in high]
        highest = process.extractOne(name, tmp)
        exact = True if highest[0] == 100 else False
        correlation.append({name: high, 'exact': exact})

    with open('correlation_selected.json', 'w') as file:
        file.write(json.dumps(correlation, ensure_ascii=False))
