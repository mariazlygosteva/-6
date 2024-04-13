import math

radius = 6.5

length = float(input('Введите длину ковровой дорожки (в метрах): '))
width = float(input('Введите ширину ковровой дорожки (в метрах): '))

diagonal = math.sqrt(length ** 2 + width ** 2)

if diagonal <= 2 * radius:
    print('Да')
else:
    print('Нет')