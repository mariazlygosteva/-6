def cordon_of_blocks(dimensions, number_quarter):
    width, height = map(int, dimensions.split())

    if number_quarter <= width * height and (
            number_quarter % width == 0 or number_quarter % height == 0):
        return 'Успешно'
    else:
        return 'Неосуществимо'

dimensions = input('Введите размеры оцепления района (в формате N×M): ')
number_quarter = int(input('Введите количество кварталов для отделения: '))

print(cordon_of_blocks(dimensions, number_quarter))