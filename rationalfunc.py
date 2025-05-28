# code structure 
# *  f(x) = (x2 + x - 2) / (2x2 - 2x - 3) 
'''
1. we take the values from the user as q(x) and p(x) #! getvalues()
** make sure that the values are valid #! getvalues()
2. we split the terms over some list #! sfw()
3. we already have dictionary that has up to 10 keys #! sfw()
4. done, now we have dect for the n and the d, now we take the d and we get the zeros from it and done #! domain()
** we will do that for both n and d 
and lastly the main script that the code and all functions will be called in and it will be #! mainscript()
'''
def getvalues():
    validinputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'x', '+', '-']
    while True:
        px = input('Please Enter P(x): ')
        ispxvalid = True
        for i in px:
            if i not in validinputs:
                print('Invalid Input: Please Try Again')
                ispxvalid = False
            else:
                break
        if ispxvalid:
            break
                
    while True:
        qx = input('Please Enter Q(x): ')
        isqxvalid = True
        for i in px:
            if i not in validinputs:
                print('Invalid Input: Please Try Again')
                isqxvalid = False
            else:
                break
        if isqxvalid:
            break
    return px, qx

def sfw(px, qx):
    p_terms = px.split('+')
    q_terms = qx.split('+')
    p_dict = {}
    q_dict = {}
    for term in p_terms:
        if 'x' in term:
            coeff, power = term.split('x')
            p_dict[int(power)] = int(coeff)
        else:
            p_dict[0] = int(term)
    for term in q_terms:
        if 'x' in term:
            coeff, power = term.split('x')
            q_dict[int(power)] = int(coeff)
        else:
            q_dict[0] = int(term)
    return p_dict, q_dict
