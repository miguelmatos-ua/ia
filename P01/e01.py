a = [1, 2, 3, 4, 5, 6, 7]
b = ["a", "b", "c"]
c = [1, 2, 3, 2, 1]
d = [a, b, c]
e = [4, 6, 8]


# 1. Dada uma lista, retorna o seu comprimento
def ex1(lst):
    if not lst:
        return 0
    return 1 + ex1(lst[1:])


# 2.  Dada uma lista de numeros, retorna a respectiva soma
def ex2(lst):
    if not lst:
        return 0
    return lst[0] + ex2(lst[1:])


# 3.  Dada uma lista e um elemento, verifica se o elemento ocorre na lista.  Retorna um valor booleano.
def ex3(lst, i):
    if not lst:
        return False
    if lst[0] == i:
        return True
    return ex3(lst[1:], i)


# 4.  Dadas duas listas, retorna a sua concatenação.
def ex4(lst1, lst2):
    if not lst1:
        return lst2[:]
    new_lst = ex4(lst1[1:], lst2)
    new_lst[:0] = [lst1[0]]
    return new_lst


# 5.  Dada uma lista, retorna a sua inversa.
def ex5(lst):
    if not lst:
        return []
    new_lst = ex5(lst[:-1])
    new_lst[:0] = [lst[-1]]
    return new_lst


# 6.  Dada uma lista, verifica se forma uma capicua, ou seja, se, quer se leia da esquerda para a direita ou
# vice-versa, se obtem a mesma sequencia de elementos
def ex6(lst):
    if not lst:
        return True
    if lst[0] == lst[-1]:
        return ex6(lst[1:-1])
    return False


# 7.  Dada uma lista de listas, retorna a concatenacao dessas listas.
def ex7(lst):
    if not lst:
        return []
    new_lst = ex7(lst[1:])
    new_lst[:0] = lst[0]
    return new_lst


# 8.  Dada uma lista,  um elemento x e outro elemento y,  retorna uma lista similar a lista de entrada, na qual x e
# substituido por y em todas as ocorrencias de x.
def ex8(lst, x, y):
    if not lst:
        return []
    if lst[0] == x:
        lst[0] = y
    new_lst = ex8(lst[1:], x, y)
    new_lst[:0] = [lst[0]]
    return new_lst


# 9.  Dadas duas listas ordenadas de numeros, calcular a uniao ordenada mantendo eventuais repeticoes.
def ex9(lst1, lst2):
    if not lst1:
        return lst2[:]
    if not lst2:
        return lst1[:]
    if lst1[0] != lst2[0]:
        new_lst = ex9(lst1[1:], lst2)
    else:
        new_lst = ex9(lst1, lst2[1:])
    new_lst[:0] = [lst1[0]]
    return new_lst


# TODO: 10.  Dado  um  conjunto,  na  forma  de  uma  lista,  retorna  uma  lista  de  listas  que  representa  o
#  conjunto de todos os subconjuntos do conjunto dado.
def ex10(conj):
    if not conj:
        return []
    return 0


print(ex1(a))
print(ex2(a))
print(ex3(a, 3))
print(ex4(a, b))
print(ex5(a))
print(ex6(c))
print(ex7(d))
print(ex8(a, 3, 13))
print(ex9(a, e))
