import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)

def circle_arrangement(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)

    if d > r1 + r2:
        return "Окружности лежат одна вне другой, не касаясь"
    elif d == r1 + r2:
        return "Окружности имеют внешнее касание"
    elif abs(r1 - r2) < d < r1 + r2:
        return "Окружности пересекаются"
    elif d == abs(r1 - r2):
        return "Окружности имеют внутреннее касание"
    else:
        return "Одна окружность лежит внутри другой, не касаясь"

x1 = float(input("Введите координату x центра первой окружности: "))
y1 = float(input("Введите координату y центра первой окружности: "))
r1 = float(input("Введите радиус первой окружности: "))

x2 = float(input("Введите координату x центра второй окружности: "))
y2 = float(input("Введите координату y центра второй окружности: "))
r2 = float(input("Введите радиус второй окружности: "))

print(circle_arrangement(x1, y1, r1, x2, y2, r2))
