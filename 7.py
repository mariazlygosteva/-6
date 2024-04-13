def can_order_sushi(K):
    for i in range(K // 7 + 1):
        for j in range(K // 5 + 1):
            if 5 * j + 7 * i == K:
                return 'Да'
    return 'Нет'

K = int(input('Введите количество суши (K): '))

print(can_order_sushi(K))
