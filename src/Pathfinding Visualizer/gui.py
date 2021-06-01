""""""
import pygame

from node import Node
from pathfinding_algorithm import Pathfinder


class GUI:
    """Class which implements the user interface.

    Attributes:
        __gap: The width of a node.
        __rows: The number of rows of the grid.
        __cols: The number of columns of the grid.
        __width: The width of the interface.
        __window: The graphical user interface.
    """
    __GREY = (128, 128, 128)

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

    def __initialize_grid(self) -> list[list[Node]]:
        """Initializes an empty grid.

        Returns:
            A 2D array containing all of the nodes in the grid.
        """
        grid = []

        for row in range(self.__rows):
            grid.append([])

            for col in range(self.__cols):
                grid[row].append(Node(row, col, self.__gap, self.__rows))

        return grid

    def draw(self, grid: list[list[Node]]) -> None:
        """Draws the nodes."""
        for row in grid:
            for node in row:
                node.draw(self.__window)

        self.__draw_lines()
        pygame.display.update()

    def __draw_lines(self) -> None:
        """Draws the grid lines."""
        for i in range(self.__rows):
            pygame.draw.line(self.__window, self.__GREY, (0, i * self.__gap), (self.__width, i * self.__gap))
            pygame.draw.line(self.__window, self.__GREY, (i * self.__gap, 0), (i * self.__gap, self.__width))

    def __get_clicked_position(self, position: tuple[int, int]) -> tuple[int, int]:
        """Gets the clicked position.

        Args:
            position: x-, y-Coordinate of the position.

        Returns:
            The row and column of the node.
        """
        x, y = position
        row, col = x // self.__gap, y // self.__gap
        return row, col

    def run(self) -> None:
        """Main loop of the gui."""
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

                #if started:
                #    continue

                # Left click
                if pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()
                    row, column = self.__get_clicked_position(position)
                    node = grid[row][column]

                    if not start and node != destination:
                        start = node
                        start.make_start()

                    elif not destination and node != start:
                        destination = node
                        destination.make_destination()

                    elif node != start and node != destination:
                        node.make_wall()

                # Right click
                elif pygame.mouse.get_pressed()[2]:
                    position = pygame.mouse.get_pos()
                    row, column = self.__get_clicked_position(position)
                    node = grid[row][column]
                    node.reset_node()

                    if node == start:
                        start = None

                    if node == destination:
                        destination = None

                # Initialize the pathfinder
                pathfinder = Pathfinder(grid, start, destination)

                if event.type == pygame.KEYDOWN:

                    # Dijkstra
                    if event.key == pygame.K_d and not started:
                        started = True

                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)

                        pathfinder.dijkstra(self)

                    # A* search
                    elif event.key == pygame.K_a and not started:
                        started = True

                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)

                        pathfinder.a_star_search(self)

                    # Reset grid
                    elif event.key == pygame.K_c:
                        started = False
                        start = destination = None
                        grid = self.__initialize_grid()
                        self.draw(grid)

        pygame.quit()
