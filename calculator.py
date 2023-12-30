import os
logo = '''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}
def calculator():
    print(logo)
    num_1 = float(input("Enter the first number: "))
    for key in operations:
        print(key)
    calc = True
    while calc:
        operator = input('Pick an operator: ')
        num_2 = float(input("Enter the next number: "))
        result = operations[operator](num_1, num_2)
        print(f"{num_1} {operator} {num_2} = {result}")
        cont = input(f"Do you want to continue calculating with {result}\nType 'y' to continue, \
'n' to start over or any other key to exit: ").lower()
        if cont == 'y':
            num_1 = result
        elif cont == 'n':
            calc = False
            os.system('clear')
            calculator()
        else:
            break
calculator()
                