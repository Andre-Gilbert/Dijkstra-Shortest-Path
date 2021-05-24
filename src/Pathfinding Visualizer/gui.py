import pygame

from a_star import aStar
from dijkstra import dijkstra
from node import Node
from pathfinding_algorithm import Pathfinder

pygame.init()

HEIGHT, WIDTH = 900, 900
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Pathfinding visualizer")

GREY = (128, 128, 128)


def algorithm(draw, grid, start, end):
    aStar(draw, grid, start, end)
    # dijkstra(draw, grid, start, end)


def buildGrid(row, width):

    grid = []
    node_width = width // row
    for i in range(row):
        grid.append([])
        for j in range(row):
            grid[i].append(Node(i, j, node_width, row))
    return grid


def drawGridLines(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        pygame.draw.line(window, GREY, (i * gap, 0), (i * gap, width))


def draw(window, grid, rows, width):
    for row in grid:
        for node in row:
            node.draw(window)
    drawGridLines(window, rows, width)
    pygame.display.update()


def getClickedPosition(position, rows, width):
    gap = width // rows
    x, y = position
    row, column = x // gap, y // gap
    return (row, column)


def main(window, WIDTH):
    ROWS = 90
    grid = buildGrid(ROWS, WIDTH)

    start, end = None, None
    started = False
    run = True

    started = False
    while run:
        draw(window, grid, ROWS, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, column = getClickedPosition(position, ROWS, WIDTH)
                node = grid[row][column]
                if not start and node != end:
                    start = node
                    start.makeStartNode()
                elif not end and node != start:
                    end = node
                    end.makeEndNode()
                elif node != start and node != end:
                    node.makeObstacle()

            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, column = getClickedPosition(position, ROWS, WIDTH)
                node = grid[row][column]
                node.resetNode()
                if node == start:
                    start = None
                if node == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid)

                    algorithm(lambda: draw(window, grid, ROWS, WIDTH), grid, start, end)
                    started = False

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = buildGrid(ROWS, WIDTH)
                    draw(window, grid, ROWS, WIDTH)

    pygame.quit()


# main(window, WIDTH)


class GUI(Pathfinder):
    """

    Attributes:
        __gap: The width of a node.
        __rows: The number of rows of the grid.
        __cols: The number of columns of the grid.
        __width:
        __window:
    """
    def __init__(self, rows, width) -> None:
        """Initializes the graphical user interface."""
        if not isinstance(rows, int) or not isinstance(width, int):
            raise TypeError("Inputs must be integers.")

        self.__gap = width // rows
        self.__rows = rows
        self.__cols = rows
        self.__width = width
        self.__window = pygame.display.set_mode((width, width))
        pygame.display.set_caption("Pathfinding Visualizer")

    def __initialize_grid(self) -> list[list[Node]]:
        """Initializes an empty grid."""
        grid = []

        for row in range(self.__rows):
            grid.append([])

            for col in range(self.__cols):
                grid[row].append(Node(row, col, self.__gap, row))

        return grid

    def draw(self, grid: list[list[Node]]) -> None:
        """"""
        for row in grid:
            for node in row:
                node.draw(self.__window)

        self.__draw_lines()
        pygame.display.update()

    def __draw_lines(self) -> None:
        """"""
        for i in range(self.__rows):
            pygame.draw.line(self.__window, GREY, (0, i * self.__gap), (self.__width, i * self.__gap))
            pygame.draw.line(self.__window, GREY, (i * self.__gap, 0), (i * self.__gap, self.__width))

    def __get_clicked_position(self, position: tuple[int, int]) -> tuple[int, int]:
        """"""
        x, y = position
        row, col = x // self.__gap, y // self.__gap
        return row, col

    def run(self) -> None:
        """"""
        run = True
        started = False
        start = destination = None
        grid = self.__initialize_grid()

        while run:
            self.draw(grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if started:
                    continue

                if pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()
                    row, column = self.__get_clicked_position(position)
                    node = grid[row][column]

                    if not start and node != destination:
                        start = node
                        start.make_start_node()

                    elif not destination and node != start:
                        destination = node
                        destination.make_destination_node()

                    elif node != start and node != destination:
                        node.make_wall()

                elif pygame.mouse.get_pressed()[2]:
                    position = pygame.mouse.get_pos()
                    row, column = self.__get_clicked_position(position)
                    node = grid[row][column]
                    node.reset_node()

                    if node == start:
                        start = None

                    if node == destination:
                        destination = None

                pathfinder = Pathfinder(grid, start, destination)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d and not started:
                        started = True
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)

                        pathfinder.dijkstra(self)
                        started = False

                    elif event.key == pygame.K_a and not started:
                        started = True
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)

                        pathfinder.a_star_search(self)
                        started = False

                    elif event.key == pygame.K_c:
                        start = None
                        destination = None
                        grid = self.__initialize_grid()
                        self.draw(grid)

        pygame.quit()
