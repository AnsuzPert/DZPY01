# Напишите программу, которая по заданному 
# номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
per1 = int(input('ВВедите номер четверти (Число от 1 до 4):  '))
if per1 in range(1,5):
    if per1 == 1:
        print('x = (от нуля до бесконечности) и y = (от нуля до бесконечности)')
    elif per1 == 2:
        print('x = (от нуля до бесконечности) и y = (от нуля до -бесконечности)')
    elif per1 == 3:
        print('x = (от нуля до -бесконечности) и y = (от нуля до бесконечности)')
    else:
        print('x = (от нуля до -бесконечности) и y = (от нуля до -бесконечности)')
else: 
    print('Попрошу открыть гляделки и/или использовать их по назначению')

