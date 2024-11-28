from collections import deque

# find shortest path from start to goal

def bfs(start, goal, maze):
    queue = deque([start])  
    visited = set([start]) 
    parent = {start: None}  

    while queue:
        current = queue.popleft() # while there are elements in the queue we visit

        if current == goal:
            return reconstruct_path(parent, goal)

        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited and maze[neighbor[0]][neighbor[1]] == 1: # if not visited and is a path
                queue.append(neighbor)
                visited.add(neighbor) 
                parent[neighbor] = current # add current to path list

    return None

def reconstruct_path(parent, goal): # backtrack from goal using parent dict to create sequence of moves
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    return path[::-1] # create copy

def get_neighbors(pos, maze): # return list of valid cells to explore
    neighbors = []
    x, y = pos
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]): # check bounds
            neighbors.append((nx, ny)) # append to list of valid cells
    return neighbors
