""""""
import pygame


class Node:
    """Class node which represents a cell in the grid.
    
    Attributes:
        x:
        y:
        row:
        col:
        width:
        colour:
        neighbours:
        total_rows:
    """
    _WHITE = (255, 255, 255)
    _RED = (255, 0, 0)
    _GREEN = (0, 255, 0)
    _BLUE = (0, 0, 255)
    _YELLOW = (255, 255, 0)
    _BLACK = (0, 0, 0)
    _PURPLE = (128, 0, 128)
    _ORANGE = (255, 165, 0)
    _GREY = (128, 128, 128)
    _CYAN = (0, 255, 255)

    def __init__(self, row: int, col: int, width: int, total_rows: int) -> None:
        """Initializes a node."""
        self.x = row * width
        self.y = col * width
        self.row = row
        self.col = col
        self.width = width
        self.colour = self._WHITE
        self.neighbours = []
        self.total_rows = total_rows

    def get_position(self) -> tuple[int, int]:
        """"""
        return self.row, self.col

    def is_open(self) -> bool:
        return self.colour == self._GREEN

    def is_closed(self) -> bool:
        return self.colour == self._RED

    def is_wall(self) -> bool:
        return self.colour == self._BLACK

    def is_start_node(self) -> bool:
        return self.colour == self._ORANGE

    def is_destination_node(self) -> bool:
        return self.colour == self._TURQUOISE

    def make_start_node(self) -> None:
        self.colour = self._ORANGE

    def make_destination_node(self) -> None:
        self.colour = self._CYAN

    def make_wall(self) -> None:
        self.colour = self._BLACK

    def make_path(self) -> None:
        """"""
        self.colour = self._PURPLE

    def make_visited(self) -> None:
        """"""
        self.colour = self._RED

    def make_visiting(self) -> None:
        """"""
        self.colour = self._GREEN

    def reset_node(self) -> None:
        """"""
        self.colour = self._WHITE

    def draw(self, window) -> None:
        """"""
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid: list[list[object]]) -> list[list[object]]:
        """"""
        neighbours = []

        # Bottom neighbour
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():  # DOWN
            neighbours.append(grid[self.row + 1][self.col])

        # Top neighbour
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():  # UP
            neighbours.append(grid[self.row - 1][self.col])

        # Right neighbour
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():  # RIGHT
            neighbours.append(grid[self.row][self.col + 1])

        # Left neighbour
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            neighbours.append(grid[self.row][self.col - 1])
