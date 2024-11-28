import pygame

def draw_maze(screen, maze, cell_size):
    """
    Draws the maze on the Pygame screen.
    
    :param screen: The Pygame screen to draw on.
    :param maze: The 2D list representing the maze.
    :param cell_size: The size of each cell in pixels.
    """
    rows = len(maze)
    cols = len(maze[0])

    # Choose colors
    EDGE_COLOR = (0, 0, 255)
    WALL_COLOR = (0, 0, 0)
    PATH_COLOR = (255, 255, 255)
    
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == 0:
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    color = EDGE_COLOR 
                else:
                    color = WALL_COLOR
            else:
                color = PATH_COLOR
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

