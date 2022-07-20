# Pathfinding Visualizer

This repository's goal is to demonstrate how to implement pathfinding algorithms in the simplest and most elegant ways. At its core, a pathfinding algorithm searches a graph by starting at one vertex and exploring adjacent vertices until the destination is reached, generally with the intent of finding the shortest path.

## Meet the Algorithms

**Dijkstra Algorithm** (weighted): <br/>
The OG pathfinding algorithm which guarantees the shortest path.

**A\* Search** (weighted): <br/>
Arguably the best pathfinding algorithm which uses heuristics to guarantee the shortest path much faster than Dijkstra's algorithm.

**Bidirectional Search** (unweighted): <br/>
Runs Breadth-first search from both sides. Does guarantee the shortest path.

**Breadth-first search** (unweighted): <br/>
A great algorithm for pathfinding. Does guarantee the shortest path.

**Depth-first search** (unweighted): <br/>
An awful algorithm for pathfinding. Does not guarantee the shortest path.

## Pathfinding Visualizer Usage

- Left click to create the start, destination and walls
- Right click to undo a vertex
- Press c to reset all vertices
- Press m to generate a random maze
- Press 1 to visualize Dijkstra's algorithm
- Press 2 to visualize A* search
- Press 3 to visualize Bidirectional search
- Press 4 to visualize Breadth-first search
- Press 5 to visualize Depth-first search

## Requirements

- python >= 3.10
- View [requirements](requirements.txt).

## License

This repository is released under the [MIT license](https://opensource.org/licenses/MIT). In short, this means you are free to use this software in any personal, open-source or commercial projects. Attribution is optional but appreciated.
