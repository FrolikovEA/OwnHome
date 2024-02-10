str_user_input = input("Введите число : ")
if not str_user_input.isdigit():
    print("Вы ввели не число")

groups_nums = []
while str_user_input:
    groups_nums.append(str_user_input[-3:])
    str_user_input = str_user_input[:-3]

print(' '.join(reversed(groups_nums)))
