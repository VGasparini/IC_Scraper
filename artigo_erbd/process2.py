import csv
import difflib as df
import jellyfish as jf

def load_data():
    names, links, base = [],{},[]

    file = open('scraped_data_sorted','r')
    for line in file:
        name, link = line.split(' : ')
        names.append(name)
        links[name] = link.replace('\n','')
    file.close()
    base = list(set(names))

    file = open('autores_sbbd','r')
    seek = []
    for line in file:
        name = line[:-1]
        seek.append(name)
    file.close()

    return base, seek

# Selecionando as N maiores semelhanças utilizando K cutoff
def get_N_similar(base, seek, N, K):
    output = []
    for name in seek:
        output.append([name,df.get_close_matches( name, base, n=N, cutoff=K )])
    return output

def rank_by_dist(base):
    print("Jaro (0~1) | Levenshtein (0~inf) | Damerau (0~inf)")
    for instance in base:
        print("--- %s ---" % instance[0])
        for similar in instance[1]:
            print("    %s: %.4f | %.4f | %.4f" % (similar,*rank(similar, instance[0])))
        print()

def rank(str_a, str_b):
    return jf.jaro_distance(str_a,str_b), jf.levenshtein_distance(str_a,str_b), jf.damerau_levenshtein_distance(str_a,str_b)


if __name__ == "__main__":
    base, seek = load_data()
    data = get_N_similar(base, seek, 5, 0.5)
    rank_by_dist(data)