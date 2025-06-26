def get_oldest(ages):
    max_age = -1
    oldest_name = None

    for name, age in ages.items():
        if age > max_age:
            max_age = age
            oldest_name = name
        elif age == max_age:
            if name < oldest_name:
                oldest_name = name
    return oldest_name
print(get_oldest({'Тимур': 31, 'Валерий': 34, 'Артур': 24, 'Анастасия': 28, 'Антон': 21, 'Сослан': 27}))
print(get_oldest({'Лариса': 35, 'Антон': 21, 'Сослан': 27, 'Тимур': 31, 'Артур': 41}))
print(get_oldest({'Тимур': 31}))
print(get_oldest({'Лариса': 18, 'Анастасия': 18}))
print(get_oldest({'Пантелеймон': 34, 'Нина': 34, 'Любовь': 25, 'Станислав': 34}))
print(get_oldest({'Елисей': 49, 'Сидор': 31, 'Василиса': 21, 'Мирон': 40, 'Юрий': 26}))
