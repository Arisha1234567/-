def count_triplet_numbers(nums) :
    from collections import Counter

    # Подсчитываем количество вхождений каждого числа
    count = Counter(nums)

    # Подсчитываем, сколько чисел встречается ровно три раза
    triplet_count = sum(1 for v in count.values() if v == 3)

    return triplet_count
print(count_triplet_numbers([4, 5, 6, 4, 5, 4, 5, 6]))    # числа 4 и 5 встречаются ровно 3 раза
print(count_triplet_numbers([5, 4, 5, 5, 4, 5, 7, 4]))    # только число 4 встречается ровно 3 раза
print(count_triplet_numbers([4, 5, 4, 6, 5, 7, 5, 5]))    # ни одно число не встречается ровно 3 раза
print(count_triplet_numbers([5]))                         # ни одно число не встречается ровно 3 раза
print(count_triplet_numbers([1, 1, 1, 1]))                # ни одно число не встречается ровно 3 раза
print(count_triplet_numbers([7, 7, 7]))                   # только число 7 встречается ровно 3 раза
