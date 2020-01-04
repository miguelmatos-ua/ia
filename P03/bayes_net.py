from itertools import product


class BayesNet:

    def __init__(self, ldep=None):  # Why not ldep={}? See footnote 1.
        if not ldep:
            ldep = {}
        self.dependencies = ldep

    # Os dados estao num dicionario (var,dependencies)
    # em que as dependencias de cada variavel
    # estao num dicionario (mothers,prob);
    # "mothers" e' um frozenset de pares (mothervar,boolvalue)
    def add(self, var, mothers, prob):
        self.dependencies.setdefault(var, {})[frozenset(mothers)] = prob

    # Probabilidade conjunta de uma dada conjuncao 
    # de valores de todas as variaveis da rede
    def jointProb(self, conjunction):
        prob = 1.0
        for (var, val) in conjunction:
            for (mothers, p) in self.dependencies[var].items():
                if mothers.issubset(conjunction):
                    prob *= (p if val else 1 - p)
        return prob

    def ancestors(self, var, start=True):
        mothers = [v for (v, b) in list(self.dependencies[var].keys())[0]]
        ancestors = [] if start else [var]
        for v in mothers:
            ancestors += self.ancestors(v, False)
        return list(set(ancestors))

    def conjuctions1(self, listvars):
        if len(listvars) == 1:
            return [[(listvars[0], True)], [(listvars[0], False)]]
        lst = []
        for r in self.conjuctions1(listvars[1:]):
            lst.append(r + [(listvars[0], True)])
            lst.append(r + [(listvars[0], False)])
        return lst

    def conjuctions2(self, listvars):
        combinations = product([True, False], repeat=len(listvars))
        return [list(zip(listvars, c)) for c in combinations]

    def individual_prob(self, var, val):
        s = 0.0
        for c in self.conjuctions2(self.ancestors(var)):
            s += self.jointProb([(var, val)] + c)
        return s

# Footnote 1:
# Default arguments are evaluated on function definition,
# not on function evaluation.
# This creates surprising behaviour when the default argument is mutable.
# See:
# http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments
