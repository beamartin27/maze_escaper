import pygame
from maze import generate_maze
from bfs import bfs
from utils import draw_maze # draw maze on screen

# Constants for the levels
LEVELS = [
    {"maze_size": 20, "cell_size": 30},  # Level 1: Small maze, large cells
    {"maze_size": 35, "cell_size": 22},  # Level 2: Medium maze, medium cells
    {"maze_size": 55, "cell_size": 15},  # Level 3: Large maze, small cells
]

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

def main():
    pygame.init() # initialize all pygame modules
    
    # Game loop for each level
    for level in range(len(LEVELS)):
        maze_size = LEVELS[level]["maze_size"] # access values on dictionary
        cell_size = LEVELS[level]["cell_size"]

        # Resize the screen based on the current maze size and cell size
        screen = pygame.display.set_mode((maze_size * cell_size, maze_size * cell_size))

        # Generate a new maze with the updated grid size
        maze = generate_maze(maze_size, maze_size)  # 1 = path, 0 = wall
        start = (1, 1)  # Starting point
        goal = (maze_size - 2, maze_size - 2)  # Exit point (bottom-right corner)

        # Ensure the goal is not a wall
        if maze[goal[0]][goal[1]] == 0:
            maze[goal[0]][goal[1]] = 1  # Make sure the goal is set to a path

        player_pos = start
        path = bfs(start, goal, maze)  # Find the shortest path using BFS

        # Check if path is valid
        if path is None:  
            path = []  # Default to an empty list if BFS failed to find a path

        show_path = False  # Flag to toggle the display of the BFS path
        move_delay = 150  # Delay between movements in milliseconds
        last_move_time = pygame.time.get_ticks()

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return  # Exit both loops
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Toggle showing the BFS path when spacebar is pressed
                        show_path = not show_path

            # Get the keys that are currently pressed
            keys = pygame.key.get_pressed()

            # Get the current time
            current_time = pygame.time.get_ticks()

            # Move the player if enough time has passed since the last move
            if current_time - last_move_time > move_delay:
                new_pos = player_pos
                if keys[pygame.K_UP]:
                    new_pos = (player_pos[0] - 1, player_pos[1])
                elif keys[pygame.K_DOWN]:
                    new_pos = (player_pos[0] + 1, player_pos[1])
                elif keys[pygame.K_LEFT]:
                    new_pos = (player_pos[0], player_pos[1] - 1)
                elif keys[pygame.K_RIGHT]:
                    new_pos = (player_pos[0], player_pos[1] + 1)

                # Check if the new position is within bounds and is a path (1)
                if 0 <= new_pos[0] < maze_size and 0 <= new_pos[1] < maze_size and maze[new_pos[0]][new_pos[1]] == 1:
                    player_pos = new_pos
                    last_move_time = current_time  # Update the last move time

            # Draw everything
            screen.fill(WHITE)
            draw_maze(screen, maze, cell_size)

            # If the user pressed the spacebar, draw the BFS path
            if show_path and path:  # Check that path is not empty before drawing it
                for pos in path:
                    pygame.draw.rect(screen, ORANGE, (pos[1] * cell_size, pos[0] * cell_size, cell_size, cell_size))

            # Draw the player
            pygame.draw.rect(screen, RED, (player_pos[1] * cell_size, player_pos[0] * cell_size, cell_size, cell_size))

            # Draw the 2x2 goal area
            pygame.draw.rect(screen, GREEN, ((goal[1] - 1) * cell_size, (goal[0] - 1) * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, GREEN, ((goal[1]) * cell_size, (goal[0] - 1) * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, GREEN, ((goal[1] - 1) * cell_size, (goal[0]) * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, GREEN, ((goal[1]) * cell_size, (goal[0]) * cell_size, cell_size, cell_size))

            # Check if the player reached the goal
            if player_pos in [(goal[0], goal[1]), (goal[0], goal[1] - 1), (goal[0] - 1, goal[1]), (goal[0] - 1, goal[1] - 1)]:
                print(f"You win level {level + 1}!")
                break

            pygame.display.flip()
            clock.tick(60)

    print("You completed all levels!")
    pygame.quit()

if __name__ == "__main__":
    main()
