def is_function(pairs): # множество для хранения аргументов
    arguments = set()

    for x, y in pairs: # Проверяем, если аргумент уже существует в множестве
        if x in arguments:
            return False
        arguments.add(x)  #добавляем аргумент в множество

    return True

print(is_function([(1, 3), (2, 5), (1, 7)]))
print(is_function([(1, 3)]))
print(is_function([(1, 3), (2, 5), (3, 7)]))