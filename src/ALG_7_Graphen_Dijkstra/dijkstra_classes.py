from __future__ import annotations


class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.adjacent_edges = set()
        self.visited = False

    def set_adjacent_edges(self, edges: set(Edge)) -> None:
        for edge in edges:
            if self == edge.start:
                self.adjacent_edges.add(edge)


class Edge:
    def __init__(self, start: Vertex, destination: Vertex, cost: int) -> None:
        self.start = start
        self.destination = destination
        self.cost = cost


class Graph:
    def __init__(self, vertices: set(Vertex), edges: set(Edge)) -> None:
        self.vertices = vertices
        for edge in edges:
            if edge.start not in self.vertices or edge.destination not in self.vertices:
                raise ValueError(
                    f'Edge {edge.start} to {edge.destination} contains a vertex that is not part of this graph.')
        self.edges = edges

        for vertex in self.vertices:
            vertex.set_adjacent_edges(self.edges)
