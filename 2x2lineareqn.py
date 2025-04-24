import sys

def take_input():
    print('\nEnter the coefficients for the system:')
    print('  a1*x + b1*y = c1')
    print('  a2*x + b2*y = c2')
    print('Type "exit" at any prompt to quit.')
    print('Type "restart" at any prompt to restart putting inputs.')
    print("-" * 20)
    while True:
        a1input = input('a1: ')
        if a1input.lower() == 'exit':
            print("Exiting program.")
            sys.exit()
        if a1input.lower() == 'restart':
            continue
        try:
            fa1 = float(a1input)
        except ValueError:
            print('Invalid input for a1: numbers only. Please try again.')
            continue

        b1input = input('b1: ')
        if b1input.lower() == 'exit':
            print("Exiting program.")
            sys.exit()
        try:
            fb1 = float(b1input)
        except ValueError:
            print('Invalid input for b1: numbers only. Please try again.')
            continue

        d1input = input('d1: ')
        if d1input.lower() == 'exit':
            print("Exiting program.")
            sys.exit()
        try:
            fd1 = float(d1input)
        except ValueError:
            print('Invalid input for d1: numbers only. Please try again.')
            continue

        a2input = input('a2: ')
        if a2input.lower() == 'exit':
            print("Exiting program.")
            sys.exit()
        try:
            fa2 = float(a2input)
        except ValueError:
            print('Invalid input for a2: numbers only. Please try again.')
            continue       

        b2input = input('b2: ')     
        if b2input.lower() == 'exit':
            print("Exiting program.")
            sys.exit()
        try:
            fb2 = float(b2input)
        except ValueError:
            print('Invalid input for b2: numbers only. Please try again.')
            continue

        d2input = input('d2: ')
        if d2input.lower() == 'exit':
            print("Exiting program.")
            sys.exit()
        try:
            fd2 = float(d2input)
        except ValueError:
            print('Invalid input for d2: numbers only. Please try again.')
            continue

        return fa1, fb1, fd1, fa2, fb2, fd2

def check_if_solvable(ca1, cb1, cd1, ca2, cb2, cd2):
    if ca1 == 0 or cb1 == 0 or cd1 == 0 or ca2 == 0 or cb2 == 0 or cd2 == 0:
        print('One or more coefficients are zero, which makes the system unsolvable.')
        return False
    diva = ca1 / ca2
    divb = cb1 / cb2
    divd = cd1 / cd2
    # if a1 / a2 = b1 / b2 then slopes are equal, that means lines are parallel.
    # if a1 / a2 = b1 / b2 = d1 / d2 then slopes and y intrecepts are equal, that means lines are stacked over.
    if diva == divb:
        if divd == divb:
            print('The two lines are coincident: there are an unlimited number of solutions.')
            return False
        else:
            print('The two lines are parallel: there is no solution.')
            return False
    else: 
        return True

def solve(sa1, sb1, sd1, sa2, sb2, sd2):
    # sa1X + sb1Y = Sd1
    # sa2X + sb2Y = sd2 (those change later)
    mulnum = -1 * sa1 / sa2
    sa2, sb2, sd2 = mulnum * sa2, mulnum * sb2, mulnum * sd2
    nb, nd = sb2 + sb1, sd2 + sd1
    y = nd / nb
    xma = (-1 * sb1 * y) + sd1
    x = xma / sa1
    return x, y
# done


def mainscript():
    print('=' * 20)
    print('Linear Equation Solver')
    print('=' * 20)

    a1, b1, d1, a2, b2, d2 = take_input()
    
    if a1 != 0 or b1 != 0 or d1 != 0 or a2 != 0 or b2 != 0 or d2 != 0:
            print('\n System Entered: ')
            print(f'   {int(a1)}X  {'-' if b1 <= -1 else '+'}  {abs(int(b1))}Y   =   {int(d1)}')
            print(f'   {int(a2)}X  {'-' if b2 <= -1 else '+'}  {abs(int(b2))}Y   =   {int(d2)}')

    if check_if_solvable(a1, b1, d1, a2, b2, d2):
        x, y = solve(a1, b1, d1, a2, b2, d2)
        print(f'\n x  =  {x}\n y = {y}')

mainscript()
while true:
    continueornot = input('Another Equation (yes / no)? ')
    if continueornot == "yes".lower():
        print('\n'+'-'*20+'\n')
        mainscript()
    elif continueornot == "no".lower():
        print("Exiting program.")
        sys.exit()
    else:
        print('Invalid Input: Please Enter "yes" Or "no"')
    
