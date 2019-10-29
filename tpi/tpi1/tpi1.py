# Miguel Matos
# 89124

from tree_search import *


class MyNode(SearchNode):
    def __init__(self, state, parent):
        super().__init__(state, parent)
        self.depth = 0
        self.cost = 0
        self.evalfunc = 0
        self.children = []


class MyTree(SearchTree):

    def __init__(self, problem, strategy='breadth', max_nodes=None):
        super().__init__(problem, strategy)
        self.root = MyNode(problem.initial, None)
        self.open_nodes = [self.root]
        self.solution_cost = 0
        self.solution_length = 0
        self.total_nodes = 1
        self.max_nodes = max_nodes
        self.terminal_nodes = 0
        self.non_terminal_nodes = 0

    def astar_add_to_open(self, lnewnodes):
        self.open_nodes = sorted(self.open_nodes + lnewnodes, key=lambda no: no.evalfunc)

    def effective_branching_factor(self):
        estimativa = self.total_nodes ** (1 / self.solution_length)
        n = (estimativa ** (self.solution_length + 1) - 1) / (estimativa - 1)
        erro = self.total_nodes - n
        while abs(erro) > 0.001:
            if erro > 0:
                estimativa += 0.000001
            else:
                estimativa -= 0.000001
            n = (estimativa ** (self.solution_length + 1) - 1) / (estimativa - 1)
            erro = self.total_nodes - n
        return estimativa

    def update_ancestors(self, node):
        node.evalfunc = min([x.evalfunc for x in node.children])
        if node.parent is not None:
            self.update_ancestors(node.parent)

    def discard_worse(self):
        m = max([x.parent for x in self.open_nodes], key=lambda no: no.evalfunc)
        for child in m.children:
            if child in self.open_nodes:
                self.open_nodes.remove(child)
        self.open_nodes.append(m)

    def search2(self):
        while self.open_nodes:
            # if self.max_nodes is not None:
            #     while self.total_nodes > self.max_nodes:
            #         self.discard_worse()

            node = self.open_nodes.pop(0)
            if self.problem.goal_test(node.state):
                self.get_terminal(self.root)
                self.solution_cost = self.get_total_cost(node)
                self.solution_length = self.get_solution_length(node)
                return str(self.get_path(node))

            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state, a)
                if newstate not in self.get_path(node):
                    newnode = MyNode(newstate, node)
                    newnode.depth = node.depth + 1
                    newnode.cost = self.problem.domain.cost(node.state, a)
                    heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                    newnode.evalfunc = self.get_total_cost(newnode) + heuristic
                    node.children.append(newnode)
                    lnewnodes += [newnode]
            self.total_nodes += len(lnewnodes)
            if node.children:
                self.update_ancestors(node)
            self.add_to_open(lnewnodes)
        return None

    # shows the search tree in the form of a listing
    def show(self, heuristic=False, node=None, indent=''):
        if node is None:
            self.show(heuristic, self.root)
            print('\n')
        else:
            line = indent + node.state
            if heuristic:
                line += (' [' + str(node.evalfunc) + ']')
            print(line)
            if node.children is None:
                return
            for n in node.children:
                self.show(heuristic, n, indent + '  ')

    def get_total_cost(self, node):
        if not node:
            return 0
        return node.cost + self.get_total_cost(node.parent)

    def get_solution_length(self, node):
        if not node:  # quando ja nao tem mais pais
            return -1  # -1 porque o no inicial e 0
        return 1 + self.get_solution_length(node.parent)

    def get_terminal(self, node):
        if not node.children:  # se nao tiver filhos entao e um node terminal
            self.terminal_nodes += 1
        else:
            self.non_terminal_nodes += 1
            for i in node.children:
                self.get_terminal(i)  # verifica se os filhos sao terminais ou nao
