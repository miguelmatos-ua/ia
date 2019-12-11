# Miguel C. Matos
# 89124

from bayes_net import *
from semantic_network import *


class MySN(SemanticNetwork):
    def __init__(self, ldecl=None):
        if ldecl is None:
            ldecl = []
        super().__init__(ldecl)

    def query_dependents(self, entity):
        dep = [self.query_dependents(d.relation.entity1) for d in self.declarations if
               d.relation.entity2 == entity and (isinstance(d.relation, Depends) or isinstance(d.relation, Subtype))]
        deps = [d.relation.entity1 for d in self.declarations if
                d.relation.entity2 == entity and (isinstance(d.relation, Depends))]

        ret = list(set([item for sublist in dep for item in sublist] + deps))
        for r in ret:
            for d in self.query_local(e2=r, rel="subtype"):
                ret.append(d.relation.entity1)
                if d.relation.entity2 in ret:
                    ret.remove(d.relation.entity2)
        return list(set(ret))

    def query_causes(self, entity):
        dep = [self.query_causes(d.relation.entity2) for d in self.declarations if
               d.relation.entity1 == entity and (isinstance(d.relation, Depends) or isinstance(d.relation, Subtype))]

        deps = [d.relation.entity2 for d in self.declarations if
                d.relation.entity1 == entity and isinstance(d.relation, Depends)]

        return list(set([item for sublist in dep for item in sublist] + deps))

    def query_causes_sorted(self, entity):
        dep = self.query_causes(entity)
        ret = [(d.relation.entity1, d.relation.entity2) for d in self.declarations if
               isinstance(d.relation, Association) and d.relation.name == "debug_time" and d.relation.entity1 in dep]

        dic = dict()
        for r in ret:
            key, val = r
            dic.setdefault(key, []).append(val)

        lst = []
        for name in dic:
            lst.append((name, sum(dic[name]) / len(dic[name])))
        lst = sorted(lst, key=lambda x: x[1])
        return lst


class MyBN(BayesNet):

    def markov_blanket(self, var):
        par = self.dependencies.get(var)

        # Dependents of var
        deps = list(set([t[0] for f in par for t in f]))
        # var depends of
        lst = list(set([d for d in self.dependencies for i in self.dependencies[d] for j in i if j[0] == var]))
        # Dependents of what var depends of
        lst_deps = list(set([t[0] for l in lst for f in self.dependencies[l] for t in f if t[0] != var]))

        return deps + lst + lst_deps
