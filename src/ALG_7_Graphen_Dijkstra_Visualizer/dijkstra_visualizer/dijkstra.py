""""""
from queue import PriorityQueue
from typing import Callable

import pygame

from dijkstra_visualizer.node import Node


class DijkstraVisualizer:
    """Class which implements the dijkstra visualizer.
    
    Attributes:
        destination: Destination node.
        start: Starting node.
        gap: The size of a node in the graph.
        rows: The number of rows in the graph.
        cols: The number of columns in the graph.
        width: The width of the GUI.
        graph: A 2D grid.
        window: The size of the graphical user interface.
    """
    _GREY = (128, 128, 128)
    _WHITE = (255, 255, 255)

    def __init__(self, rows: int, width: int) -> None:
        """Initializes the GUI."""
        if not isinstance(rows, int) or not isinstance(width, int):
            raise TypeError("Inputs must be integers.")

        self.destination = None
        self.start = None
        self.gap = width // rows
        self.rows = rows
        self.cols = rows
        self.width = width
        self.graph = self.__initialize_grid()
        self.window = pygame.display.set_mode((width, width))
        pygame.display.set_caption("Dijkstra Shortest Path Visualizer")

    def __initialize_grid(self) -> list[list[Node]]:
        """"""
        grid = []

        for row in range(self.rows):
            grid.append([])

            for col in range(self.cols):
                grid[row].append(Node(row, col, self.gap, row))

        return grid

    def dijkstra(self) -> bool:
        """"""
        visited = {node: False for row in self.graph for node in row}
        distance = {node: float("inf") for row in self.graph for node in row}
        distance[self.start] = 0
        came_from = {}
        queue = PriorityQueue()
        queue.put((0, self.start))

        while not queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.get()[1]

            if visited[current]:
                continue

            visited[current] = True

            if current == self.destination:
                self.reconstruct_path(came_from, current)
                return True

            if current != self.start:
                current.make_visited()

            for neighbour in current.neighbours:
                weight = 1

                if distance[current] + weight < distance[neighbour]:
                    came_from[neighbour] = current
                    distance[neighbour] = distance[current] + 1
                    queue.put((distance[neighbour], neighbour))

                elif neighbour != self.destination and neighbour != self.start and not visited[neighbour]:
                    neighbour.make_visiting()

            self.draw()

        return False

    def reconstruct_path(self, came_from: dict, current: Node) -> None:
        """"""
        while current in came_from:
            current = came_from[current]
            current.make_path()
            self.draw()

    def draw_grid(self) -> None:
        """Draws the grid lines."""
        for i in range(self.rows):
            pygame.draw.line(self.window, self._GREY, (0, i * self.gap), (self.width, i * self.gap))
            pygame.draw.line(self.window, self._GREY, (i * self.gap, 0), (i * self.gap, self.width))

    def draw(self) -> None:
        """"""
        self.window.fill(self._WHITE)

        for row in self.graph:
            for node in row:
                pygame.draw.rect(self.window, node.colour, (node.x, node.y, self.gap, self.gap))

        self.draw_grid()
        pygame.display.update()

    def get_clicked_position(self, position: tuple[int, int]) -> tuple[int, int]:
        """"""
        x, y = position
        row, col = x // self.gap, y // self.gap
        return row, col

    def handles_events(self) -> bool:
        """"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = self.get_clicked_position(position)
                node = self.graph[row][col]

                if not self.start and node != self.start:
                    self.start = node
                    self.start.make_start_node()

                elif not self.destination and node != self.destination:
                    self.destination = node
                    self.destination.make_destination_node()

                elif node != self.start and node != self.destination:
                    node.make_wall()

            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, col = self.get_clicked_position(position)
                node = self.graph[row][col]
                node.reset_node()

                if node == self.start:
                    self.start = None

                if node == self.destination:
                    self.destination = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for row in self.graph:
                        for node in row:
                            node.update_neighbours(self.graph)

                    self.dijkstra()

                if event.key == pygame.K_c:
                    self.start = None
                    self.destination = None
                    self.graph = self.__initialize_grid()
                    self.draw()

        return True

    def run(self) -> None:
        """"""
        while self.handles_events():
            self.draw()

        pygame.quit()
