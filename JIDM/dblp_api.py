from requests import get
from json import loads, dump
from time import sleep

data = []
with open('rejected_names', 'r') as file:
    for line in file:
        name = line.replace('\n', '').replace(' ', '+')
        print(f'Getting {name} info')
        response = get(
            f'https://dblp.org/search/author/api?q={name}&format=json')
        response_data = loads(response.text)
        tmp_data = []
        try:
            for inst in response_data['result']['hits']['hit']:
                tmp_data.append({inst['info']['author']: inst['info']['url']})
        except:
            tmp_data = 'null'
        data.append({name.replace('+', ' '): tmp_data})
        sleep(1)

with open('rejected_names_expanded.json', 'w') as file:
    dump(data, file, ensure_ascii=False, sort_keys=True)
