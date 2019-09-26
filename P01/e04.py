# ex1
import math

ex1 = lambda x: x % 2 == 0
print(ex1(2))

# ex2
ex2 = lambda x: x > 0
print(ex2(-1))

# ex3
ex3 = lambda x, y: abs(x) < abs(y)
print(ex3(1, -3))

# ex4
ex4 = lambda x, y: (math.sqrt(x ** 2 + y ** 2), math.atan2(y, x))
print(ex4(1, 2))


# ex5
def ex5(f, g, h):
    return lambda x, y, z: h(f(x, y), g(y, z))


print(ex5(lambda x, y: x + y, lambda x, y: x * y, lambda x, y: x - y)(1, 2, 3))


# ex6
def ex6(lst, f):
    if not lst:
        return True
    if f(lst[0]):
        return ex6(lst[1:], f)
    return False


print(ex6([1, 4, 3], lambda x: x <= 3))


# ex9
def ex9(lst, f, last):
    if not lst:
        return last
    return f(lst[0], ex9(lst[1:], f, last))


print(ex9([5, 2, 3], lambda x, y: x if x < y else y, 3))


# ex12
def ex12(lst, f):
    if not lst:
        return []
    new_lst = ex12(lst[1:], f)
    new_lst[:0] = [f(lst[0][0], lst[0][1])]
    return new_lst


print(ex12([(1, 2), (2, 1), (4, 1)], ex4))

# # ex13
# def ex13(lst1, lst2, f):
#
