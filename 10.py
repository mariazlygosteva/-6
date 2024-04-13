def locate(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return "Прямоугольники лежат вне друг друга, не касаясь"

    if ((x2 == x3 and (y1 <= y4 <= y2 or y3 <= y1 <= y4))
            or (x4 == x1 and (y1 <= y4 <= y2 or y3 <= y1 <= y4))
            or (y2 == y3 and (x1 <= x4 <= x2 or x3 <= x1 <= x4))
            or (y4 == y1 and (x1 <= x4 <= x2 or x3 <= x1 <= x4))):
        return "Прямоугольники имеют касание"

    if ((x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2)
            or (x3 < x2 and x1 < x4 and y3 < y2 and y1 < y4)):
       return "Прямоугольники имеют пересечение"

    if ((x1 <= x3 and x4 <= x2 and y1 <= y3 and y4 <= y2)
        or (x3 <= x1 and x2 <= x4 and y3 <= y1 and y2 <= y4)):
        return "Один прямоугольник лежит внутри другого, не касаясь"

x1, y1 = map(int, input("Введите координаты верхней левой вершины первого прямоугольника (x1 y1): ").split())
x2, y2 = map(int, input("Введите координаты правой нижней вершины первого прямоугольника (x2 y2): ").split())
x3, y3 = map(int, input("Введите координаты верхней левой вершины второго прямоугольника (x3 y3): ").split())
x4, y4 = map(int, input("Введите координаты правой нижней вершины второго прямоугольника (x4 y4): ").split())

print(locate(x1, y1, x2, y2, x3, y3, x4, y4))
