

class Vertice(object):
    name = ''
    visited = None
    distance_source = 0
    neighbours = []

    def __init__(self, name):
        self.name = name


class Graph(object):
    vertices = {}

    queue = []

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.neighbours.append(v)
                if key == v:
                    value.neighbours.append(u)
            return True
        else:
            return False

    def bfs(self, vertice):
        self.queue = []

        start = Vertice(self.vertices[vertice])

        start.distance_source = 0
        start.visited = True

        for n in start.neighbours:
            # First error
            self.vertices[n].distance = start.distance_source + 1
            self.queue.append(n)

        while self.queue:
            # Second error
            current = self.queue.pop(0)
            current_vertice = Vertice(self.vertices[current])
            current_vertice.visited = True

            for neighb in current_vertice.neighbours:
                currents_neighb = Vertice(self.vertices[neighb])

                if not currents_neighb.visited:
                    self.queue.append(neighb)

                    if currents_neighb.distance_source > current_vertice.distance_source + 1:
                        currents_neighb.distance_source = current_vertice.distance_source + 1

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " + str(
                self.vertices[key].distance))


g = Graph()

for letter in range(ord('A'), ord('K')):
    g.vertices[chr(letter)] = (Vertice(chr(letter)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
    g.add_edge(edge[0], edge[1])


g.bfs('A')
g.print_graph()