def add_one(item):
    length = len(item)
    remainder = True
    for i in range(length-1, -1, -1):
        if remainder is True:
            if item[i] == 9:
                item[i] = 0
            else:
                item[i] += 1
                remainder = False

    if remainder is True:
        item.insert(0, 1)
    print(item)

# add_one([9, 5, 9, 9])

def riddle(arr):
    """Finds max in the minimums in gradually increasing window sizes.
    eg: 5, 1, 4, 3
        [(5)] [(1)] [(4)] [(1)] => 5
        [5, (1)], [(1), 4], [4, (3)] => 3
        [5, (1), 4], [(1), 4, 3] => 1
        [5, (1), 4, 3] => 1

    """
    length = len(arr)
    # Window going up in size
    final_list = []

    for i in range(0, length):
        all_windows = []
        # Iteration
        for j in range(0, length - i):
            window = []

            # Filling the windows up
            for k in range(0, i+1):
                window.append(arr[j+k])

            all_windows.append(min(window))
        final_list.append(max(all_windows))

    return final_list
print(riddle([5, 1, 4, 3]))
