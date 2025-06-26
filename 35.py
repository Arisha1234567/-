def max_of_two(a, b):
    if a < b:
        return b
    return a

def max_of_four(a, b, c, d):
    max_ab = max_of_two(a, b)
    max_cd = max_of_two(c, d)
    max_all = max_of_two(max_ab, max_cd)
    return max_all
print(max_of_four(4, 9, 10, 5))
print(max_of_four(5, 5, 5, 5))
print(max_of_four(0, -1, -1, 0))
print(max_of_four(-3, -5, -1, -2))
print(max_of_four(1, -2, -1, 2))
print(max_of_four(10, 1, 1, 1))

