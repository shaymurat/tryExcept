def add_everything_up(a, b):
    '''складывает числа (int, float) и строки (str)'''
    try:
        sum = a + b
    except TypeError:
        # все типы конвертировать в str
        sum = str(a) + str(b)

        # или только str, int и float
        # if {type(a).__name__, type(b).__name__}.issubset(
        #         {'str', 'int', 'float'}):
        #     sum = str(a) + str(b)
        # else:
        #     # на все остальные ретранслировать исключение
        #     raise

    return sum


if __name__ == '__main__':
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
