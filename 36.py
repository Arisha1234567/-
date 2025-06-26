def golden_pairs(pairs):
    count = 0
    for a, b in pairs:
        max_elem = max(a, b)
        min_elem = min(a, b)
        ratio = max_elem / min_elem
        if 1.6 <= ratio <= 1.7:
            count += 1
    return count
print(golden_pairs([(100, 165), (180, 100), (170, 100), (100, 160)]))
print(golden_pairs([(1, 10), (10, 1), (2, 5), (7, 4)]))
print(golden_pairs([(1, 1), (2, 2), (3, 3), (4, 4)]))
print(golden_pairs([(8, 5)]))
print(golden_pairs([(7, 4), (7, 5), (6, 7)]))
print(golden_pairs([(8, 5), (17, 10), (32, 20), (34, 20)]))
