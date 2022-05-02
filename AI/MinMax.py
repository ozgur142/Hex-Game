from AI import *

#backtrack taille devrait etre plus petit ou égale à 5

#complexité: O(n^profondeur)
class MinMax(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur
		self.name = "MinMax"
		self.PROFONDEUR = float('inf')


	def minmax(self, graph, depth, isMaximizing):
		#controler les condition gagnants
		rcolor = None
		if self.color == ROUGE:
			rcolor = BLUE
		else:
			rcolor = ROUGE
			
		if graph.gagnant(self.color):
			return 1
		if graph.gagnant(rcolor):
			return -1

		if depth == self.PROFONDEUR: # s'il n'y pas de gagnant et on arrive à la limite de profondeur
			return 0

		

		if isMaximizing:
			bestScore = float('-inf')
			for i in range(self.size*self.size):
				if i not in graph.getGraphComplet():
					graph.ajoutSommet(self.color, i)
					score = self.minmax(graph, depth+1, False)
					graph.supprimeSommet(self.color, i)
					bestScore = max(score, bestScore)
			return bestScore

		else:
			bestScore = float('inf')
			for i in range(self.size*self.size):
				if i not in graph.getGraphComplet():
					graph.ajoutSommet(rcolor, i)
					score = self.minmax(graph, depth+1, True)
					graph.supprimeSommet(rcolor, i)
					bestScore = min(score, bestScore)
			return bestScore

	def algo(self, GameGraph):
		

		bestScore = float('-inf')
		move = None


		for i in range(self.size*self.size):
			if i not in GameGraph.getGraphComplet().keys():
				GameGraph.ajoutSommet(self.color, i)
				score = self.minmax(GameGraph, 0, False)
				GameGraph.supprimeSommet(self.color, i)
				if score > bestScore:
					bestScore = score
					move = i

		return move

	





