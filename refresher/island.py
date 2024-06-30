islands = [
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
]

def handle_islands(y, x, grid):
    if grid[y][x] == 1:
        grid[y][x] = 0

        if x < len(grid[y]) - 1:
            handle_islands(y, x+1, grid)
        if x > 0:
            handle_islands(y, x-1, grid)
        if y < len(grid) - 1:
            handle_islands(y+1, x, grid)
        if y > 0:
            handle_islands(y-1, x, grid)
    return


amount = 0
for y in range(len(islands)):
    for x in range(len(islands[y])):
        print(y, x)
        if islands[y][x] == 1:
            amount += 1
            handle_islands(y, x, islands)

print("======================")
print(amount)
print(islands)