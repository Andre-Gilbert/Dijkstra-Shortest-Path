"""A dijkstra shortest path visualizer."""
from queue import PriorityQueue

import pygame


class DijkstraVisualizer:
    """

    Attributes:
        rows:
        width:
    """
    _WHITE = (255, 255, 255)
    _GREY = (128, 128, 128)

    def __init__(self, rows: int = 50, width: int = 800) -> None:
        """Initializes the dijkstra visualizer."""
        self.rows = rows
        self.width = width
        self.window = pygame.display.set_mode((width, width))

        pygame.display.set_caption("Dijkstra Shortest Path")

    def create_grid(self):
        grid = []
        gap = self.width // self.rows

        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                spot = DijkstraVisualizer().Spot(i, j, gap, self.rows)
                grid[i].append(spot)

        return grid

    def reconstruct_path(self, current, came_from):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            self.draw()

    def draw(self, grid):
        self.window.fill(self._WHITE)

        for row in grid:
            for spot in row:
                spot.draw(self.window)

        self.draw_grid()
        pygame.display.update()

    def draw_grid(self):
        gap = self.width // self.rows
        for i in range(self.rows):
            pygame.draw.line(self.window, self._GREY, (0, i * gap), (self.width, i * gap))
            for j in range(self.rows):
                pygame.draw.line(self.window, self._GREY, (j * gap, 0), (j * gap, self.width))

    def get_position(self, pos):
        gap = self.width // self.rows
        y, x = pos

        row = y // gap
        column = x // gap

        return row, column

    def h(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def dijkstra(self, draw, grid, start, end):
        count = 0

        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}
        g_score = {spot: float("inf") for row in grid for spot in row}
        g_score[start] = 0
        f_score = {spot: float("inf") for row in grid for spot in row}
        f_score[start] = self.h(start.get_pos(), end.get_pos())

        open_set_hash = {start}

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                self.reconstruct_path(came_from, end, draw)
                end.make_end()
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.h(neighbor.get_position(), end.get_position())
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.create_open()

            self.draw()

            if current != start:
                current.create_closed()

        return False

    def visualize(self):
        grid = self.create_grid()

        start = None
        end = None

        run = True
        while run:
            self.draw(grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if pygame.mouse.get_pressed()[0]:  # LEFT
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_position(pos)
                    spot = grid[row][col]
                    if not start and spot != end:
                        start = spot
                        self.start.create_start()

                    elif not end and spot != start:
                        end = spot
                        end.create_end()

                    elif spot != end and spot != start:
                        spot.create_wall()

                elif pygame.mouse.get_pressed()[2]:  # RIGHT
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_position(pos)
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start and end:
                        for row in grid:
                            for spot in row:
                                spot.self.update_neighbors(grid)

                        self.dijkstra(lambda: self.draw(grid), grid, start, end)

                    if event.key == pygame.K_c:
                        start = None
                        end = None
                        grid = self.create_grid()

                pygame.quit()

    class Spot:
        """"""
        _RED = (255, 0, 0)
        _GREEN = (0, 255, 0)
        _BLUE = (0, 255, 0)
        _YELLOW = (255, 255, 0)
        _BLACK = (0, 0, 0)
        _PURPLE = (128, 0, 128)
        _ORANGE = (255, 165, 0)
        _TURQUOISE = (64, 224, 208)

        def __init__(self, row: int, column: int, width: int, total_rows: int):
            """Initializes the spot class."""
            self.row = row
            self.col = column
            self.x = row * width
            self.y = column * width
            self.color = DijkstraVisualizer._WHITE
            self.neighbors = []
            self.width = width
            self.total_rows = total_rows

        def get_position(self):
            return self.row, self.column

        def is_closed(self):
            return self.color == self._RED

        def is_open(self):
            return self.color == self._GREEN

        def is_wall(self):
            return self.color == self._BLACK

        def is_start(self):
            return self.color == self._ORANGE

        def is_end(self):
            return self.color == self._TURQUOISE

        def reset(self):
            self.color = DijkstraVisualizer._WHITE

        def create_start(self):
            self.color = self._ORANGE

        def create_closed(self):
            self.color = self._RED

        def create_open(self):
            self.color = self._GREEN

        def create_wall(self):
            self.color = self._BLACK

        def create_end(self):
            self.color = self._TURQUOISE

        def create_path(self):
            self.color = self._PURPLE

        def draw(self, win):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

        def update_neighbors(self, grid):
            self.neighbors = []

            # Down
            if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():
                self.neighbors.append(grid[self.row + 1][self.col])

            # Up
            if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
                self.neighbors.append(grid[self.row - 1][self.col])

            # Right
            if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():
                self.neighbors.append(grid[self.row][self.col + 1])

            # Left
            if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
                self.neighbors.append(grid[self.row][self.col - 1])

        def __lt__(self, other):
            return False


# Example usage
if __name__ == "__main__":
    dijkstra = DijkstraVisualizer()
    dijkstra.visualize()
