import json


class Edge:
    def __init__(self, u, v, category=''):
        self.u = u
        self.v = v
        self.category = category

    def __str__(self):
        return str(self.u) + '--' + str(self.v) + (f'[ label={self.category}];' if self.category else '') + ';'


class Vertex:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ' "' + self.name + '" '


class Subgraph:
    def __init__(self, name, mode, id):
        self.name = name
        self.id = id
        self.mode = mode
        self.edges = []

    def __str__(self):
        graph = ''
        prefix = f'{self.mode} cluster_{self.id} ' + \
            '{\nlabel = ' + f'"{self.name}";'
        for edge in self.edges:
            graph += '\n'+str(edge)
        sufix = '}'
        return prefix + graph + sufix

    def add_edge(self, edge):
        self.edges.append(edge)


class Graph:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.subgraphs = []
        self.style = ''

    def set_style(self, style):
        self.style = style

    def __str__(self):
        graph = ''
        prefix = f'{self.mode} G ' + '{\n' + f'{self.style}\n'
        for subgraph in self.subgraphs:
            graph += '\n'+str(subgraph)
        sufix = '}'
        return prefix + graph + sufix

    def add_subgraph(self, subgraph):
        self.subgraphs.append(subgraph)


with open('data/raw/conference.json', 'r') as file:
    data = json.load(file)

for conference in data:
    name = conference['name']
    url = conference['url']
    year = conference['year']
    publishes = conference['data']
    conference_vertex = Vertex(year)
    graph = Graph(name, 'graph')
    graph.set_style('rankdir=LR')
    for publishe in publishes:
        p_name = publishe['name']
        cluster = Subgraph(p_name, 'subgraph', len(graph.subgraphs))
        p_category = publishe['category']
        p_authors = [list(author.keys())[0]
                     for author in publishe['authors']]
        for author in p_authors:
            p_vertex = Vertex(author)
            cluster.add_edge(Edge(conference_vertex, p_vertex))
        graph.add_subgraph(cluster)

with open('data/parsed/graph.dot', 'w') as file:
    file.write(str(graph))
