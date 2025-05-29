import re

# *  f(x) = (x2 + x - 2) / (2x2 - 2x - 3) 

def getvalues():
    validinputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'x', '+', '-', '^']
    essentialinputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'x']
    while True:
        px = input('Please Enter P(x): ').replace(" ", "")
        ispxvalid = True
        for i in px:
            if i not in validinputs:
                print('Invalid Input: Please Try Again')
                ispxvalid = False
                break
        if ispxvalid:
            break

    while True:
        qx = input('Please Enter Q(x): ').replace(" ", "")
        isqxvalid = True
        for i in qx:
            if i not in validinputs:
                print('Invalid Input: Please Try Again')
                isqxvalid = False
                break
        if isqxvalid:
            break
    return px, qx

def zeros(px: str, qx: str):
    #! 2x^2
    px.replace("^", "**")
    qx.replace("^", "**")
    px.replace("x", "")
    return



    





