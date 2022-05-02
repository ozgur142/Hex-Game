from AI import *


# minmax optimisé avec alpha beta

class AlphaBeta(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur
		self.name = "AlphaBeta"
		self.PROFONDEUR = 6


	def alphaBeta(self, graph, depth, isMaximizing, alpha, beta):
		#controler les condition gagnants
		rcolor = None
		if self.color == ROUGE:
			rcolor = BLUE
		else:
			rcolor = ROUGE

		if graph.gagnant(self.color):
			return 1 / depth
		if graph.gagnant(rcolor):
			return -1 / depth

		if self.PROFONDEUR == depth:
			return 0
		



		if isMaximizing:
			bestScore = float('-inf')
			for i in range(self.size*self.size):
				if i not in graph.getGraphComplet():
					graph.ajoutSommet(self.color, i)
					score = self.alphaBeta(graph, depth+1, False, alpha, beta)
					graph.supprimeSommet(self.color, i)
					bestScore = max(score, bestScore)
					alpha = max(alpha, bestScore)
					if alpha >= beta:
						break #on coup la branche beta 
			return bestScore

		else:
			bestScore = float('inf')
			for i in range(self.size*self.size):
				if i not in graph.getGraphComplet():
					graph.ajoutSommet(rcolor, i)
					score = self.alphaBeta(graph, depth+1, True, alpha, beta)
					graph.supprimeSommet(rcolor, i)
					bestScore = min(score, bestScore)
					beta = min(beta, bestScore)
					if beta <= alpha:
						break #on coup la branche alpha 
			return bestScore

	def algo(self, GameGraph):

		rcolor = None
		if self.color == ROUGE:
			rcolor = BLUE
		else:
			rcolor = ROUGE

		#si il y a une condition gagnant pour nous
		for i in range(self.size * self.size):
			if i not in GameGraph.getGraphComplet():
				GameGraph.ajoutSommet(self.color, i)
				if GameGraph.gagnant(self.color):
					GameGraph.supprimeSommet(self.color, i)
					return i
				GameGraph.supprimeSommet(self.color, i)

		#si il y a une condition gagnant pour adversaire on empeche
		for i in range(self.size * self.size):
			if i not in GameGraph.getGraphComplet():
				GameGraph.ajoutSommet(rcolor, i)
				if GameGraph.gagnant(rcolor):
					GameGraph.supprimeSommet(rcolor, i)
					return i
				GameGraph.supprimeSommet(rcolor, i)


		bestScore = float('-inf')
		move = None
		alpha = float('-inf')
		beta = float('inf')

		for i in range(self.size*self.size):
			if i not in GameGraph.getGraphComplet().keys():
				GameGraph.ajoutSommet(self.color, i)
				score = self.alphaBeta(GameGraph, 0, False, alpha, beta)
				GameGraph.supprimeSommet(self.color, i)
				if score > bestScore:
					bestScore = score
					move = i


		return move

	

