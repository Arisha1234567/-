def min_product_of_two(nums) :
    min1 = float('inf')
    min2 = float('inf')

    for num in nums :
        if num < min1 :
            min2 = min1
            min1 = num
        elif num < min2 :
            min2 = num
    return min1 * min2


print(min_product_of_two([5, 2, 6, 1, 7]))
print(min_product_of_two([1, 1, 1, 1, 1]))
print(min_product_of_two([5, 4, 3, 2, 1]))
print(min_product_of_two([1, 5, 4, 3, 2]))
print(min_product_of_two([1, 2, 1, 3, 4]))
print(min_product_of_two([3, 4, 5, 2, 2]))
