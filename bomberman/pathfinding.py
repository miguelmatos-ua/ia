# Daniel Coelho de Oliveira - 96800
# Pedro Candoso - 86140
# Miguel Matos - 89124

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
		return state==self.goal

# Nos de uma arvore de pesquisa
class SearchNode:
	def __init__(self,state,parent=None, depth=0,cost=0,heuristic=0): 
		self.state = state
		self.parent = parent
		self.depth = depth
		self.cost= cost
		self.heuristic=heuristic

	def in_parent(self, state):
		if self.parent == None:
			return False
		return self.parent.state == state or self.parent.in_parent(state)

	def __str__(self):
		return f"no({self.state}, {self.parent}, {self.depth})"
	def __repr__(self):
		return str(self)

# Arvores de pesquisa
class SearchTree:

	# construtor
	def __init__(self,problem, strategy='breadth'): 
		self.problem = problem
		root = SearchNode(problem.initial,None,0,0,self.problem.domain.heuristic(problem.initial, self.problem.goal))
		self.open_nodes = [root]
		self.strategy = strategy
		self.length = 0

	# obter o caminho (sequencia de estados) da raiz ate um no
	def get_path(self,node):
		if node.parent == None:
			return [node.state]
		path = self.get_path(node.parent)
		path += [node.state]
		return path

	def get_path2(self,node):
		if node.parent == None:
			return [(node.state,node.action)]
		path = self.get_path(node.parent)
		path += [(node.state,node.action)]
		return path

	# procurar a solucao
	def search(self):
		while self.open_nodes != []:
			node = self.open_nodes.pop(0)
			self.length+=1
			# Check if we reached our goal
			if self.problem.goal_test(node.state) or self.length > 200:
				path = self.get_path(node)
				return path
			lnewnodes = []
			# If we haven't reached our goal we will look at our possible actions
			for a in self.problem.domain.actions(node.state):
				newstate = self.problem.domain.result(node.state,a)
				if (not node.in_parent(newstate)):
					newdepth=node.depth+1
					newcost=node.cost+self.problem.domain.cost(newstate,a)
					newheuristic=self.problem.domain.heuristic(newstate, self.problem.goal)
					lnewnodes += [SearchNode(newstate,node,newdepth,newcost,newheuristic)]
			self.add_to_open(lnewnodes)
		return None

	# juntar novos nos a lista de nos abertos de acordo com a estrategia
	def add_to_open(self,lnewnodes):
		if self.strategy == 'breadth':
			self.open_nodes.extend(lnewnodes)
		elif self.strategy == 'depth':
			self.open_nodes[:0] = lnewnodes
		elif self.strategy == 'uniform':
			self.open_nodes = sorted(self.open_nodes + lnewnodes,key=lambda no: no.cost)
		elif self.strategy == 'greedy':
			self.open_nodes= sorted(self.open_nodes + lnewnodes,key=lambda no: no.heuristic)
		elif self.strategy == 'astar':
			self.open_nodes = sorted(self.open_nodes + lnewnodes,key=lambda no: no.cost+no.heuristic)