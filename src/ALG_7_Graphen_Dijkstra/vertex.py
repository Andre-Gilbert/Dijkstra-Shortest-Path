from ALG_7_Graphen_Dijkstra.edge import Edge


class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.adjacent_vertices = set()

    def set_adjacent_vertices(self, edges: set(Edge)) -> None:
        for edge in edges:
            if self == edge.start:
                self.adjacent_vertices.add(edge.destination)
