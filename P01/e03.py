# 1.  Dada uma lista, retornar o elemento que esta a cabȩca (ou seja, na posicao 0).
def cabeca(lst):
    if not lst:
        return None
    return lst[0]


# 3.  Dado um par de listas com igual comprimento, produzir uma lista dos pares dos elementos homologos.
def homol(lst1, lst2):
    if not lst1 or not lst2:
        return None
    tup = (lst1[0], lst2[0])
    new_lst = homol(lst1[1:], lst2[1:])
    if new_lst is None:
        new_lst = []
    new_lst[:0] = [tup]
    return new_lst


# 4.  Dada uma lista de numeros, retorna o menor elemento.
def menor(lst):
    if not lst:
        return None
    n = lst[0]
    m = menor(lst[1:])
    if m is None or n < m:
        return n
    return m


print(cabeca([]))
print(homol([1,2], [3,4]))
print(menor([]))
