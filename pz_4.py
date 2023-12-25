heigh = int(input('Введите длинну прямоугольника: '))
width = int(input('Введите ширину прямоугольника: '))

for i in range(heigh):
    for j in range(width):
        if i == 0 or i == heigh - 1 or j == 0 or j == width - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print( )    