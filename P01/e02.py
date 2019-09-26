# ex1
def separa(lst):
    if not lst:
        return [], []
    a, b = lst[0]
    lst1, lst2 = separa(lst[1:])
    return [a] + lst1, [b] + lst2


# ex2
def remove_e_conta(l, x):
    if not l:
        return [], 0
    r, c = remove_e_conta(l[1:], x)
    if l[0] == x:
        return r, c + 1
    return [l[0]] + r, c


print(separa([(1, 2), (5, 3), (8, 0)]))
print(remove_e_conta([1, 6, 2, 5, 5, 2, 5, 2], 2))
