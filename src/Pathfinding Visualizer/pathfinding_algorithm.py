""""""
from queue import PriorityQueue

import pygame

from node import Node


class Pathfinder:
    """Class

    Attributes:
        grid:
        start: The start node.
        destination: The destination node.
    """
    def __init__(self, grid: list[list[Node]], start: Node, destination: Node) -> None:
        """Initializes the pathfinder."""
        self.__grid = grid
        self.__start = start
        self.__destination = destination

    def dijkstra(self, gui: object) -> bool:
        """Visualizes Dijkstra's shortest path algorithm."""
        visited = {node: False for row in self.__grid for node in row}
        distance = {node: float("inf") for row in self.__grid for node in row}
        distance[self.__start] = 0
        came_from = {}
        priority_queue = PriorityQueue()
        priority_queue.put((0, self.__start))

        while not priority_queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = priority_queue.get()[1]

            if visited[current]:
                continue

            visited[current] = True

            if current == self.__destination:
                self.__reconstruct_path(gui, came_from)
                return True

            if current != self.__start:
                current.makeVisited()

            for neighbor in current.neighbors:
                weight = 1

                if distance[current] + weight < distance[neighbor]:
                    came_from[neighbor] = current
                    distance[neighbor] = distance[current] + weight
                    priority_queue.put((distance[neighbor], neighbor))

                elif neighbor != self.__destination and neighbor != self.__start and not visited[neighbor]:
                    neighbor.makeVisiting()

            gui.draw(self.__grid)

        return False

    def a_star_search(self, gui: object) -> bool:
        """Visualizes the A* search algorithm."""
        count = 0
        priority_queue = PriorityQueue()
        priority_queue.put((0, count, self.__start))
        came_from = {}
        g_score = {node: float("inf") for row in self.__grid for node in row}
        g_score[self.__start] = 0
        f_score = {node: float("inf") for row in self.__grid for node in row}
        f_score[self.__start] = self.__heuristic(self.__start.get_position(), self.__destination.get_position())
        open_set = {self.__start}

        while not priority_queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = priority_queue.get()[2]
            open_set.remove(current)

            if current == self.__destination:
                self.__reconstruct_path(gui, came_from)
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1
                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = (temp_g_score +
                                         self.__heuristic(neighbor.get_position(), self.__destination.get_position()))
                    if neighbor not in open_set:
                        count += 1
                        priority_queue.put((f_score[neighbor], count, neighbor))
                        open_set.add(neighbor)
                        if neighbor != self.__destination:
                            neighbor.visiting()

            gui.draw(self.__grid)
            if current != self.__start:
                current.visited()

        return False

    def __heuristic(self, start, end) -> int:
        """"""
        x1, y1 = start
        x2, y2 = end
        return abs(x1 - x2) + abs(y1 - y2)

    def __reconstruct_path(self, gui: object, came_from: dict[Node, Node]) -> None:
        """Reconstructs the shortest path."""
        while self.__destination in came_from:
            current = came_from[self.__destination]
            current.make_path()
            gui.draw(self.__grid)
