# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
x = int(input('ВВедите точку x не равную 0: '))
y = int(input('ВВедите точку y не равную 0: '))
if (x!=0)and(y!=0):
    if (x>0)and(y>0):
        print ('Первая четверть')
    elif (x>0)and(y<0):
        print ('Вторая четверть')
    elif (x<0)and(y>0):
        print ('Третья чеверть')
    else:
        print ('Четвертая четверть')
else:
    print('Читай условие, мешок с костями. Точка не может быть на оси.')