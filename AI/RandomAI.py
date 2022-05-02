from AI import *

class AlgoRandom(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur

		self.name = "RandomAI"

	def algo(self, GameGraph):

		move = None

		for i in range(self.size * self.size):
			if i not in GameGraph.getGraphComplet():
				GameGraph.ajoutSommet(self.color, i)
				if GameGraph.gagnant(self.color):
					move = i
					GameGraph.supprimeSommet(self.color, i)
					return move
				GameGraph.supprimeSommet(self.color, i)


		x = random.randint(0, self.size*self.size-1)
		while x in GameGraph.getGraphComplet().keys():
			x = random.randint(0, self.size*self.size-1)

		return x
