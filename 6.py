N = int(input('Введите количество детей (N): '))
K = int(input('Введите вместимость карусели (K): '))
M = int(input('Введите длительность одного сеанса аттракциона в минутах (M): '))

total_rides = N * 2
num_sessions = round(total_rides / K)
total_time = num_sessions * M

print(f'Воспитателю потребуется минимум {total_time} минут, чтобы завершить культурное мероприятие.')
