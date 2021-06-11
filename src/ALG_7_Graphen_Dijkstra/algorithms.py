"""Contains the different variations of Dijktra's Algotithm for finding the shortest
path from a start vertex to a destination vertex in a directed graph.
"""
import heapq
from queue import PriorityQueue

from data_structures import Graph, Vertex


def dijkstra_lazy(graph: Graph, start: Vertex, destination: Vertex) -> None:
    """Dijktra's shortest path with priority queue.
    """
    count = 0
    queue = PriorityQueue()
    queue.put((0, count, start))
    visited = {start}
    came_from = {}

    costs = dict.fromkeys(graph.vertices, float('inf'))

    costs[start] = 0

    while not queue.empty():

        current = queue.get()[2]
        visited.remove(current)

        for edge in current.adjacent_edges:
            temp_distance = costs[current] + edge.cost

            if temp_distance < costs[edge.destination]:
                came_from[edge.destination] = current
                costs[edge.destination] = temp_distance

                if edge.destination not in visited:
                    count += 1
                    queue.put((costs[edge.destination], count, edge.destination))
                    visited.add(edge.destination)

    current = destination
    path = current.name

    while current in came_from:
        current = came_from[current]
        path = f'{current.name} -> {path}'

    print(f'Shortest Path: {path}')
    print(f'Distance: {costs[destination]}')


def dijkstra_eager(graph: Graph, start: Vertex, destination: Vertex) -> None:
    """Dijktra's shortest path with heapqueue.
    """
    heap = [(0, start)]
    visited = {start}
    came_from = {}

    costs = dict.fromkeys(graph.vertices, float('inf'))

    costs[start] = 0

    while heap:
        current = heapq.heappop(heap)[1]

        for edge in current.adjacent_edges:
            temp_distance = costs[current] + edge.cost

            if temp_distance < costs[edge.destination]:
                came_from[edge.destination] = current
                costs[edge.destination] = temp_distance

                if edge.destination not in visited:
                    heapq.heappush(heap, (costs[edge.destination], edge.destination))
                    visited.add(edge.destination)

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
