"""Contains the different variations of Dijktra's Algorithm.

It supports a lazy and an eager version of dijkstra's shortest path.
Before you run the algorithms, you need to create a graph, and pass
the graph as an argument.

Lazy implementation:
    Rather than updating existing key's value in O(n), the lazy version
    inserts key-value pairs in O(log(n)) even if they already exist in our
    priority queue.

Eager implementation:
    The eager version avoids inserting duplicate key-value pairs.
"""
from heapq import heappop, heappush
from queue import PriorityQueue

from data_structures import Edge, Graph, Vertex


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

        # Destinaton reached
        if current == destination:
            reconstruct_path(came_from, destination, costs)
            return

        visited.add(current)

        # Check all neighbors
        for edge in current.adjacent_edges:
            if edge in visited: continue
            new_cost = costs[current] + edge.cost

            if new_cost < costs[edge.destination]:
                came_from[edge.destination] = current
                costs[edge.destination] = new_cost
                queue.put((costs[edge.destination], edge.destination))

    reconstruct_path(came_from, current, costs)


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
        min_value, current = heappop(heap)

        # Destinaton reached
        if current == destination:
            reconstruct_path(came_from, destination, costs)
            return

        visited.add(current)
        if costs[current] < min_value: continue

        # Check all neighbors
        for edge in current.adjacent_edges:
            if edge in visited: continue
            new_cost = costs[current] + edge.cost
            current_cost = costs[edge.destination]

            if new_cost < current_cost:
                came_from[edge.destination] = current
                costs[edge.destination] = new_cost

                if edge.destination not in heap_vertices:
                    heap_vertices.add(edge.destination)
                    heappush(heap, (costs[edge.destination], edge.destination))
                else:
                    decrease_key(heap, edge, costs[edge.destination], current_cost)

    reconstruct_path(came_from, current, costs)


def decrease_key(heap: list[tuple[int, Vertex]], edge: Edge, new_cost: int, current_cost: int) -> None:
    """Decrease a value of a vertex given a edge.

    Since the heapq module doesn't support a decrease key method
    with O(1) lookup, we iterate over the heap in O(V) as a workaround.

    Args:
        heap: An array of tuples containing the cost and vertex.
        edge: The current edge we're considering.
        new_cost: The new distance from vertex A to vertex B.
        current_cost: The current distance from vertex A to vertex B.
    """
    for i in range(len(heap)):
        if heap[i] == (current_cost, edge.destination):
            heap[i] = (new_cost, edge.destination)
            break

    swim(heap, 0, i)


def swim(heap: list[tuple[int, Vertex]], start_position: int, position: int) -> None:
    """Restore the heap invariant.

    Args:
        heap: An array of tuples containing the cost and vertex.
        start_position: The index of the root.
        position: The index of the updated tuple.
    """
    new_item = heap[position]

    while position > start_position:
        parent_position = (position - 1) >> 1
        parent = heap[parent_position]

        if new_item < parent:
            heap[position] = parent
            position = parent_position
            continue

        break

    heap[position] = new_item


def reconstruct_path(came_from: dict[Vertex, Vertex], current: Vertex, costs: dict[int, Vertex]) -> None:
    """Reconstruct the shortest path.

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
