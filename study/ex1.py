def f(x):
    if x == []:
        return 0
    if x[0] > 0:
        return x[0] + f(x[1:])
    return f(x[1:])

def g(x):
    if x == []:
        return [[]]
    y = g(x[1:])
    return y + [[x[0]] + z for z in y ]


