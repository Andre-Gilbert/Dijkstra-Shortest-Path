from ALG_7_Graphen_Dijkstra.vertex import Vertex


class Edge:
    def __init__(self, start: Vertex, destination: Vertex, cost: int) -> None:
        self.start = start
        self.destination = destination
        self.cost = cost
