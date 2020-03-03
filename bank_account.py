bill_sum = 0
history = []

def buy (bill_sum):
    cost = int(input('Enter purchase cost'))
    if cost > bill_sum:
        print('There is not enough money in the account')
    else:
        bill_sum -= cost
        name = input('Enter purchase name:')
        history.append((name, cost))
    return bill_sum


while True:
    print('1. refill')
    print('2. purchase')
    print('3. purchase hystory')
    print('4. exit')

    choice = input('Select menu item:')
    if choice == '1':
        cost = int(input('Enter amount'))
        bill_sum += cost
    elif choice == '2':
        bill_sum = buy(bill_sum)
    elif choice == '3':
        print (history)

    elif choice == '4':
        break
    else:
        print('Invalid menu item')