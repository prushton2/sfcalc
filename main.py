debug = False #A debug mode that will print any messages using the dprint command


def dprint(ipt):   #ipt = input, use as a tuple
    if (debug):
        print('DEBUG:', ipt)


def math(ipt):   #input a string in the format of '10 + 5'
    dprint(ipt)
    problem = ipt.split(" ")  #creates problem as a list of ipt split up at each ' '
    problem2 = []
    operator = None
    for i in problem:
        try:     #looks for integers and prints them
            float(i)
            dprint(('integer found:', float(i)))
            problem2.append(float(i))
        except:
            dprint(('Non integer found', i))
            operator = i
    if operator == '+':
        return problem2[0] + problem2[1]
    elif operator == '-':
        return problem2[0] - problem2[1]
    elif operator == '*':
        return problem2[0] * problem2[1]
    elif operator == '/':
        return problem2[0] / problem2[1]
    else:
        return("Invalid Operator")


print(math('5 + 10'))



