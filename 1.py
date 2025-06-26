def calculate(vars, values, exp):
    mapping = {var: val for var, val in zip(vars, values)} #создаем словарь сопоставления переменных и их значений
    expr = ''  #строка для выражения значений
    for ch in exp:
        if ch in mapping:  #если тек. сим. переменная заменяем ее значением
            expr += str(mapping[ch])
        else:
            expr += ch #оставляем без измен
    return eval(expr)

print(calculate('xyz', [1, 2, 3], 'x-y+z'))             # 1 - 2 + 3 = 2
print(calculate('dbcw', [3, 0, -2, -3], '-d-c-b+w'))    # -3 - (-2) - 0 - 3 = -4
print(calculate('abcd', [0, 0, 0, 0], 'a+b+c+d'))       # 0 + 0 + 0 + 0 = 0
print(calculate('a', [4], 'a'))                         # 4 = 4