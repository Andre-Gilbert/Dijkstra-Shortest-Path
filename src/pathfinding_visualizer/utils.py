"""Pathfinding visualizer utils."""
from __future__ import annotations
from enum import Enum, auto
from queue import deque


class Algorithms(Enum):
    DIJKTRA = auto()
    A_STAR_SEARCH = auto()
    BIDIRECTIONAL_SEARCH = auto()
    BREADTH_FIRST_SEARCH = auto()
    DEPTH_FIRST_SEARCH = auto()


class Colors:
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (12, 53, 71)
    YELLOW = (255, 254, 106)
    GREEN = (50, 205, 50)
    BLUE = (0, 190, 218, 0.75)
    LIGHT_BLUE = (175, 216, 248)


class Path:
    """Helper class for reconstructing paths."""

    @staticmethod
    def reconstruct(
        gui: object,
        grid: list[list[object]],
        came_from: dict[object, object],
        destination: object,
    ) -> None:
        """Reconstructs the shortest path."""
        current = destination
        while current in came_from:
            current = came_from[current]
            current.make_path()
            gui.draw(grid)

    @staticmethod
    def reconstruct_bidirectional(
        gui: object,
        grid: list[list[object]],
        came_from_src: dict[object, object],
        came_from_dst: dict[object, object],
        intersection: object,
    ) -> None:
        """Reconstructs the shortest path."""
        intersection.make_path()
        current_src = intersection
        current_dst = intersection
        while current_src in came_from_src or current_dst in came_from_dst:
            current_src = came_from_src[current_src] if current_src else None
            current_src.make_path()
            current_dst = came_from_dst[current_dst] if current_dst else None
            current_dst.make_path()
            gui.draw(grid)


class AStarSearch:
    """Helper class for visualizing A* search."""

    @staticmethod
    def manhatten_distance(current: object, destination: object) -> int:
        """Computes the manhatten distance to the destination."""
        x1, y1 = current.get_position()
        x2, y2 = destination.get_position()
        return abs(x1 - x2) + abs(y1 - y2)


class BidirectionalSearch:
    """Helper class for visualizing bidirectional search."""

    @staticmethod
    def bfs(
        gui: object,
        grid: list[list[object]],
        goal: object,
        queue: deque[object],
        visited: set[object],
        came_from: dict[object, object],
    ) -> None:
        """Runs breadth-first search."""
        current = queue.popleft()
        visited.add(current)

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

        if current != goal:
            current.make_visited()

        gui.draw(grid)

    @staticmethod
    def is_intersecting(visited_src: set[object], visited_dst: set[object]) -> set[object] | int:
        """Checks if the visited vertices starting at start intersects with visited vertices starting at destination."""
        intersection = visited_src.intersection(visited_dst)
        return intersection if intersection else -1
