""""""
from queue import PriorityQueue

from dijkstra_visualizer.spot import Spot


class Graph:
    """Class which implements the graph.
    
    Attributes:
        gap:
        rows:
        cols:
        grid:
        path:
        start:
        destination:
    """
    def __init__(self, rows: int, gap: int) -> None:
        """Initializes the graph."""
        self.gap = gap
        self.rows = rows
        self.cols = rows
        self.grid = self.create_grid()
        self.path = {}
        self.start = None
        self.destination = None

    def create_grid(self) -> list[object]:
        """Creates the initial state of the grid."""
        grid = []

        for row in range(self.rows):
            grid.append([])

            for col in range(self.rows):
                spot = Spot(row, col, self.gap)
                grid[row].append(spot)

        return grid

    def create_start(self, spot: object) -> None:
        """"""
        spot.is_start()
        self.start = spot

    def create_destination(self, spot: object) -> None:
        """"""
        spot.is_destination()
        self.destination = spot

    def dijkstra(self, gui: object) -> None:
        """"""
        prev = {}
        distance = {}
        queue = PriorityQueue()
