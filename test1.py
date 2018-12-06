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

add_one([9, 5, 9, 9])
