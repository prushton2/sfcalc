import main

varl = ['x']
vall = ["'1'"]
vatl = ["int"]
ln = 0

debug = 1


def dprint(x, y):
    if debug == 1:
        print("DEBUG:", x, y)


def reset():
    global varl
    global vall
    varl = []
    vall = []


while (1):
    txt = input("ln[" + str(ln) + "]>")
    ln += 1

    try:
        x = txt.split("(")
        y = x[1]
        y = y.replace(")", "")
        x = x[0]
        y = y.split(",")

        dprint("Command:", x)
        dprint("Parameters:", y)

        if x == 'reset':
            ln = 0
            reset()
        elif x == 'prin':
            main.prin(varl, vall, vatl)
        elif x == 'ls':
            main.ls(varl, vall)
        elif x == "print":
            main.myPrint(y, varl, vatl)
        elif x == "set":
            main.set(y, varl, vall, vatl)
        elif x == 'math':
            main.math(y, varl, vatl)

    except:
        print("Either an internal error occurred, or a user error occurred")
        print("Error on input:", ln - 1, "command:", txt)
