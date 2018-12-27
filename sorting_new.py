# Radix, in_place heap sort, no removal (use max heap)
import math


def digit(data):
    largest = max(data)
    smallest = min(data)
    num = max([abs(largest), abs(smallest)])

    if num == 0:
        return 1

    digits = 0

    while num // 10 ** digits > 0:
        digits += 1

    return digits

def radix(data):
    digits = digit(data)
    copy = data[:]
    buckets = [[] for _ in range(10)]

    # Go through amount of digits
    for i in range(digits):
        # Per number's digit, place into proper bucket
        for num in data:
            bucket = (num // 10 ** i) % 10
            buckets[bucket].append(num)
        # Clearing original
        data.clear()

        # Unload the bucket
        for bucket in buckets:
            data.extend(bucket)
            bucket.clear()

        print("\n")
    print(data)


data = [0, 501, 10, 100, 121, 500, 1000]
radix(data)
print(data)
