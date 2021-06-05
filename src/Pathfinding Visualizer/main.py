"""Runs the pathfinding visualizer.

It supports dijkstra's shortest path and the A* search algorithm.
The GUI allows one to create a start and destination vertex, and obstacles
which the algorithms take into consideration to guarantee the shortest path.

Typical usage example:
    window = GUI(rows=50, width=800)
    window.run()
"""
from gui import GUI

# Example usage
if __name__ == "__main__":
    window = GUI(rows=50, width=800)
    window.run()
