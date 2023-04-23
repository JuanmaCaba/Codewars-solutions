#Check the description to read the instructions for this task. Please,check it before going crazy over this code...

def makeNum(num, func=None):
    if func is None:
        return num
    else:
        return func(num)

def zero(func=None):
    return makeNum(0, func)

def one(func=None):
    return makeNum(1, func)

def two(func=None):
    return makeNum(2, func)

def three(func=None):
    return makeNum(3, func)

def four(func=None):
    return makeNum(4, func)

def five(func=None):
    return makeNum(5, func)

def six(func=None):
    return makeNum(6, func)

def seven(func=None):
    return makeNum(7, func)

def eight(func=None):
    return makeNum(8, func)

def nine(func=None):
    return makeNum(9, func)

def plus(x):
    return lambda y: y + x

def minus(x):
    return lambda y: y - x

def times(x):
    return lambda y: y * x

def divided_by(x):
    return lambda y: y // x
