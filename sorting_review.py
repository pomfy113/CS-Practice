

def bubble_sort(data):
    return

def sorting_test(sort_type):
    data1 = [5, 4, 2, 1, 3]
    results1 = globals()[sort_type]
    print(results1)

if __name__ == '__main__':
    sort_type = args[0]
    if sort_type in globals():
        sorting_test(sort_type)
    else:
        print("Could not find sorting type!")
