def prin(varl, vall, vatl):
    print(varl)
    print(vall)
    print(vatl)


def ls(varl, vall):
    """Print all elements in variable list with their complement in value list.

    Keyword arguments:
    varl -- the list of variables
    vall -- the list of values
    """
    for i in range(len(varl)):
        print(varl[i], "=", vall[i])


def myPrint(y, varl, vall):
    """Print element y in variable list with their complement in value list.

    Keyword arguments:
    y    -- the element to print
    varl -- the list of variables
    vall -- the list of values
    """
    for i in range(len(y)):
        item = y[i]
        if "'" in item:
            item = item.replace("'", "")
            print(item)
        else:
            if item in varl:
                pos = varl.index(item)
                print(vall[pos])
            else:
                print("Invalid Variable:", item)
    print("")


def set(y, varl, vall, vatl):
    """Set element y in variable list with their complement in value list.

    Keyword arguments:
    y    -- the element to set
    varl -- the list of variables
    vall -- the list of values
    valt -- ???
    """
    if (len(y) != 3):
        print("Set uses 3 parameters, not", len(y))
    else:
        var = y[0]
        var = var.replace("'", "")
        print("Variable:", var)
        if (var in varl):
            vpos = varl.index(var)
            vall[vpos] = y[1]
            vatl[vpos] = y[2]
        else:
            varl.append(var)
            vall.append(y[1])
            vatl.append(y[2])


def math(y, varl, vatl):
    """Print y in variable list.

    Keyword arguments:
    y    -- the element to print
    varl -- the list of variables
    valt -- ???
    """
    for item in y:
        if item in varl:
            pos = varl.index(item)
            if vatl[pos] == "int":
                print('kk')
    print(int(y[0]) + int(y[1]))
