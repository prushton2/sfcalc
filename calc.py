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

        if (x == 'reset'):
            ln = 0
            reset()
        elif (x == 'prin'):
            print(varl)
            print(vall)
            print(vatl)
        elif (x == 'ls'):
            for i in range(len(varl)):
                print(varl[i], "=", vall[i])

        elif (x == "print"):
            for i in range(len(y)):
                item = y[i]
                if "'" in item:
                    item = item.replace("'", "")
                    print(item, end=" ")
                else:
                    if item in varl:
                        pos = varl.index(item)
                        print(vall[pos], end=" ")
                    else:
                        print("Invalid Variable:", item)
            print("")

        elif (x == "set"):
            if (len(y) != 3):
                print("Set uses 3 parameters, not", len(y))
            else:
                var = y[0]
                var = var.replace("'", "")
                dprint("Variable:", var)
                if (var in varl):
                    vpos = varl.index(var)
                    vall[vpos] = y[1]
                    vatl[vpos] = y[2]
                else:
                    varl.append(var)
                    vall.append(y[1])
                    vatl.append(y[2])

        elif (x == 'math'):
            for item in y:
                if item in varl:
                    pos = varl.index(item)
                    if vatl[pos] == "int":
                        print('kk')
            print(int(y[0]) + int(y[1]))


    except:
        print("Either an internal error occurred, or a user error occurred")
        print("Error on input line:", ln - 1, "command:", txt)