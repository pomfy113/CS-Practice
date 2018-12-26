def memoize(func):
    memo = {}

    def memoized_func(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]

    return memoized_func

@memoize
def fib(num):
    if num == 1 or num == 0:
        return num
    else:
        return fib(num-1) + fib(num-2)

print(fib(100))
