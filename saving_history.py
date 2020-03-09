import os
import json

FILE_NAME = 'saving_the_history.txt' #создаёт файл для сохранения списка покупок
# списки пусты или содержат последние сохранённые значениения
history = 0
historys = []

amount = 0
def buy (amount):
    cost = int(input('Enter purchase cost'))
    if cost > amount:
        print('There is not enough money in the account')
    else:
        amount -= cost
        history = input('Enter purchase name:')
        historys.append((history, cost))
    return amount
while True:
    print('1. refill')
    print('2. purchase')
    print('3. exit')

    choice = input('Select menu item:')
    if choice == '1':
        cost = int(input('Enter amount'))
        amount += cost
    elif choice == '2':
            amount = buy(amount)
            #with open ('saving_the_amount.txt', 'w') as f:
             # for amount in amounts:
               # json.dump(amount, f)
            #amount = json.load(f)
    elif choice == '3':
            print(history)
            if os.path.exists(FILE_NAME):
                # при открытии программы последнее сохранённое значение записывается в список
                with open(FILE_NAME, 'r') as f:
                    history = json.load(f)
                    for history in f:
                        historys.append(historys.replace('\n', ''))
            with open(FILE_NAME, 'w') as f:
               # for history in history:
                    json.dump(history, f)
    elif choice == '4':
        #print (amount)
     break
    else:
        print('Invalid menu item')

