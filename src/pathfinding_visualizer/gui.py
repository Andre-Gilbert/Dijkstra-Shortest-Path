"""Implements the graphical user interface using pygame.

The GUI handles mouse and keyboard events such as:
- Left click to create the start, destination and walls
- Right click to undo a vertex
- Press c to reset all vertices
- Press m to generate a random maze
- Press 1 to visualize Dijkstra's algorithm
- Press 2 to visualize A* search
- Press 3 to visualize Bidirectional search
- Press 4 to visualize Breadth-first search
- Press 5 to visualize Depth-first search
"""
import pygame
from random import randrange
from pathfinder import Pathfinder
from vertex import Vertex
from utils import Algorithms, Colors


class GUI:
    """Class which implements the user interface.

    Attributes:
        _pathfinder: The pathfinder object used to run the algorithms.
        _gap: The width of a vertex.
        _rows: The number of rows of the grid.
        _cols: The number of columns of the grid.
        _width: The width of the interface.
        _window: The graphical user interface.
    """

    def __init__(self, rows: int = 50, width: int = 700) -> None:
        """Initializes the graphical user interface.

        Args:
            rows: The number of rows of the grid.
            width: The width of the window.

        Raises:
            TypeError: If rows or width are not of type int.
        """
        if not isinstance(rows, int) or not isinstance(width, int):
            raise TypeError('Inputs must be integers.')

        self._pathfinder = Pathfinder()
        self._gap = width // rows
        self._rows = rows
        self._cols = rows
        self._width = width
        self._window = pygame.display.set_mode((width, width))

        pygame.display.set_caption("Pathfinding Visualizer")

    def _initialize_grid(self) -> list[list[Vertex]]:
        """Initializes an empty grid."""
        grid = []
        for row in range(self._rows):
            grid.append([])
            for col in range(self._cols):
                grid[row].append(Vertex(row, col, self._gap, self._rows))

        return grid

    def _generate_maze(
        self,
        grid: list[list[Vertex]],
        start: Vertex,
        destination: Vertex,
        threshold: float = 0.3,
    ) -> list[list[Vertex]]:
        """Generates a random maze."""
        self._reset_vertices(grid, True)
        n = round(len(grid) * len(grid) * threshold)

        for _ in range(n + 1):
            row = randrange(len(grid))
            col = randrange(len(grid))
            if grid[row][col] != start and grid[row][col] != destination:
                grid[row][col].make_wall()

    def draw(self, grid: list[list[Vertex]]) -> None:
        """Draws the vertices."""
        for row in grid:
            for vertex in row:
                vertex.draw(self._window)

        self._draw_lines()
        pygame.display.update()

    def _draw_lines(self) -> None:
        """Draws the grid lines."""
        for i in range(self._rows):
            pygame.draw.line(self._window, Colors.LIGHT_BLUE, (0, i * self._gap), (self._width, i * self._gap))
            pygame.draw.line(self._window, Colors.LIGHT_BLUE, (i * self._gap, 0), (i * self._gap, self._width))

    def _get_clicked_position(self, position: tuple[int, int]) -> tuple[int, int]:
        """Gets the clicked position."""
        x, y = position
        row = x // self._gap
        col = y // self._gap
        return row, col

    def _make_vertex(
        self,
        grid: list[list[Vertex]],
        start: Vertex,
        destination: Vertex,
    ) -> tuple[list[list[Vertex]], Vertex, Vertex]:
        """Creates the start, destination or a wall vertex."""
        position = pygame.mouse.get_pos()
        row, col = self._get_clicked_position(position)
        vertex = grid[row][col]

        if not start and vertex != destination and not vertex.is_wall():
            start = vertex
            start.make_start()
        elif not destination and vertex != start and not vertex.is_wall():
            destination = vertex
            destination.make_destination()
        elif vertex != start and vertex != destination:
            vertex.make_wall()

        return grid, start, destination

    def _reset_vertex(
        self,
        grid: list[list[Vertex]],
        start: Vertex,
        destination: Vertex,
    ) -> tuple[list[list[Vertex]], Vertex, Vertex]:
        """Resets the start, destination or a wall vertex."""
        position = pygame.mouse.get_pos()
        row, col = self._get_clicked_position(position)
        vertex = grid[row][col]
        vertex.reset_vertex()

        if vertex == start:
            start = None
        elif vertex == destination:
            destination = None

        return grid, start, destination

    def _reset_vertices(self, grid: list[list[Vertex]], is_maze: bool = False) -> None:
        """Resets all vertices by coloring them white."""
        for row in grid:
            for vertex in row:
                if vertex.is_visited() or vertex.is_path():
                    vertex.reset_vertex()
                elif is_maze and vertex.is_wall():
                    vertex.reset_vertex()

    def _update_neighbors(self, grid: list[list[Vertex]]) -> None:
        """Updates the neighbor vertices."""
        for row in grid:
            for vertex in row:
                vertex.update_neighbors(grid)

    def _visualize_algorithm(
        self,
        grid: list[list[Vertex]],
        start: Vertex,
        destination: Vertex,
        algorithm: Algorithms,
    ) -> None:
        """Visualizes a pathfinding algorithm."""
        self._reset_vertices(grid)
        self._update_neighbors(grid)

        if algorithm == Algorithms.DIJKTRA:
            self._pathfinder.dijkstra(self, grid, start, destination)
        elif algorithm == Algorithms.A_STAR_SEARCH:
            self._pathfinder.a_star_search(self, grid, start, destination)
        elif algorithm == Algorithms.BIDIRECTIONAL_SEARCH:
            self._pathfinder.bidirectional_search(self, grid, start, destination)
        elif algorithm == Algorithms.BREADTH_FIRST_SEARCH:
            self._pathfinder.breadth_first_search(self, grid, start, destination)
        elif algorithm == Algorithms.DEPTH_FIRST_SEARCH:
            self._pathfinder.depth_first_search(self, grid, start, destination)

    def run(self) -> None:
        """Runs the pathfinding visualizer."""
        run = True
        start = destination = None
        grid = self._initialize_grid()

        while run:
            self.draw(grid)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # Left click
                if pygame.mouse.get_pressed()[0]:
                    grid, start, destination = self._make_vertex(grid, start, destination)

                # Right click
                if pygame.mouse.get_pressed()[2]:
                    grid, start, destination = self._reset_vertex(grid, start, destination)

                if event.type == pygame.KEYDOWN:

                    # Dijkstra's algorithm
                    if event.key == pygame.K_1 and start and destination:
                        self._visualize_algorithm(grid, start, destination, Algorithms.DIJKTRA)

                    # A* search algorithm
                    elif event.key == pygame.K_2 and start and destination:
                        self._visualize_algorithm(grid, start, destination, Algorithms.A_STAR_SEARCH)

                    # Bidirectional search
                    elif event.key == pygame.K_3 and start and destination:
                        self._visualize_algorithm(grid, start, destination, Algorithms.BIDIRECTIONAL_SEARCH)

                    # Breath-first search
                    elif event.key == pygame.K_4 and start and destination:
                        self._visualize_algorithm(grid, start, destination, Algorithms.BREADTH_FIRST_SEARCH)

                    # Depth-first search
                    elif event.key == pygame.K_5 and start and destination:
                        self._visualize_algorithm(grid, start, destination, Algorithms.DEPTH_FIRST_SEARCH)

                    # Generate maze
                    elif event.key == pygame.K_m:
                        self._generate_maze(grid, start, destination)

                    # Reset grid
                    elif event.key == pygame.K_c:
                        start = destination = None
                        grid = self._initialize_grid()
                        self.draw(grid)

        pygame.quit()
