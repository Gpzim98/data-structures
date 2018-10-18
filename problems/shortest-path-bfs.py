class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def get_vertex(self, vertex):
        return self.vertices[vertex]

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        s = ''
        for key in sorted(list(self.vertices.keys())):
            if self.vertices[key].distance == 0:
                continue
            elif self.vertices[key].distance == 9999:
                s += '-1 '
            else:
                s += str(self.vertices[key].distance) + ' '

        return s

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 6
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 6:
                        node_v.distance = node_u.distance + 6


q = input()
results = []
for i in range(0, int(q)):
    g = Graph()
    g.vertices = {}
    nodes_edges = input()
    nodes = nodes_edges[0]

    for i in range(1, int(nodes) + 1):
        g.add_vertex(Vertex(i))

    edges = nodes_edges[2]

    for i in range(0, int(edges)):
        edge = str(input()).split(' ')
        g.add_edge(int(edge[0]), int(edge[1]))

    start_vertex = g.get_vertex(int(input()))

    g.bfs(start_vertex)
    results.append(g.print_graph())

    del g

for res in results:
    print(res)
