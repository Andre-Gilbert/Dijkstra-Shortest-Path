# Pathfinding Algorithms

This repository's goal is to demonstrate how to implement pathfinding algorithms in the simplest and most elegant ways. At its core, a pathfinding algorithms searches a graph by starting at one vertex and exploring adjacent vertices until the destination is reached, generally with the intent of finding the shortest path.

## Meet the Algorithms

**Dijkstra Shortest Path** (weighted): <br/>
The OG pathfinding algorithm which guarantees the shortest path.

<b>A\* Search Algorithm</b> (weighted): <br/>
Arguably the best pathfinding algorithm which uses heuristics to guarantee the shortest path much faster than Dijkstra's Shortest Path.

## Usage

- Left click to set the start, destination and walls
- Right click to undo a vertex
- Press **c** to reset all vertices
- Press **a** to start the A\* search algorithm
- Press **d** to start Dijkstra's shortest path algorithm
- Press **m** to generate a random maze

## Requirements

- python >= 3.9
- pygame

## License

This repository is released under the [MIT license](https://opensource.org/licenses/MIT). In short, this means you are free to use this software in any personal, open-source or commercial projects. Attribution is optional but appreciated.
