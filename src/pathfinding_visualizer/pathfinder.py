"""Pathfinder implements the pathfinding algorithms.

Given a grid, the start, and destination vertex
a path from start to destination can be found using these algorithms:
- Dijkstra's algorithm
- A* search algorithm
- Bidirectional search
- Breadth-first search
- Depth-first search
"""
import pygame
from queue import PriorityQueue, deque
from vertex import Vertex
from utils import AStarSearch, BidirectionalSearch, Path


class Pathfinder:
    """Class which implements the pathfinding algorithms."""

    @staticmethod
    def dijkstra(gui: object, grid: list[list[Vertex]], start: Vertex, destination: Vertex) -> bool:
        """Visualizes Dijkstra's algorithm."""
        count = 0
        queue = PriorityQueue()
        queue.put((0, count, start))
        visited = {start}
        came_from = {}
        costs = {vertex: float('inf') for row in grid for vertex in row}
        costs[start] = 0

        while not queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.get()[2]
            visited.add(current)

            if current == destination:
                Path.reconstruct(gui, grid, came_from, destination)
                start.make_start()
                return True

            for neighbor in current.neighbors:
                new_cost = costs[current] + 1
                if new_cost < costs[neighbor]:
                    came_from[neighbor] = current
                    costs[neighbor] = new_cost
                    if neighbor not in visited:
                        count += 1
                        queue.put((costs[neighbor], count, neighbor))
                        visited.add(neighbor)

            if current != start:
                current.make_visited()

            gui.draw(grid)

        return False

    @staticmethod
    def a_star_search(gui: object, grid: list[list[Vertex]], start: Vertex, destination: Vertex) -> bool:
        """Visualizes A* search."""
        count = 0
        queue = PriorityQueue()
        queue.put((0, count, start))
        visited = {start}
        came_from = {}
        g_score = {vertex: float('inf') for row in grid for vertex in row}
        g_score[start] = 0
        f_score = {vertex: float('inf') for row in grid for vertex in row}
        f_score[start] = AStarSearch.manhatten_distance(start, destination)

        while not queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.get()[2]
            visited.add(current)

            if current == destination:
                Path.reconstruct(gui, grid, came_from, destination)
                start.make_start()
                return True

            for neighbor in current.neighbors:
                new_g_score = g_score[current] + 1
                if new_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = new_g_score
                    f_score[neighbor] = new_g_score + AStarSearch.manhatten_distance(neighbor, destination)
                    if neighbor not in visited:
                        count += 1
                        queue.put((f_score[neighbor], count, neighbor))
                        visited.add(neighbor)

            if current != start:
                current.make_visited()

            gui.draw(grid)

        return False

    @staticmethod
    def bidirectional_search(gui: object, grid: list[list[Vertex]], start: Vertex, destination: Vertex) -> bool:
        """Visualizes bidirectional search."""
        queue_src = deque()
        queue_src.append(start)
        queue_dst = deque()
        queue_dst.append(destination)
        visited_src = {start}
        visited_dst = {destination}
        came_from_src = {}
        came_from_dst = {}
        intersection = -1

        while queue_src and queue_dst and intersection == -1:
            BidirectionalSearch.bfs(gui, grid, start, queue_src, visited_src, came_from_src)
            BidirectionalSearch.bfs(gui, grid, destination, queue_dst, visited_dst, came_from_dst)

            intersection = BidirectionalSearch.is_intersecting(visited_src, visited_dst)

            if intersection != -1:
                Path.reconstruct_bidirectional(gui, grid, came_from_src, came_from_dst, intersection.pop())
                start.make_start()
                destination.make_destination()
                return True

        return False

    @staticmethod
    def breadth_first_search(gui: object, grid: list[list[Vertex]], start: Vertex, destination: Vertex) -> bool:
        """Visualizes breadth-first search."""
        queue = deque()
        queue.append(start)
        visited = {start}
        came_from = {}

        while queue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.popleft()
            visited.add(current)

            if current == destination:
                Path.reconstruct(gui, grid, came_from, destination)
                start.make_start()
                return True

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    queue.append(neighbor)

            if current != start:
                current.make_visited()

            gui.draw(grid)

        return False

    @staticmethod
    def depth_first_search(gui: object, grid: list[list[Vertex]], start: Vertex, destination: Vertex) -> bool:
        """Visualizes depth-first search."""
        stack = []
        stack.append(start)
        visited = {start}
        came_from = {}

        while stack:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = stack.pop()
            visited.add(current)

            if current == destination:
                Path.reconstruct(gui, grid, came_from, destination)
                start.make_start()
                return True

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    stack.append(neighbor)

            if current != start:
                current.make_visited()

            gui.draw(grid)

        return False
