"""Contains all data structures required for the pathfinding algorithms.

Together, they are used to represent a directed graph with vertices (also known as 'nodes')
and edges. Each edge connects two vertices and has a cost, which might represent distance,
difficulty or any kind of rating (the higher, the less desireable the path).
"""
from __future__ import annotations


class Vertex:
    def __init__(self, name: str) -> None:
        """Initializes a Vertex object."""
        self.name = name
        self.adjacent_edges = set()
        self.visited = False

    def __lt__(self, other: Vertex) -> bool:
        """Less than comparison of two vertices."""
        return False

    def set_adjacent_edges(self, edges: set[Edge]) -> None:
        """Initializes all edges leading away from this vertex."""
        for edge in edges:
            if self == edge.start:
                self.adjacent_edges.add(edge)


class Edge:
    """Represents a directed edge between two vertices.

    Attributes:
        start: Vertex from which the edge leads away.
        end: Vertex towards which the edge leads.
        cost: Path costs of the respective edge.
    """
    def __init__(self, start: Vertex, destination: Vertex, cost: int) -> None:
        """Initialzes an Edge object."""
        self.start = start
        self.destination = destination
        self.cost = cost


class Graph:
    """Represents a weighted graph consisting of vertices and edges.

    Attributes
        vertices: List of all vertices the graph contains.
        edges: List of all edges the graph contains.
    """
    def __init__(self, vertices: set[Vertex], edges: set[Edge]) -> None:
        """Initializes a Graph object.

        Raises:
            ValueError: If start or destination of any edge in edges is not in vertices.
        """
        self.vertices = vertices

        for edge in edges:
            if edge.start not in self.vertices or edge.destination not in self.vertices:
                raise ValueError(
                    f'Edge {edge.start} to {edge.destination} contains a vertex that is not part of this graph.')

        self.edges = edges

        for vertex in self.vertices:
            vertex.set_adjacent_edges(self.edges)
