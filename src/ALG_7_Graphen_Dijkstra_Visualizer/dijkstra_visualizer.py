"""A dijkstra shortest path visualizer."""
import pygame


class DijkstraVisualizer:
    """
    
    Attributes:
        rows:
        width:
    """
    _WHITE = (255, 255, 255)

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
                spot = Spot(i, j, gap, self.rows)
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

    def visualize(self):
        pass

    class Spot:
        """"""
        _RED = (255, 0, 0)
        _GREEN = (0, 255, 0)
        _BLUE = (0, 255, 0)
        _YELLOW = (255, 255, 0)
        _BLACK = (0, 0, 0)
        _PURPLE = (128, 0, 128)
        _ORANGE = (255, 165, 0)
        _GREY = (128, 128, 128)
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
            self.color = self._WHITE

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


# Example usage
if __name__ == "__main__":
    pass
