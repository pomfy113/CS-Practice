maze = [
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
]

def maze_get(y, x, grid, solution):
    if y == len(maze) - 1 and x == len(maze[y]) - 1:
        print([*solution, (x, y)])
        return [*solution, (x, y)]
    if grid[y][x] == 0:
        grid[y][x] = 1

        new_solution = [*solution, (x, y)]

        if x < len(grid[y]) - 1 and grid[y][x+1] != 1:
            return maze_get(y, x+1, grid, new_solution)
        if x > 0  and grid[y][x-1] != 1:
            return maze_get(y, x-1, grid, new_solution)
        if y < len(grid) - 1 and grid[y+1][x] != 1:
            return maze_get(y+1, x, grid, new_solution)
        if y > 0  and grid[y -1][x] != 1:
            return maze_get(y-1, x, grid, new_solution)

new_solution = []
maze_get(0, 0, maze, new_solution)
