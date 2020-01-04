from constraintsearch import *


def queen_constraint(r1, c1, r2, c2):
    l1 = int(r1[1:])
    l2 = int(r2[1:])
    if c1 == c2:
        return False
    if abs(l1 - l2) == abs(c1 - c2):
        return False
    return True


def make_constraint_graph(n):
    queens = ['R' + str(i + 1) for i in range(n)]
    return {(X, Y): queen_constraint for X in queens for Y in queens if X != Y}


def make_domains(n):
    queens = ['R' + str(i + 1) for i in range(n)]
    cols = [i + 1 for i in range(n)]
    return {r: cols for r in queens}


cs = ConstraintSearch(make_domains(4), make_constraint_graph(4))

print(cs.search())

###################################################
# Guiao TP - IV.4
###################################################


func = lambda r1, c1, r2, c2: c1 != c2


def make_domains_4(n: int, c: int) -> dict:
    regions = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    regions = regions[0:n]
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    return {r: colors[0:c] for r in regions}


def make_constraint_graph(mapa: dict) -> dict:
    return {(X, Y): func for X in mapa for Y in mapa[X]}


alinea_a = {'A': 'BED', 'B': 'AEC', 'C': 'BED', 'D': 'AEC', 'E': 'ABCD'}
alinea_b = {'A': 'BED', 'B': 'AEC', 'C': 'BEF', 'D': 'AEF', 'E': 'ABCDF', 'F': 'DEC'}
alinea_c = {'A': 'BEFD', 'B': 'AFC', 'C': 'BFGD', 'D': 'AEGC', 'E': 'ADFG', 'F': 'AEBCG', 'G': 'DEFC'}

cs_a = ConstraintSearch(make_domains_4(5, 3), make_constraint_graph(alinea_a))
cs_b = ConstraintSearch(make_domains_4(6, 4), make_constraint_graph(alinea_b))
cs_c = ConstraintSearch(make_domains_4(7, 4), make_constraint_graph(alinea_c))

print(cs_a.search())
print(cs_b.search())
print(cs_c.search())

###################################################
# Guiao TP - V.5
###################################################

friends = ['Andre', 'Bernardo', 'Claudio']


def make_friends(f):
    return {a: [(c, b) for c in f for b in f] for a in f}


def constraints_friends(a1, t1, a2, t2):
    c1, b1 = t1
    c2, b2 = t2

    if a1 in [c1, b1] or a2 in [c2, b2]:
        return False

    if c1 == b1 or c2 == b2:
        return False

    if c1 == "Claudio" and b1 != "Bernardo":
        return False

    return True


def make_constraints_friends(f):
    return {(X, Y): constraints_friends for X in f for Y in f}


cs = ConstraintSearch(make_friends(friends), make_constraints_friends(friends))

print(cs.search())

###############################################################################
# Guiao TP - III.10
###############################################################################

