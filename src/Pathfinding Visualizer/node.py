""""""
import pygame


class Node:
    """Class which represents a node (cell) in the grid.

    Attributes:
        neighbors: Neighbors of the node.
        __row: Row of the node.
        __col: Column of the node.
        __x: x-Coordinate of the node in the grid.
        __y: y-Coordinate of the node in the grid.
        __width: Width of the node.
        __total_rows: Total rows of the grid.
    """
    __RED = (255, 0, 0)
    __GREEN = (0, 255, 0)
    __WHITE = (255, 255, 255)
    __BLACK = (0, 0, 0)
    __PURPLE = (128, 0, 128)
    __ORANGE = (255, 165, 0)
    __CYAN = (0, 255, 255)

    def __init__(self, row: int, col: int, width: int, total_rows: int) -> None:
        """Initializes a node in the grid."""
        self.neighbors = []
        self.__row = row
        self.__col = col
        self.__x = row * width
        self.__y = col * width
        self.__color = self.__WHITE
        self.__width = width
        self.__total_rows = total_rows

    def get_position(self) -> tuple[int, int]:
        """Returns the position of the node."""
        return self.__row, self.__col

    # def is_closed(self):
    #    return self.__color == self.__RED

    # def is_open(self):
    #    return self.__color == self.__GREEN

    # def is_visiting(self):
    #    return self.__color == self.__GREEN

    def is_wall(self) -> bool:
        """Checks whether the node is a wall."""
        return self.__color == self.__BLACK

    def is_start(self):
        return self.__color == self.__ORANGE

    def is_destination(self):
        return self.__color == self.__CYAN

    def reset_node(self):
        """Resets the node."""
        self.__color = self.__WHITE

    def make_start(self):
        """Creates the start node."""
        self.__color = self.__ORANGE

    def make_destination(self):
        """Creates the end node."""
        self.__color = self.__CYAN

    def make_visited(self):
        """Visited node."""
        self.__color = self.__RED

    def make_visiting(self):
        """Currently visiting."""
        self.__color = self.__GREEN

    def make_wall(self):
        """Creates a wall."""
        self.__color = self.__BLACK

    def make_path(self):
        """Creates a path."""
        self.__color = self.__PURPLE

    def draw(self, window):
        """Draws the node."""
        pygame.draw.rect(window, self.__color, (self.__x, self.__y, self.__width, self.__width))

    def update_neighbors(self, grid: list[list[object]]) -> None:
        """Updates all neighbors of a node.

        Args:
            grid: The grid containing node objects.
        """
        self.neighbors = []

        # Node below
        if self.__row < self.__total_rows - 1 and not grid[self.__row + 1][self.__col].is_wall():
            self.neighbors.append(grid[self.__row + 1][self.__col])

        # Node above
        if self.__row > 0 and not grid[self.__row - 1][self.__col].is_wall():
            self.neighbors.append(grid[self.__row - 1][self.__col])

        # Node to the right
        if self.__col < self.__total_rows - 1 and not grid[self.__row][self.__col + 1].is_wall():
            self.neighbors.append(grid[self.__row][self.__col + 1])

        # Node to the left
        if self.__col > 0 and not grid[self.__row][self.__col - 1].is_wall():
            self.neighbors.append(grid[self.__row][self.__col - 1])

    def __lt__(self, other: object):
        """Less than comparison of two nodes."""
        return False
