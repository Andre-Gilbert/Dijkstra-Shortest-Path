"""Contains the different variations of Dijktra's Algorithm.

It supports a lazy and an eager version of dijkstra's shortest path.
Before you run the algorithms, you need to create a graph, and pass
the graph as an argument.

Lazy implementation:
    Rather than updating existing key's value in O(n), the lazy version
    inserts key-value pairs in O(log(n)) even if they already exist in our
    priority queue.

Eager implementation:
    The eager version uses a heapq which avoids inserting duplicate key-value pairs.
"""
import heapq
from queue import PriorityQueue

from data_structures import Graph, Vertex


def dijkstra_lazy(graph: Graph, start: Vertex, destination: Vertex) -> None:
    """Dijktra's shortest path with priority queue.

    Args:
        graph: A graph with edges and vertices.
        start: The start vertex.
        destination: The destination vertex.
    """
    queue = PriorityQueue()
    queue.put((0, start))
    visited = set()
    came_from = {}

    costs = dict.fromkeys(graph.vertices, float('inf'))
    costs[start] = 0

    while not queue.empty():
        current = queue.get()[1]
        visited.add(current)

        for edge in current.adjacent_edges:
            if edge in visited:
                continue

            temp_distance = costs[current] + edge.cost

            if temp_distance < costs[edge.destination]:
                came_from[edge.destination] = current
                costs[edge.destination] = temp_distance
                queue.put((costs[edge.destination], edge.destination))

    __reconstruct_path(came_from, destination, costs)


def dijkstra_eager(graph: Graph, start: Vertex, destination: Vertex) -> None:
    """Dijktra's shortest path with heapqueue.

    Args:
        graph: A graph with edges and vertices.
        start: The start vertex.
        destination: The destination vertex.
    """
    heap = [(0, start)]
    heap_vertices = set()
    visited = set()
    came_from = {}

    costs = dict.fromkeys(graph.vertices, float('inf'))
    costs[start] = 0

    while heap:
        idx, current = heapq.heappop(heap)
        visited.add(current)

        if costs[current] < idx:
            continue

        for edge in current.adjacent_edges:
            if edge in visited:
                continue

            temp_distance = costs[current] + edge.cost

            if temp_distance < costs[edge.destination]:
                came_from[edge.destination] = current
                costs[edge.destination] = temp_distance

                if edge.destination not in heap_vertices:
                    heap_vertices.add(edge.destination)
                    heapq.heappush(heap, (costs[edge.destination], edge.destination))
                else:
                    # Since the heapq module doesn't support a decrease key method
                    # with O(1) lookup, we iterate over the heap in O(V) as a workaround.
                    for idx, tup in enumerate(heap):
                        if tup[1] == edge.destination and temp_distance < tup[0]:
                            heap[idx] = (temp_distance, tup[1])
                            heapq.heapify(heap)

    __reconstruct_path(came_from, destination, costs)


def __reconstruct_path(came_from: dict, current: Vertex, costs: dict) -> None:
    """Reconstructs the shortest path.

    Args:
        came_from: A dictionary containing the path to the destination.
        current: The current vertex we're considering.
        costs: A dictionary containing all of the costs.
    """
    print(f'Distance: {costs[current]}')
    path = current.name

    while current in came_from:
        current = came_from[current]
        path = f'{current.name} -> {path}'

    print(f'Shortest Path: {path}')
