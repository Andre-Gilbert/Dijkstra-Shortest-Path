"""Implements the graphical user interface using pygame.

The GUI handles mouse and keyboard events such as:
- Left click to create the start, destination and walls
- Right click to undo a vertex
- Press c to reset all vertices
- Press a to start the A* search algorithm
- Press d to start Dijkstra's shortest path algorithm
- Press m to generate a random maze
"""
import pygame

from pathfinding_algorithm import Pathfinder
from vertex import Vertex


class GUI:
    """Class which implements the user interface.

    Attributes:
        __gap: The width of a node.
        __rows: The number of rows of the grid.
        __cols: The number of columns of the grid.
        __width: The width of the interface.
        __window: The graphical user interface.
    """
    __LIGHT_BLUE = (175, 216, 248)

    def __init__(self, rows: int, width: int) -> None:
        """Initializes the graphical user interface.

        Raises:
            TypeError: If rows or width are not of type int.
        """
        if not isinstance(rows, int) or not isinstance(width, int):
            raise TypeError("Inputs must be integers.")

        self.__gap = width // rows
        self.__rows = rows
        self.__cols = rows
        self.__width = width
        self.__window = pygame.display.set_mode((width, width))
        pygame.display.set_caption("Pathfinding Visualizer")

    def __initialize_grid(self) -> list[list[Vertex]]:
        """Initializes an empty grid.

        Returns:
            A 2D array containing all vertices in the grid.
        """
        grid = []

        for row in range(self.__rows):
            grid.append([])

            for col in range(self.__cols):
                grid[row].append(Vertex(row, col, self.__gap, self.__rows))

        return grid

    def draw(self, grid: list[list[Vertex]]) -> None:
        """Draw the vertices.

        Args:
            grid: The grid containing all vertices.
        """
        for row in grid:
            for node in row:
                node.draw(self.__window)

        self.__draw_lines()
        pygame.display.update()

    def __draw_lines(self) -> None:
        """Draw the grid lines."""
        for i in range(self.__rows):
            pygame.draw.line(self.__window, self.__LIGHT_BLUE, (0, i * self.__gap), (self.__width, i * self.__gap))
            pygame.draw.line(self.__window, self.__LIGHT_BLUE, (i * self.__gap, 0), (i * self.__gap, self.__width))

    def __get_clicked_position(self, position: tuple[int, int]) -> tuple[int, int]:
        """Get the clicked position.

        Args:
            position: x-, y-Coordinate of the position.

        Returns:
            The row and column of the vertex.
        """
        x, y = position
        row, col = x // self.__gap, y // self.__gap
        return row, col

    def run(self) -> None:
        """Main loop of the gui."""
        mode = 0
        run = True
        started = False
        start = destination = None
        grid = self.__initialize_grid()

        while run:
            self.draw(grid)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # Left click
                if pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()
                    row, col = self.__get_clicked_position(position)
                    node = grid[row][col]

                    if not start and node != destination and not node.is_wall():
                        start = node
                        start.make_start()

                    elif not destination and node != start and not node.is_wall():
                        destination = node
                        destination.make_destination()

                    elif node != start and node != destination:
                        node.make_wall()

                # Right click
                elif pygame.mouse.get_pressed()[2]:
                    position = pygame.mouse.get_pos()
                    row, col = self.__get_clicked_position(position)
                    node = grid[row][col]
                    node.reset_vertex()

                    if node == start:
                        start = None

                    if node == destination:
                        destination = None

                # Initialize the pathfinder
                pathfinder = Pathfinder(grid, start, destination)

                if event.type == pygame.KEYDOWN:

                    # Dijkstra's shortest path
                    if event.key == pygame.K_d and not started and start and destination:
                        started = True

                        if mode != 0:
                            for row in grid:
                                for vertex in row:
                                    if vertex.is_visited() or vertex.is_visiting() or vertex.is_path():
                                        vertex.reset_vertex()

                        for row in grid:
                            for vertex in row:
                                vertex.update_neighbors(grid)

                        pathfinder.dijkstra(self)
                        mode = 1
                        started = False

                    # A* search algorithm
                    elif event.key == pygame.K_a and not started and start and destination:
                        started = True

                        if mode != 0:
                            for row in grid:
                                for vertex in row:
                                    if vertex.is_visited() or vertex.is_visiting() or vertex.is_path():
                                        vertex.reset_vertex()

                        for row in grid:
                            for vertex in row:
                                vertex.update_neighbors(grid)

                        pathfinder.a_star_search(self)
                        mode = 1
                        started = False

                    # Generate maze
                    elif event.key == pygame.K_m and not started:
                        if mode != 0:
                            for row in grid:
                                for vertex in row:
                                    if vertex.is_visited() or vertex.is_visiting() or vertex.is_path():
                                        vertex.reset_vertex()

                        for row in grid:
                            for vertex in row:
                                if vertex.is_wall():
                                    vertex.reset_vertex()

                        pathfinder.generate_maze()

                    # Reset grid
                    elif event.key == pygame.K_c:
                        mode = 0
                        started = False
                        start = destination = None
                        grid = self.__initialize_grid()
                        self.draw(grid)

        pygame.quit()
