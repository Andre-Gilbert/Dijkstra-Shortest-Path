from ALG_7_Graphen_Dijkstra.edge import Edge
from ALG_7_Graphen_Dijkstra.vertex import Vertex


class Graph:
    def __init__(self, vertices: set(Vertex), edges: set(Edge)) -> None:
        self.vertices = vertices
        for edge in edges:
            if edge.start not in self.vertices or edge.destination not in self.vertices:
                raise ValueError(
                    f'Edge {edge.start} to {edge.destination} contains a vertex that is not part of this graph.')
        self.edges = edges

        for vertex in self.vertices:
            vertex.set_adjacent_vertices(self.edges)

    def get_vertices(self) -> set(Vertex):
        return self.vertices
