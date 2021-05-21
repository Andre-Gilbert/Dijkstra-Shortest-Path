""""""
import pygame

from dijkstra_visualizer.graph import Graph
from dijkstra_visualizer.util.colour import Colour


class GUI:
    """Class which implements the graphical user interface.
    
    Attributes:
        gap:
        rows: 
        cols:
        width:
        graph:
        window:
    """
    def __init__(self, rows: int, width: int) -> None:
        """Initializes the GUI."""
        if not isinstance(rows, int) or not isinstance(width, int):
            raise TypeError("Inputs must be integers.")

        self.gap = width // rows
        self.rows = rows
        self.cols = rows
        self.width = width
        self.graph = Graph(self.rows, self.gap)
        self.window = pygame.display.set_mode((width, width))
        pygame.display.set_caption("Dijkstra Shortest Path Visualizer")

    def draw_grid(self) -> None:
        """Draws the lines of the grid."""
        for i in range(self.rows):
            pygame.draw.line(self.window)

            for j in range(self.cols):
                pygame.draw.line(self.window)

    def draw(self) -> None:
        """Draws the cells of the grid."""
        self.window.fill(Colour._WHITE)

    def handle_events(self) -> bool:
        """Handles mouse and key events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

    def run(self) -> None:
        """Main loop of the GUI."""
        while self.handle_events():
            self.draw()

        pygame.quit()

    def get_position(self, position: tuple[int, int]) -> tuple[int, int]:
        """Gets the position of the cell which was clicked."""
        x, y = position
