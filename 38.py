def can_nest(nums1, nums2) :
    min1, max1 = min(nums1), max(nums1)
    min2, max2 = min(nums2), max(nums2)

    nest_1_in_2 = (min1 > min2) and (max1 < max2)

    nest_2_in_1 = (min2 > min1) and (max2 < max1)

    return nest_1_in_2 or nest_2_in_1
print(can_nest([1, 2, 3, 4], [0, 6]))     # первый список можно вложить во второй
print(can_nest([4, 0], [3, 1]))           # второй список можно вложить в первый
print(can_nest([1, 2, 3, 4], [2, 3]))     # второй список можно вложить в первый
print(can_nest([9, 9, 8], [8, 9]))        # минимумы и максимумы списков совпадают
print(can_nest([1], [1]))                 # минимумы и максимумы списков совпадают
print(can_nest([-1, 1, -2], [-3, 2, 0]))  # первый список можно вложить во второй
