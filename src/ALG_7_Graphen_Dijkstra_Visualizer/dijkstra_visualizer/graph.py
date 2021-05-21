""""""
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

        for i in range(self.rows):
            grid.append([])

            for j in range(self.rows):
                spot = Spot(i, j, self.gap, self.rows)
                grid[i].append(spot)

        return grid
