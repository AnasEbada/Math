def add(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')

def sub(num1, num2):
    print(f'{num1} - {num2} = {num1 - num2}')

def mul(num1, num2):
    print(f'{num1} × {num2} = {num1 * num2}')

def div(num1, num2):
    if num2 == 0:
        print("Error: Can't divide by zero.")
    else:
        print(f'{num1} ÷ {num2} = {num1 / num2}')

def input_num():
    while True:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            return num1, num2
        except ValueError:
            print("Invalid input: ONLY NUMBERS PLEASE")

def choose_op():
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input('Choose your operation (1/2/3/4/5): ')
        if choice.isdigit():
            int_choice = int(choice)
            if 1 <= int_choice <= 5:
                return int_choice
        print("Invalid choice: Please enter a number between 1 and 5.")

def calculator():
    while True:
        final_choice = choose_op()
        if final_choice == 5:
            print("Exiting calculator. Goodbye!")
            break

        number1, number2 = input_num()

        if final_choice == 1:
            add(number1, number2)
        elif final_choice == 2:
            sub(number1, number2)
        elif final_choice == 3:
            mul(number1, number2)
        elif final_choice == 4:
            div(number1, number2)

calculator()
def add(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')

def sub(num1, num2):
    print(f'{num1} - {num2} = {num1 - num2}')

def mul(num1, num2):
    print(f'{num1} × {num2} = {num1 * num2}')

def div(num1, num2):
    if num2 == 0:
        print("Error: Can't divide by zero.")
    else:
        print(f'{num1} ÷ {num2} = {num1 / num2}')

def input_num():
    while True:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            return num1, num2
        except ValueError:
            print("Invalid input: ONLY NUMBERS PLEASE")

def choose_op():
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input('Choose your operation (1/2/3/4/5): ')
        if choice.isdigit():
            int_choice = int(choice)
            if 1 <= int_choice <= 5:
                return int_choice
        print("Invalid choice: Please enter a number between 1 and 5.")

def calculator():
    while True:
        final_choice = choose_op()
        if final_choice == 5:
            print("Exiting calculator. Goodbye!")
            break

        number1, number2 = input_num()

        if final_choice == 1:
            add(number1, number2)
        elif final_choice == 2:
            sub(number1, number2)
        elif final_choice == 3:
            mul(number1, number2)
        elif final_choice == 4:
            div(number1, number2)

calculator()
