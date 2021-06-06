"""A dijkstra shortest path lazy implementation."""

from dijkstra_classes import Edge, Graph, Vertex


def dijkstra_lazy(graph: Graph, start: Vertex, destination: Vertex) -> None:
    costs = dict.fromkeys(graph.vertices, float('inf'))

    current_vertex = start
    current_vertex.visited = True
    costs[current_vertex] = 0

    path = [current_vertex]

    while not destination.visited:
        new_vertex_found = False
        for edge in current_vertex.adjacent_edges:
            if edge.cost == min(edge.cost for edge in current_vertex.adjacent_edges if not edge.destination.visited):
                new_vertex = edge.destination
                new_vertex_found = True
            new_cost = edge.cost + costs[current_vertex]
            if costs[edge.destination] > new_cost:
                costs[edge.destination] = new_cost

        if new_vertex_found:
            current_vertex = new_vertex
            current_vertex.visited = True
            path.append(current_vertex)
        else:
            min_cost = float('inf')
            for vertex in [vertex for vertex in graph.vertices if not vertex.visited]:
                if costs[vertex] < min_cost:
                    min_cost = costs[vertex]
                    current_vertex = vertex

            found_vertex = False
            i = 0
            while not found_vertex and i < len(path):
                for edge in path[i].adjacent_edges:
                    if edge.destination == current_vertex:
                        path = path[:i + 1]
                        found_vertex = True
                i += 1

            current_vertex.visited = True
            path.append(current_vertex)

    print(f'Shortest Path: {"".join([(vertex.name + " -> ") for vertex in path if vertex != path[-1]])}{path[-1].name}')
    print(f'Distance: {costs[destination]}')


if __name__ == "__main__":
    v_a = Vertex('A')
    v_b = Vertex('B')
    v_c = Vertex('C')
    v_d = Vertex('D')
    v_e = Vertex('E')
    v_f = Vertex('F')
    vertices = {v_a, v_b, v_c, v_d, v_e, v_f}

    e_a_b = Edge(v_a, v_b, 7)
    e_a_c = Edge(v_a, v_c, 9)
    e_a_f = Edge(v_a, v_f, 14)
    e_b_c = Edge(v_b, v_c, 10)
    e_b_d = Edge(v_b, v_d, 15)
    e_c_d = Edge(v_c, v_d, 11)
    e_c_f = Edge(v_c, v_f, 2)
    e_d_e = Edge(v_d, v_e, 6)
    e_f_e = Edge(v_f, v_e, 9)
    edges = {e_a_b, e_a_c, e_a_f, e_b_c, e_b_d, e_c_d, e_c_f, e_d_e, e_f_e}

    graph = Graph(vertices, edges)

    dijkstra_lazy(graph, v_a, v_e)
