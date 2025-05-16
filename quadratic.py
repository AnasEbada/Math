import sys
import math

def input_coeff(name):
    while True:
        value = input(f"{name}: ")
        if value.lower == 'exit':
            print("Exiting program.")
            sys.exit()
        if value.lower == 'restart':
            continue
        try:
            fvalue = float(value)
        except ValueError:
            print('Invalid input for a1: numbers only. Please try again.')
            continue
        return fvalue
    
def solve(a, b, c):
    delta = ((b)**2) - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt((delta))) / (2*a)
        return x1, x2
    if delta == 0:
        x = (-b + math.sqrt((delta))) / (2*a)
        return x
    if delta < 0:
        return None
    
print('=' * 20)
print('Quadratic Equation Solver')
print('=' * 20)
print('\nEnter the coefficients for the system:')
print('  y = aX2 + bY + c = 0')
print('Type "exit" at any prompt to quit.')
print("-" * 20)

def mainscript():
    while True:
        a = input_coeff('a')
        if a == 0:
            print("Invalid Coefficient: Cannot Equal To Zero")
            continue
        else:
            break
    b = input_coeff('b')
    c = input_coeff('c')

    print('\n System Entered: ')
    if a == 1: 
        print(f"   X2  {'-' if b <= -1 else '+'}  {abs(int(b))}Y   {'-' if c <= -1 else '+'}   {abs(int(c))}  =  0")
    elif a == -1:
        print(f"   -X2  {'-' if b <= -1 else '+'}  {abs(int(b))}Y   {'-' if c <= -1 else '+'}   {abs(int(c))}  =  0")
    else:
        print(f"   {int(a)}X2  {'-' if b <= -1 else '+'}  {abs(int(b))}Y   {'-' if c <= -1 else '+'}   {abs(int(c))}  =  0")

    roots = solve(a, b, c)
    print(f"Solution is: ")
    if roots == None:
        print(roots)
        print("No Solution For The Equation")
    else:
        print(roots)

mainscript()

while True:
    continueornot = input('Another Equation (yes / no)? ')
    if continueornot == "yes".lower():
        print('\n'+'-'*20+'\n')
        mainscript()
    elif continueornot == "no".lower():
        print("Exiting program.")
        sys.exit()
    else:
        print('Invalid Input: Please Enter "yes" Or "no"')
