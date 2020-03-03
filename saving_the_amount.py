import os
import json

FILE_NAME = 'saving_the_amount.txt' #создаёт файл для сохранения счёта
FILE_NAME1 = 'saving_the_history.txt' #создаёт файл для сохранения списка покупок
# списки пусты или содержат последние сохранённые значениения
amount = 0
amounts = []
historys = []
# при открытии программы последнее сохранённое значение записывается в список

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        amount = json.load(f)
        #for amount in f:
         #   amount.append(amount.replace('\n', ''))

if os.path.exists(FILE_NAME1):
    with open(FILE_NAME1, 'r') as f1:
        history = json.load(f1)
        #for history in f:
         #   historys.append (historys.replace('\n', ''))

def buy (amount):
    cost = int(input('Enter purchase cost'))
    if cost > amount:
        print('There is not enough money in the account')
    else:
        amount -= cost
        name = input('Enter purchase name:')
        historys.append((name, cost))
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
            with open ('saving_the_amount.txt', 'w') as f:
             # for amount in amounts:
                json.dump(amount, f)
            #amount = json.load(f)
    elif choice == '3':
            print(history)
            with open(FILE_NAME1, 'w') as h:
               # for history in history:
                    json.dump(history, f1)
    elif choice == '4':
        #print (amount)
     break
    else:
        print('Invalid menu item')
