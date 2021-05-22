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
            pygame.draw.line(self.window, Colour._GREY, (0, i * self.gap), (self.width, i * self.gap))

            for j in range(self.cols):
                pygame.draw.line(self.window, Colour._GREY, (j * self.gap, 0), (j * self.gap, self.width))

    def draw(self) -> None:
        """Draws the cells of the grid."""
        self.window.fill(Colour._WHITE)

        for row in self.graph.grid:
            for spot in row:
                pygame.draw.rect(self.window, spot.colour, (spot.x, spot.y, self.gap, self.gap))

        pygame.display.update()

    def handle_events(self) -> bool:
        """Handles mouse and key events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            # Left mouse button
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = self.get_position(position)
                spot = self.graph.grid[row][col]

                if not self.graph.start and spot != self.graph.destination:
                    self.graph.create_start(spot)

                elif not self.graph.destination and spot != self.graph.start:
                    self.graph.create_destination(spot)

                elif spot != self.graph.destination and spot != self.graph.start:
                    spot.create_wall()

        return True

    def run(self) -> None:
        """Main loop of the GUI."""
        while self.handle_events():
            self.draw()

        pygame.quit()

    def get_position(self, position: tuple[int, int]) -> tuple[int, int]:
        """Gets the position of the cell which was clicked."""
        x, y = position
        row = y // self.gap
        col = x // self.gap
        return row, col
