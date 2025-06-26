def sort_binary_list(binary_list):
    count_zero = 0
    count_one = 0
    for element in binary_list: # подсчёт количества нулей и единиц
        if element == 0:
            count_zero += 1
        elif element == 1:
            count_one += 1
        else:
            # в случае некорректных данных можно выбросить исключение или пропустить
            raise ValueError("Список содержит элементы, отличающиеся от 0 и 1.")

    # заполнение списка нулями и единицами по подсчёту
    for i in range(len(binary_list)):
        if i < count_zero:
            binary_list[i] = 0
        else:
            binary_list[i] = 1
binary_list = [0, 1, 1, 0, 1]
sort_binary_list(binary_list)
print(binary_list)
binary_list = [0, 0, 0, 0, 0]
sort_binary_list(binary_list)
print(binary_list)
binary_list = [1, 1, 1, 1, 1]
sort_binary_list(binary_list)
print(binary_list)
binary_list = [1]
sort_binary_list(binary_list)
print(binary_list)
binary_list = [0, 1]
sort_binary_list(binary_list)
print(binary_list)
binary_list = [0, 1, 0, 1]
sort_binary_list(binary_list)
print(binary_list)