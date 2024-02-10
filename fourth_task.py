min_val = ord('a')
max_val = ord('z') + 1

key_encoder = 1
str_my = "Helloy Worldz"


def upper_case_flag(val: str, flag: bool) -> str:
    return val.upper() if flag else val


def encoder(val: str, key: int) -> str:
    str_return = ""
    for i in val:
        flag_upper = i.isupper()
        if not i == " ":
            ord_element = ord(i.lower()) + key
            if ord_element >= max_val:
                str_return += upper_case_flag(chr((ord_element - max_val) + min_val), flag_upper)
            elif ord_element <= min_val:
                str_return += upper_case_flag(chr((ord_element + max_val) - min_val), flag_upper)
            else:
                str_return += upper_case_flag(chr(ord_element), flag_upper)
        else:
            str_return += " "
    return str_return


def decoder(val: str, key: int) -> str:
    return encoder(val, key * -1)


val_encoder = encoder(str_my, key_encoder)
print(val_encoder)
print(decoder(val_encoder, key_encoder))

print(list(range(ord('a'), ord('z'))))
print(list(chr(k) for k in range(ord('a'), ord('z') + 1)))
