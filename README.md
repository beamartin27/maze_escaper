# Maze Escaper Game

## Final Project for Algorithms and Data Structures

### Overview

This project is divided into two parts:

1. **Graded Algorithms**: Focused on the core algorithms required for grading.
2. **Game Implementation**: Handles the graphical interface and game mechanics.

### Graded Algorithms

The key algorithms for grading are implemented in `bfs.py` and `maze.py`.

- **Maze Generation (Recursion)**:  
  Found in `maze.py`. This algorithm creates a maze by recursively carving paths (changing 0s to 1s) until no more adjacent cells are available.  
  Based on:  
  [Maze Generation - Recursive Division Algorithm](https://weblog.jamisbuck.org/2011/1/12/maze-generation-recursive-division-algorithm)  
  [Maze Generation - Recursive Backtracking](https://aryanab.medium.com/maze-generation-recursive-backtracking-5981bc5cc766)

- **Breadth-First Search (BFS) and Queuing**:  
  Found in `bfs.py`. This algorithm finds the optimal path from the start to the goal using classical BFS, exploring all nodes at the current level before moving deeper into the graph.  
  References:  
  Class materials and slides  
  [BFS Algorithm for Maze Solving](https://medium.com/@luthfisauqi17_68455/artificial-intelligence-search-problem-solve-maze-using-breadth-first-search-bfs-algorithm-255139c6e1a3)

### Game Implementation

The game and its graphical interface are implemented in `maze_escape.py` and `utils.py`. These files are not part of the grading focus. Large Language Models (e.g., ChatGPT-4) were used to help implement the game's mechanics.

### How to Play

1. **Install Required Packages**:  
   Ensure you have the following Python packages installed: `collections`, `random`, and `pygame`.

2. **Run the Game**:  
   Launch the game by running `maze_escape.py`.

3. **Controls**:  
   - Use the arrow keys to control the player (red).  
   - Reach the goal (green).  
   - There are 3 levels, each increasing in difficulty (larger grids and smaller cells).  
   - If stuck, press the spacebar to reveal the optimal path (press again to hide it).

Enjoy the game!

### Group Members

- Beatriz Martin
- Luis Infante
- Maximiliano Martin
- Gonzalo Nicolas