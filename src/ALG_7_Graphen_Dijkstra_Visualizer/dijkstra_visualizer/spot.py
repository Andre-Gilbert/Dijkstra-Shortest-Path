""""""
from dijkstra_visualizer.util.colour import Colour


class Spot:
    def __init__(self, row, col, width, total_rows):
        """Initializes a spot."""
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = Colour._WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
