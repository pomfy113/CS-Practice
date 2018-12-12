"""Let's play with floodfills and graphs again."""

def adjacencies(array, x, y):
    xlimit = len(array[0]) - 1
    ylimit = len(array) - 1

    adjacencies = []
    # Left
    if x != 0 and array[y][x-1] != 1:
        adjacencies.append((x-1, y))
    # Up
    if y != 0 and array[y-1][x] != 1:
        adjacencies.append((x, y-1))
    # Right
    if x != xlimit and array[y][x+1] != 1:
        adjacencies.append((x+1, y))
    # Bottom
    if y != ylimit and array[y+1][x] != 1:
        adjacencies.append((x, y+1))

    return adjacencies

def fill(array, x, y):

    if array[y][x] == 0:
        array[y][x] = 8

        for adj_x, adj_y in adjacencies(array, x, y):
            fill(array, adj_x, adj_y)
    else:
        return

array = [
[1, 0, 0, 1, 0],
[0, 1, 0, 1, 0],
[0, 1, 0, 1, 0],
[0, 1, 0, 0, 0],
[0, 1, 1, 0, 1]
]

for i in array:
    print(i)

print("\n\n")

fill(array, 0, 1)
for i in array:
    print(i)
