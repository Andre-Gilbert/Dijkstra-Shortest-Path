"""Contains the different variations of Dijktra's Algotithm for finding the shortest
path from a start vertex to a destination vertex in a directed graph.
"""
import heapq
from queue import PriorityQueue

from data_structures import Graph, Vertex


def dijkstra_lazy(graph: Graph, start: Vertex, destination: Vertex) -> None:
    """Dijktra's shortest path with priority queue.

    Args:
        graph:
        start: The start vertex.
        destination: The destination vertex.

    Complexity:
        time: O(E*log(V))
        space: O(V^2)
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

    current = destination
    path = current.name

    while current in came_from:
        current = came_from[current]
        path = f'{current.name} -> {path}'

    print(f'Shortest Path: {path}')
    print(f'Distance: {costs[destination]}')


def dijkstra_eager(graph: Graph, start: Vertex, destination: Vertex) -> None:
    """Dijktra's shortest path with heapqueue.

    Args:
        graph:
        start: The start vertex.
        destination: The destination vertex.

    Complexity:
        time:
        space:
    """
    heap = [(0, start)]
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

                if edge.destination not in [tup[1] for tup in heap]:
                    heapq.heappush(heap, (costs[edge.destination], edge.destination))
                else:
                    # decrease key
                    for idx, tup in enumerate(heap):
                        if tup[1] == edge.destination:
                            heap[idx] = (temp_distance, tup[1])

    current = destination
    path = current.name

    while current in came_from:
        current = came_from[current]
        path = f'{current.name} -> {path}'

    print(f'Shortest Path: {path}')
    print(f'Distance: {costs[destination]}')


def a_star_search() -> None:
    """tbd"""
    pass
