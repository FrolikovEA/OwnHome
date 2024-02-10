str_user_input = input("Введите строку : ")
if str_user_input.isdigit():
    print("Вы ввели не строку")


def convertToSnakeCase(val: str) -> str:
    new_str = ""
    index_for = 0
    for ch in val:
        if ch.isupper():
            new_str += ("_" if index_for > 0 else "") + ch.lower()
        else:
            new_str += ch
        index_for += 1
    return new_str


def convertToCamelCase(val: str) -> str:
    list_split_str = [k.title() for k in val.split("_")]
    return "".join(list_split_str)


if str_user_input.find("_") > 0:
    print(convertToCamelCase(str_user_input))
else:
    print(convertToSnakeCase(str_user_input))
