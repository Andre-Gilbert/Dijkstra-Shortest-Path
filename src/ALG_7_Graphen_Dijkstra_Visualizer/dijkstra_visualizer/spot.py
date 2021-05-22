""""""
from dijkstra_visualizer.util.colour import Colour


class Spot:
    """
    
    Attributes:
        x:
        y:
        row:
        col:
        width:
        colour:
    """
    def __init__(self, row: int, col: int, width: int) -> None:
        """Initializes a spot."""
        self.x = row * width
        self.y = col * width
        self.row = row
        self.col = col
        self.width = width
        self.colour = Colour._WHITE

    def get_position(self) -> tuple[int, int]:
        """"""
        return self.row, self.col

    def is_open(self) -> bool:
        return self.colour == Colour._GREEN

    def is_closed(self) -> bool:
        return self.colour == Colour._RED

    def is_wall(self) -> bool:
        return self.colour == Colour._BLACK

    def is_start(self) -> bool:
        return self.colour == Colour._ORANGE

    def is_destination(self) -> bool:
        return self.colour == Colour._TURQUOISE

    def create_wall(self) -> None:
        self.colour = Colour._BLACK

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

        return neighbours
