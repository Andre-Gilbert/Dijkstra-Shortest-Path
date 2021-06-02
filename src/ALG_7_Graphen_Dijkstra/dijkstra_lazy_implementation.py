"""A dijkstra shortest path lazy implementation."""
from dijkstra_classes import Edge, Graph, Vertex


def dijkstra_lazy(graph: Graph, start: Vertex, destination: Vertex) -> None:
    pass


if __name__ == "__main__":
    v_a = Vertex('A')
    v_b = Vertex('B')
    v_c = Vertex('C')
    v_d = Vertex('D')
    v_e = Vertex('E')
    vertices = {v_a, v_b, v_c, v_d, v_e}

    e_a_b = Edge(v_a, v_b, 4)
    e_a_c = Edge(v_a, v_c, 1)
    e_b_d = Edge(v_b, v_d, 1)
    e_c_b = Edge(v_c, v_b, 2)
    e_c_d = Edge(v_c, v_d, 5)
    e_d_e = Edge(v_d, v_e, 3)
    edges = {e_a_b, e_a_c, e_b_d, e_c_b, e_c_d, e_d_e}

    graph = Graph(vertices, edges)

    dijkstra_lazy(graph, v_a, v_e)
