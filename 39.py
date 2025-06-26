def max_to_min(nums) :
    if not nums :
        return  # Если список пустой, ничего не делаем

    max_val = max(nums)
    min_val = min(nums)

    for i in range(len(nums)) :
        if nums[i] == max_val :
            nums[i] = min_val
data = [1, 3, 3, 3, 4]
max_to_min(data)
print(data)
data = [5, 4, 2, -2, 4, 2, 2, 5]
max_to_min(data)
print(data)
data = [1]
max_to_min(data)
print(data)
data = [1, 2, 1, 2, 1, 2]
max_to_min(data)
print(data)
data = [1, 1, 1, -1, 1, 1, 0]
max_to_min(data)
print(data)
data = [1, 1]
max_to_min(data)
print(data)