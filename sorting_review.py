

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
    """Keep moving data down the line and inserting them in appropriate index.
    NOTE: Really useful for almost sorted
    """
    length = len(data)
    print(data)
    for i in range(1, length):
        key = data[i]
        index = i - 1

        while index >= 0 and key < data[index]:
            print("Thing")
            # Move what's on index up
            data[index+1] = data[index]
            # Move left
            index -= 1

        # Place item in front of first number lower than it
        data[index+1] = key

def merge(data):
    helper = data[:] # Using this for buffer
    merge_helper(data, helper, 0, len(data))

def merge_helper(input, output, left, right):
    # We have to swap input/output to change what's being used as a buffer
    length = len(input)
    if right - left < 2:
        return
    else:
        partition = (left + right) // 2
        merge_helper(output, input, left, partition)
        merge_helper(output, input, partition, right)
        merge_combine(input, output, left, partition, right)

def merge_combine(data, helper, left, partition, right):
    left_buffer = 0
    right_buffer = 0

    for i in range(left, right):
        left_total = left + left_buffer
        right_total = partition + right_buffer

        if right_total == right:
            # Check if we only have the left items remaining
            data[i] = helper[left_total]
            left_buffer += 1
        elif left_total == partition:
            # Check if we only have the right items remaining
            data[i] = helper[right_total]
            right_buffer += 1
        elif helper[left_total] <= helper[right_total]:
            # Add the smaller left object
            data[i] = helper[left_total]
            left_buffer += 1
        elif helper[left_total] > helper[right_total]:
            # Add the smaller right object
            data[i] = helper[right_total]
            right_buffer += 1

def radix(data):
    pass

def quick(data):
    quick_helper(data, 0, len(data))

def quick_helper(data, left, right):
    if left < right:
        # Keeping track of where to put in new data
        index = left

        for i in range(left+1, right):
            if data[index] > data[i]:
                data[index], data[i] = data[i], data[index]
                index += 1

        quick_helper(data, left, index)
        quick_helper(data, index+1, right)

def sorting_test(sort_type):
    if sort_type == radix:
        dataRad = [111, 101, 121, 415, 612, 135, 213]
        globals()[sort_type](data2)
    else:
        # data_random = [5, 4, 2, 1, 3, 5]
        # data_sorted = [1, 2, 3, 4, 3]
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
