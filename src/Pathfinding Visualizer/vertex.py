"""A vertex which will be used for the pathfinding algorithms."""
from __future__ import annotations

import pygame


class Vertex:
    """Class which represents a vertex (cell) in the grid.

    Attributes:
        neighbors: Neighbors of the vertex.
        __color: Color of the vertex indicates its state.
        __row: Row of the vertex.
        __col: Column of the vertex.
        __x: x-Coordinate of the vertex.
        __y: y-Coordinate of the vertex.
        __width: Width of the vertex.
        __total_rows: Total rows of the grid.
    """
    __RED = (255, 0, 0)
    __WHITE = (255, 255, 255)
    __BLACK = (12, 53, 71)
    __YELLOW = (255, 254, 106)
    __GREEN = (50, 205, 50)
    __PURPLE = (178, 67, 255, 0.75)
    __LIGHT_BLUE = (0, 190, 218, 0.75)

    def __init__(self, row: int, col: int, width: int, total_rows: int) -> None:
        """Initializes a vertex in the grid."""
        self.neighbors = []
        self.__color = self.__WHITE
        self.__row = row
        self.__col = col
        self.__x = row * width
        self.__y = col * width
        self.__width = width
        self.__total_rows = total_rows

    def get_position(self) -> tuple[int, int]:
        """Returns the position of the vertex."""
        return self.__row, self.__col

    def is_wall(self) -> bool:
        """Checks if the vertex is a wall."""
        return self.__color == self.__BLACK

    def is_visited(self) -> bool:
        """Checks if the state of the vertex is visited."""
        return self.__color == self.__LIGHT_BLUE

    def is_visiting(self) -> bool:
        """Checks if the state of the vertex is visiting."""
        return self.__color == self.__PURPLE

    def is_path(self) -> bool:
        """Checks if the vertex belongs to the shortest path."""
        return self.__color == self.__YELLOW

    def reset_vertex(self) -> None:
        """Resets the vertex."""
        self.__color = self.__WHITE

    def make_start(self) -> None:
        """Creates the start vertex."""
        self.__color = self.__GREEN

    def make_destination(self) -> None:
        """Creates the destination vertex."""
        self.__color = self.__RED

    def make_visited(self) -> None:
        """Visited vertex."""
        self.__color = self.__LIGHT_BLUE

    def make_visiting(self) -> None:
        """Currently visiting vertex."""
        self.__color = self.__PURPLE

    def make_wall(self) -> None:
        """Creates a wall."""
        self.__color = self.__BLACK

    def make_path(self) -> None:
        """Creates a path."""
        self.__color = self.__YELLOW

    def draw(self, window: pygame.display) -> None:
        """Draws the vertex."""
        pygame.draw.rect(window, self.__color, (self.__x, self.__y, self.__width, self.__width))

    def update_neighbors(self, grid: list[list[Vertex]]) -> None:
        """Updates all neighbors of a vertex.

        Args:
            grid: The grid containing vertex objects.
        """
        self.neighbors = []

        # Vertex below
        if self.__row < self.__total_rows - 1 and not grid[self.__row + 1][self.__col].is_wall():
            self.neighbors.append(grid[self.__row + 1][self.__col])

        # Vertex above
        if self.__row > 0 and not grid[self.__row - 1][self.__col].is_wall():
            self.neighbors.append(grid[self.__row - 1][self.__col])

        # Vertex to the right
        if self.__col < self.__total_rows - 1 and not grid[self.__row][self.__col + 1].is_wall():
            self.neighbors.append(grid[self.__row][self.__col + 1])

        # Vertex to the left
        if self.__col > 0 and not grid[self.__row][self.__col - 1].is_wall():
            self.neighbors.append(grid[self.__row][self.__col - 1])

    def __lt__(self, other: Vertex):
        """Less than comparison of two vertices."""
        return False
