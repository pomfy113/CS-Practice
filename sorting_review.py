

def bubble(data):
    """Keep swapping as we go forward."""
    for _ in range(len(data)):
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

def selection(data):
    """Find lowest, then jam it left."""
    length = len(data)
    for i in range(length):
        min = i
        for j in range(i, length):
            if data[j] < data[min]:
                min = j

        data[i], data[min] = data[min], data[i]

def insertion(data):
    """Keep moving data down the line and inserting them in appropriate index."""
    length = len(data)

    for i in range(length):
        index = i
        for j in range(length - 1, i, -1):
            # Option 1: swap
            # if data[i] > data[j]:
            #     data[i], data[j] = data[j], data[i]

            # Option 2: keep track of index
            if data[index] > data[j]:
                index = j

        new_item = data.pop(index)
        data.insert(i, new_item)

def sorting_test(sort_type):
    data1 = [5, 4, 2, 1, 3]
    globals()[sort_type](data1)
    print(data1)

if __name__ == '__main__':
    import sys

    sort_type = sys.argv[1]
    print("Using {}".format(sort_type))
    if sort_type in globals():
        sorting_test(sort_type)
    else:
        print("Could not find sorting type!")
