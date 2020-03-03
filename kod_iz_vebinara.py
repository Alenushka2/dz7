#ЗАДАНИЕ 1
#1. В подпрограмме Мой банковский счет;
#2. Добавить сохранение суммы счета в файл.
#При первом открытии программы на счету 0
#После того как мы воспользовались программой и вышли сохранить сумму счета (35 минута вебинара)
#При следующем открытии программы прочитать сумму счета, которую сохранили
import os

FILE_NAME = 'orders.txt'

orders = []
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        for order in f:
            orders.append(order.replace('\n', ''))

while True:
    print('1. Добавить покупку')
    print('2. История покупок')
    print('3. Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        name = input('Введите название: ')
        orders.append(name)
    elif choise == '2':
        for order in orders:
            print(order)
    elif choise == '3':
        with open(FILE_NAME, 'w') as f:
            for order in orders:
                f.write(f'{order}\n')
        break
    else:
        print('Неправильно введены даные')