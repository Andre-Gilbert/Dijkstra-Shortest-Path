""""""
from queue import PriorityQueue

import pygame

from node import Node


class Pathfinder:
    """Class which implements the pathfinding algorithms.

    Attributes:
        __grid: A 2D array containing nodes.
        __start: The start node.
        __destination: The destination node.
    """
    def __init__(self, grid: list[list[Node]], start: Node, destination: Node) -> None:
        """Initializes the pathfinder."""
        self.__grid = grid
        self.__start = start
        self.__destination = destination

    def dijkstra(self, gui: object) -> bool:
        """Visualizes Dijkstra's shortest path algorithm.

        Args:
            gui: The grid object.

        Returns:
            True if the shortest path is found, False otherwise.
        """
        visited = {node: False for row in self.__grid for node in row}
        distance = {node: float("inf") for row in self.__grid for node in row}
        distance[self.__start] = 0
        came_from = {}
        queue = PriorityQueue()
        queue.put((0, self.__start))

        while not queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.get()[1]

            if visited[current]:
                continue

            visited[current] = True

            if current == self.__destination:
                self.__reconstruct_path(gui, came_from, self.__destination)
                self.__start.make_start()
                return True

            if current != self.__start:
                current.visited()

            for neighbor in current.neighbors:
                weight = 1

                if distance[current] + weight < distance[neighbor]:
                    came_from[neighbor] = current
                    distance[neighbor] = distance[current] + weight
                    queue.put((distance[neighbor], neighbor))

                elif neighbor != self.__destination and neighbor != self.__start and not visited[neighbor]:
                    neighbor.visiting()

            gui.draw(self.__grid)

        return False

    def a_star_search(self, gui: object) -> bool:
        """Visualizes the A* search algorithm.

        Args:
            gui: The grid object.

        Returns:
            True if the shortest path is found, False otherwise.
        """
        count = 0
        queue = PriorityQueue()
        queue.put((0, count, self.__start))

        g_score = {node: float("inf") for row in self.__grid for node in row}
        g_score[self.__start] = 0
        f_score = {node: float("inf") for row in self.__grid for node in row}
        f_score[self.__start] = self.__manhatten_distance(self.__start.get_position(),
                                                          self.__destination.get_position())

        open_set = {self.__start}
        came_from = {}

        while not queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.get()[2]
            open_set.remove(current)

            if current == self.__destination:
                self.__reconstruct_path(gui, came_from, self.__destination)
                self.__start.make_start()
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.__manhatten_distance(neighbor.get_position(),
                                                                                 self.__destination.get_position())

                    if neighbor not in open_set:
                        count += 1
                        queue.put((f_score[neighbor], count, neighbor))
                        open_set.add(neighbor)

                        if neighbor != self.__destination:
                            neighbor.visiting()

            # Redraw the grid
            gui.draw(self.__grid)

            if current != self.__start:
                current.visited()

        return False

    def __manhatten_distance(self, current: Node, destination: Node) -> int:
        """Computes the manhatten distance to the destination.

        Args:
            current: The current node we're considering.
            destination: The destination node.

        Returns:
            The absolute distance of the x-Coordinate and
            the y-Coordinate of the current node to the destination.
        """
        x1, y1 = current
        x2, y2 = destination
        return abs(x1 - x2) + abs(y1 - y2)

    def __reconstruct_path(self, gui: object, came_from: dict[Node, Node], current: Node) -> None:
        """Reconstructs the shortest path.

        Args:
            gui: The gui object.
            came_from: A dictionary containing the shortest path.
            current: The current node we're considering.
        """
        while current in came_from:
            current = came_from[current]
            current.make_path()
            gui.draw(self.__grid)