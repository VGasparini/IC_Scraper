from json import load, dump

print('''---Assistente de Classificação---\n\nSerá apresentado as opções de equivalência.\nCaso não fora encontrado nada na busca, será sinalizado.\nCaso encontrou algo, será apresentado um ID, o nome do autor e o link\nCaso haja mais de uma correspondencia, inserir espaçado os IDs.\nExemplo: \n\nAndré Aráujo
      [0] - {'Andre Araujo': 'https://dblp.org/pid/177/1567'}
      [1] - {'André Araújo': 'https://dblp.org/pid/75/11283'}
      [2] - {'Andre A. Araujo': 'https://dblp.org/pid/170/3093'}

Caso as 3 opções estão corretas, inserir 0 1 2\n--------------------------''')

with open('extract_info.json') as file:
    data = load(file)

new_data = []
nulls = 0
for inst in data:
    name, op = inst.popitem()
    print('\n', name)
    if op == 'null':
        print('Sem correspondencia\n', '-'*10)
        nulls += 1
        print(f'Correspondencias nulas = {nulls}')
        continue

    for i, o in enumerate(op):
        print(f'[{i}] - {o}')

    idx = input('\n-> ')
    idx = [int(i) for i in idx.split()]
    tmp_data = []
    for i in idx:
        tmp_data.append(op[i])
    new_data.append({name: tmp_data})

with open('parsed.json', 'w') as file:
    dump(new_data, file, ensure_ascii=False)
