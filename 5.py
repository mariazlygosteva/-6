def valid_knight_move(start_pos, end_pos):
    start_row = 8 - int(start_pos[1])
    start_col = 'abcdefgh'.index(start_pos[0])
    end_row = 8 - int(end_pos[1])
    end_col = 'abcdefgh'.index(end_pos[0])

    if ((abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1)
            or (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2)):
        return 'Верно'
    else:
        return 'Ошибка'

start_pos = input('Введите начальные координаты: ')
end_pos = input('Введите конечные координаты: ')

print(valid_knight_move(start_pos, end_pos))

