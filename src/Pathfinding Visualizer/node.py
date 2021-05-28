""""""
import pygame


class Node:
    """Class which represents a node (cell) in the grid.

    Attributes:
        row: Row of the node.
        col: Column of the node.
        x: x-Coordinate of the node in the grid.
        y: y-Coordinate of the node in the grid.
        width: Width of the node.
        neighbors: Neighbors of the node.
        total_rows: Total rows of the grid.
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
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = self.__WHITE
        self.width = width
        self.neighbors = []
        self.total_rows = total_rows

    def get_position(self) -> tuple[int, int]:
        """Returns the position of the node."""
        return self.row, self.col

    def is_closed(self):
        return self.color == self.__RED

    def is_open(self):
        return self.color == self.__GREEN

    def is_visiting(self):
        return self.color == self.__GREEN

    def is_wall(self) -> bool:
        """Checks whether the node is a wall."""
        return self.color == self.__BLACK

    def is_start(self):
        return self.color == self.__ORANGE

    def is_destination(self):
        return self.color == self.__CYAN

    def reset_node(self):
        self.color = self.__WHITE

    def make_start(self):
        self.color = self.__ORANGE

    def make_destination(self):
        self.color = self.__CYAN

    def visited(self):
        self.color = self.__RED

    def visiting(self):
        self.color = self.__GREEN

    def make_wall(self):
        self.color = self.__BLACK

    def make_path(self):
        self.color = self.__PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid: list[list[object]]) -> None:
        """Updates all neighbors of a node.

        Args:
            grid: The grid containing node objects.
        """
        self.neighbors = []

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
