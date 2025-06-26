def min_positive(func):
    left, right = 0, 100000
    result = None
    while left <= right:
        mid = (left + right) // 2
        val = func(mid)
        if val > 0:
            result = val
            right = mid - 1
        else:
            left = mid + 1
    return result
def func(x):
    return x + 1

print(min_positive(func))    # func(0) = 1
def func(x):
    return 2*x - 9

print(min_positive(func))    # func(0) = -9, func(1) = -7, func(2) = -5, func(4) = -1, func(5) = 1
def func(x):
    return x**3 + 1

print(min_positive(func))    # func(0) = 1, func(1) = 2, func(2) = 9, func(3) = 28
def func(x):
    return 2**x - 5

print(min_positive(func))    # func(0) = -4, func(1) = -3, func(2) = -1, func(3) = 3
def func(x):
    return 2*x**5 - 100

print(min_positive(func))    # func(0) = -100, func(1) = -98, func(2) = -36, func(3) = 386
def func(x):
    return 22*x - 200

print(min_positive(func))    # func(0) = -200, func(5) = -90, func(9) = -2, func(10) = 20