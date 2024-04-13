def get_cell_color(letter, number):
    letters = 'abcdefgh'

    if letters.index(letter) % 2 == 0:
        return 'Белый' if number % 2 == 0 else 'Черный'
    else:
        return 'Черный' if number % 2 == 0 else 'Белый'

coordinates = input("Введите координаты клетки через пробел: ")
letter, number = coordinates.split()
number = int(number)

print(get_cell_color(letter, number))



