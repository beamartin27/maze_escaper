import random

def generate_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]

    def carve_path(x, y): # use recursion to carve paths
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # possible movements
        random.shuffle(directions) # ensure all paths are different when calling funciton

        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy # calculate next cell to check

            if 1 <= nx < height - 1 and 1 <= ny < width - 1 and maze[nx][ny] == 0: # Check bounds
                maze[nx][ny] = 1 # convert target cell to path
                maze[x + dx][y + dy] = 1 # convert intermediate cell to path

                carve_path(nx, ny)

    # starting point
    maze[1][1] = 1
    carve_path(1, 1)

    # Hardcode paths around the goal due to errors in the maze generation
    # ensure there are paths around the goal position at the bottom right of the maze
    goal_x, goal_y = height - 2, width - 2
    maze[goal_x][goal_y - 1] = 1 
    maze[goal_x - 1][goal_y] = 1

    return maze
