import math

str_square_leveling = input("введите квадратное уравнение: ")

part_str = str_square_leveling.replace(" ", "").split("=")
if len(part_str) != 2 or part_str[1] != '0':
    print("Вы ввели не квадродное уровнение")

list_square_element = []
str_after_equals = part_str[0]
for i in str_after_equals.split("+"):
    if i.find("-") >= 0:
        list_square_element.extend(k for k in i.split("-") if k != '')
    else:
        list_square_element.append(i)

before_find = 0
for i in range(len(list_square_element)):
    print(list_square_element[i])
    find_index = str_after_equals.find(list_square_element[i], before_find + 1)
    before_find = find_index
    if (find_index - 1) >= 0:
        list_square_element[i] = str_after_equals[find_index - 1] + ';' + list_square_element[i]
    else:
        list_square_element[i] = '+;' + list_square_element[i]


def clear_val_and_convert_to_int(val: str) -> int:
    val_after_replace = val.replace("x**2", '').replace("*x", '').replace(";", '')
    if val_after_replace == "-":
        val_after_replace = '-1'
    elif val_after_replace == '+':
        val_after_replace = "+1"
    return int(val_after_replace)


def count_simvol(val: str):
    return val.count("*")


# защита от того если элементы перепутаны местами
a, b, c = map(clear_val_and_convert_to_int, sorted(list_square_element, key=count_simvol, reverse=True))

determinant = (b * b) - (4 * a * c)

if determinant < 0:
    print("уровнение не имеет корней")
elif determinant > 0:
    x1 = (-b - math.sqrt(determinant)) / 2 * a
    x2 = (-b + math.sqrt(determinant)) / 2 * a
    print(f"x_1={x1:.2f}")
    print(f"x_2={x2:.2f}")
elif determinant == 0:
    x1 = (-b - math.sqrt(determinant)) / 2 * a
    print(f"x={x1:.2f}")
