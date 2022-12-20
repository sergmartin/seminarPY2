"""Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
in
"Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

out

{'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}"""

name = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"


print(f"Вводный список: {name}")

name_dict = {}

for i in name:
    key = i[0]

    if key not in name_dict:
        name_dict[key] = []
    name_dict[key].append(i)

print (f"Словарь имен: {name_dict}")