"""The vertices, or nodes, denoted in the pathfinding visualizer.

A vertex is represented as a cell in the visualizer.
Depending on the state, a vertex will be colored differently:
- start: green
- destination: red
- wall: black
- unvisited vertices: white
- visited vertices: blue
- shortest path: yellow

Addionally a vertex belongs to a row and column in the grid,
has x, y coordinates, a width, and has access to all of its neighbors.
"""
from __future__ import annotations
import pygame
from utils import Colors


class Vertex:
    """Class which represents a vertex (cell) in the grid.

    Attributes:
        neighbors: Neighbors of the vertex.
        _color: Color of the vertex indicates its state.
        _row: Row of the vertex.
        _col: Column of the vertex.
        _x: x coordinate of the vertex.
        _y: y coordinate of the vertex.
        _width: Width of the vertex.
        _total_rows: Total rows of the grid.
    """

    def __init__(self, row: int, col: int, width: int, total_rows: int) -> None:
        self.neighbors = []
        self._color = Colors.WHITE
        self._row = row
        self._col = col
        self._x = row * width
        self._y = col * width
        self._width = width
        self._total_rows = total_rows

    def get_position(self) -> tuple[int, int]:
        """Returns the position of the vertex."""
        return self._row, self._col

    def is_wall(self) -> bool:
        """Checks if the vertex is a wall."""
        return self._color == Colors.BLACK

    def is_visited(self) -> bool:
        """Checks if the state of the vertex is visited."""
        return self._color == Colors.BLUE

    def is_path(self) -> bool:
        """Checks if the vertex belongs to the shortest path."""
        return self._color == Colors.YELLOW

    def reset_vertex(self) -> None:
        """Resets the vertex by coloring it white."""
        self._color = Colors.WHITE

    def make_start(self) -> None:
        """Colors the vertex green if it's the start."""
        self._color = Colors.GREEN

    def make_destination(self) -> None:
        """Colors the vertex red if it's the destination."""
        self._color = Colors.RED

    def make_visited(self) -> None:
        """Colors the vertex blue if the algorithm has visited it."""
        self._color = Colors.BLUE

    def make_wall(self) -> None:
        """Colors the vertex black if it's a wall."""
        self._color = Colors.BLACK

    def make_path(self) -> None:
        """Colors the vertex yellow if it belongs to the shortest path."""
        self._color = Colors.YELLOW

    def draw(self, window: pygame.display) -> None:
        """Draws the vertex."""
        pygame.draw.rect(window, self._color, (self._x, self._y, self._width, self._width))

    def update_neighbors(self, grid: list[list[Vertex]]) -> None:
        """Updates all neighbors of a vertex."""
        self.neighbors = []

        # Vertex below
        if self._row < self._total_rows - 1 and not grid[self._row + 1][self._col].is_wall():
            self.neighbors.append(grid[self._row + 1][self._col])

        # Vertex above
        if self._row > 0 and not grid[self._row - 1][self._col].is_wall():
            self.neighbors.append(grid[self._row - 1][self._col])

        # Vertex to the right
        if self._col < self._total_rows - 1 and not grid[self._row][self._col + 1].is_wall():
            self.neighbors.append(grid[self._row][self._col + 1])

        # Vertex to the left
        if self._col > 0 and not grid[self._row][self._col - 1].is_wall():
            self.neighbors.append(grid[self._row][self._col - 1])

    def __lt__(self, other: Vertex) -> bool:
        return False
