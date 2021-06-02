""""""
import pygame


class Vertex:
    """Class which represents a vertex (cell) in the grid.

    Attributes:
        neighbors: Neighbors of the vertex.
        __color: Color of the vertex indicates its state.
        __row: Row of the vertex.
        __col: Column of the vertex.
        __x: x-Coordinate of the vertex in the grid.
        __y: y-Coordinate of the vertex in the grid.
        __width: Width of the vertex.
        __total_rows: Total rows of the grid.
    """
    __RED = (255, 0, 0)
    __WHITE = (255, 255, 255)
    __BLACK = (12, 53, 71)
    __YELLOW = (255, 254, 106)
    __ORANGE = (255, 165, 0)
    __DARK_BLUE = (178, 67, 255, 0.75)
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
        """Checks whether the vertex is a wall."""
        return self.__color == self.__BLACK

    def color_visited(self):
        return self.__color == self.__LIGHT_BLUE

    def reset_node(self):
        """Resets the vertex."""
        self.__color = self.__WHITE

    def make_start(self):
        """Creates the start vertex."""
        self.__color = self.__ORANGE

    def make_destination(self):
        """Creates the end vertex."""
        self.__color = self.__RED

    def make_visited(self):
        """Visited vertex."""
        self.__color = self.__LIGHT_BLUE

    def make_visiting(self):
        """Currently visiting vertex."""
        self.__color = self.__DARK_BLUE

    def make_wall(self):
        """Creates a wall."""
        self.__color = self.__BLACK

    def make_path(self):
        """Creates a path."""
        self.__color = self.__YELLOW

    def draw(self, window):
        """Draws the vertex."""
        pygame.draw.rect(window, self.__color, (self.__x, self.__y, self.__width, self.__width))

    def update_neighbors(self, grid: list[list[object]]) -> None:
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

    def __lt__(self, other: object):
        """Less than comparison of two vertices."""
        return False
