def can_throw_brick(A, B, C, D, E):
    if ((A >= C and B >= D) or (A >= D and B >= C) or (A >= C and B >= E)
        or (A >= E and B >= C) or (A >= D and B >= E) or (A >= E and B >= D)):
        return True
    else:
        return False

A = int(input('Введите ширину отверстия в дециметрах: '))
B = int(input('Введите высоту отверстия в дециметрах: '))
C = int(input('Введите длину кирпича в дециметрах: '))
D = int(input('Введите ширину кирпича в дециметрах: '))
E = int(input('Введите высоту кирпича в дециметрах: '))

if can_throw_brick(A, B, C, D, E):
    print('Бармалей может выбрасывать кирпичи через отверстие')
else:
    print('Бармалей не может выбрасывать кирпичи через отверстие')
