# Modulo: tree_search
# 
# Fornece um conjunto de classes para suporte a resolucao de 
# problemas por pesquisa em arvore:
#    SearchDomain  - dominios de problemas
#    SearchProblem - problemas concretos a resolver 
#    SearchNode    - nos da arvore de pesquisa
#    SearchTree    - arvore de pesquisa, com metodos para 
#                    a respectiva construcao
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2018,
#  Inteligência Artificial, 2014-2018

from abc import ABC, abstractmethod


# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal_state):
        pass


# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal


# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self, state, parent, depth=0):  # 2.2 Add depth field
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = 0
        self.heuristic = 0  # 2.11

    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + "," + str(self.depth) + "," + str(
            self.cost) + "," + str(self.heuristic) + ")"

    def __repr__(self):
        return str(self)


# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self, problem, strategy='breadth'):
        self.problem = problem
        root = SearchNode(problem.initial, None, 0)
        self.open_nodes = [root]
        self.strategy = strategy
        self.length = 0
        self.terminal = 0
        self.non_terminal = 1
        self.ramification = 0
        self.total_cost = 0
        self.higher_cost = []

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self, node):
        if node.parent is None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return path

    # procurar a solucao
    def search(self, limit=None):
        while self.open_nodes:
            node = self.open_nodes.pop(0)
            if self.problem.goal_test(node.state):
                # 2.6
                self.ramification = (self.terminal + self.non_terminal + 1) / self.non_terminal
                return str(self.get_path(node)) + \
                       "\nDepth: " + str(node.depth) + "\nLength: " + str(self.length) + \
                       "\nTerminal: " + str(self.terminal) + "\nNon Terminal: " + str(self.non_terminal) + \
                       "\nRatio: " + str(self.ramification) + \
                       "\nTotal Cost: " + str(self.get_total_cost(node)) + \
                       "\n" + str(node)

            if self.strategy == "depth" and limit is not None and node.depth >= limit:  # 2.4
                continue

            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state, a)

                # 2.1
                if newstate not in self.get_path(node):
                    newnode = SearchNode(newstate, node, node.depth + 1)
                    # 2.8
                    newnode.cost = self.problem.domain.cost(newstate, a)
                    # 2.12
                    newnode.heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                    lnewnodes += [newnode]
                    self.length += 1
                # 2.5
                self.non_terminal += len(lnewnodes)
                if not lnewnodes:
                    self.terminal += 1
                    self.non_terminal -= 1

            self.add_to_open(lnewnodes)
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self, lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            self.open_nodes = sorted(self.open_nodes + lnewnodes, key=lambda node: node.cost)  # 2.10
        elif self.strategy == 'greedy':
            self.open_nodes[:0] = sorted(lnewnodes, key=lambda node: node.heuristic)  # 2.13
        elif self.strategy == 'A*':
            self.open_nodes[:0] = sorted(lnewnodes, key=lambda node: node.heuristic + node.cost)  # 2.14

    # 2.9
    def get_total_cost(self, node):
        if not node:
            return 0
        return node.cost + self.get_total_cost(node.parent)
