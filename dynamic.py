def fib(num):
    array = [1, 1]
    for i in range(1, num-1):
        array.append((array[i-1] + array[i]))

    return array[-1]

print(fib(100))
