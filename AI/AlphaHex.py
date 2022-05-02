from AI import *
from AlphaBeta import *


class AlphaHex(AI):

	def __init__(self,size, color):
		super().__init__(size, color) # appel de classe superieur
		self.name = "AlphaHex"



	# Function which finds all the paths
	# and stores it in paths array
	def find_paths(self, paths, path, parent, n, u):
		# Base Case
		if (u == -1):
			paths.append(path.copy())
			return None
 
    	# Loop for all the parents
    	# of the given vertex
		for par in parent[u]:
 
        	# Insert the current
        	# vertex in path
			path.append(u)
 
        	# Recursive call for its parent
			self.find_paths(paths, path, parent, n, par)
 
        	# Remove the current vertex
			path.pop()


	# a modified version of BFS that stores predecessor
	# of each vertex in array p
	# and its distance from source in array d
	def bfs(self, adj, parent, n, start):
		# dist will contain shortest distance
    	# from start to every other vertex
		dist = [1000 for _ in range(n)]
		q = []
 
    	# Insert source vertex in queue and make
    	# its parent -1 and distance 0
		q.append(start)
		parent[start] = [-1]
		dist[start] = 0
 
    # Until Queue is empty
		while q:
			u = q.pop(0)
			if u in adj.keys():
				for v in adj[u]:
					if (dist[v] > dist[u] + 1):
		 
		                # A shorter distance is found
		                # So erase all the previous parents
		                # and insert new parent u in parent[v]
						dist[v] = dist[u] + 1
						q.append(v)
						parent[v].clear()
						parent[v].append(u)

					elif (dist[v] == dist[u] + 1):
		                # Another candidate parent for
		                # shortes path found
						parent[v].append(u)
	                
		     
	    
	         

	# O(V + E)
	def shortestPaths(self, adj, start, end):
		n = self.size * self.size +2
		paths = []
		path = []
		parent = [[] for _ in range(n)]
 
    	# Function call to bfs
		self.bfs(adj, parent, n, start)

    	# Function call to find_paths
		self.find_paths(paths, path, parent, n, end)

		#elmine les sommets invisibles
		for p in paths: 
			p.pop(0)
			p.pop(len(p)-1)

		return paths

	# O((N + M) * T),    T = taille de graphe 
	def extrairChemins(self, GameGraph, cheminCourts1, cheminCourts2, chemins1, chemins2):
		for p in cheminCourts1:
			if self.color == ROUGE:
				for e in GameGraph.getGraphR().keys():
					if e in p:
						chemins1.append(p)
						break
			if self.color == BLUE:
				for e in GameGraph.getGraphB().keys():
					if e in p:
						chemins1.append(p)
						break
		for p in cheminCourts2:
			if self.color == ROUGE:
				for e in GameGraph.getGraphB().keys():
					if e in p:
						chemins2.append(p)
						break
			if self.color == BLUE:
				for e in GameGraph.getGraphR().keys():
					if e in p:
						chemins2.append(p)
						break


	# O((N + M) * T),    T = taille de graphe 
	def extrairCheminsPlusCommuns(self, GameGraph, cheminCourts1, cheminCourts2, chemins1, chemins2):
		maxi = 0
		R = set(GameGraph.getGraphR().keys())
		G = set(GameGraph.getGraphB().keys())
		for p in cheminCourts1:
			if self.color == ROUGE:
				communTaille = len(R & set(p))
				if communTaille > maxi:
					chemins1.clear()
					chemins1.append(p)
					maxi = communTaille
				if communTaille == maxi:
					chemins1.append(p)

			if self.color == BLUE:
				communTaille = len(G & set(p))
				if communTaille > maxi:
					chemins1.clear()
					chemins1.append(p)
					maxi = communTaille
				if communTaille == maxi:
					chemins1.append(p)


		maxi = 0
		for p in cheminCourts2:
			if self.color == ROUGE:
				communTaille = len(G & set(p))
				if communTaille > maxi:
					chemins2.clear()
					chemins2.append(p)
					maxi = communTaille
				if communTaille == maxi:
					chemins2.append(p)

			if self.color == BLUE:
				communTaille = len(R & set(p))
				if communTaille > maxi:
					chemins2.clear()
					chemins2.append(p)
					maxi = communTaille
				if communTaille == maxi:
					chemins2.append(p)


	# O(N + M) 
	def intersection(self, chemins1, chemins2):
		c1 = set()
		c2 = set()
		for t1 in chemins1:
			for e in t1:
				c1.add(e)
		for t2 in chemins2:
			for e in t2:
				c2.add(e)

		intersection = list(c1 & c2)
		return intersection




	def algo(self, GameGraph):

		rcolor = None
		if self.color == ROUGE:
			rcolor = BLUE
		else:
			rcolor = ROUGE


		if self.center not in GameGraph.getGraphComplet():
			return self.center

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

		# on appelle Alpha Beta AI pour qu'il nous aide
		tour = len(GameGraph.getGraphComplet().keys()) -2
		if self.size*self.size - tour < 20:
			AB = AlphaBeta(self.size, self.color)
			return AB.algo(GameGraph)

		# copie de graph de jeu
		GraphCopy1 = Graph(self.size)
		GraphCopy1.setGraphR(GameGraph.getGraphR())
		GraphCopy1.setGraphB(GameGraph.getGraphB())

		GraphCopy2 = Graph(self.size)
		GraphCopy2.setGraphR(GameGraph.getGraphR())
		GraphCopy2.setGraphB(GameGraph.getGraphB())


		# on remplit la graphe avec la couleur de IA et l'autre avec couleur d'adversaire
		for i in range(self.size * self.size):
			if i not in GraphCopy1.getGraphComplet():
				GraphCopy1.ajoutSommet(self.color, i)
			if i not in GraphCopy2.getGraphComplet():
				GraphCopy2.ajoutSommet(rcolor, i)

		# sommets invisibles
		Sa = self.size*self.size 
		Sb = self.size*self.size +1 
		cheminCourts1 = None
		cheminCourts2 = None

		if self.color == ROUGE:
			cheminCourts1 = self.shortestPaths(GraphCopy1.getGraphR(), Sa, Sb)
			cheminCourts2 = self.shortestPaths(GraphCopy2.getGraphB(), Sa, Sb)
		if self.color == BLUE:
			cheminCourts1 = self.shortestPaths(GraphCopy1.getGraphB(), Sa, Sb)
			cheminCourts2 = self.shortestPaths(GraphCopy2.getGraphR(), Sa, Sb)

		# etape 2: entre les chemins on exraire les chemins qui contients deja ces sommets dans le graph
		chemins1 = []
		chemins2 = []
		self.extrairChemins(GameGraph, cheminCourts1, cheminCourts2, chemins1, chemins2)
		
		# etape 3: on extraire les chemin qui contient la même coup pour 2 jouers
		# intersection des coups qui ne sont pas joué
		intersection = self.intersection(chemins1, chemins2)

		# etape 4: on extraire aussi les chemins qui contiennent plus de coup
		# deja joué puis on prends leur intersection des coups qui ne sont pas joué
		chemins1P = []
		chemins2P = []
		self.extrairCheminsPlusCommuns(GameGraph, chemins1, chemins2, chemins1P, chemins2P)
		intersectionP = self.intersection(chemins1P, chemins2P)

		#etape 5: 
		if intersectionP:
			x = random.randint(0, len(intersectionP)-1)
			return intersectionP[x]
		if intersection:
			x = random.randint(0, len(intersection)-1)
			return intersection[x]
		elif chemins2P:
			x = random.randint(0, len(chemins2P)-1)
			y = random.randint(0, len(chemins2P[x])-1)
			while chemins2P[x][y] in GameGraph.getGraphComplet().keys():
				x = random.randint(0, len(chemins2P)-1)
				y = random.randint(0, len(chemins2P[x])-1)
			return chemins2P[x][y]			
	
		elif chemins1P:
			x = random.randint(0, len(chemins1P)-1)
			y = random.randint(0, len(chemins1P[x])-1)
			while chemins1P[x][y] in GameGraph.getGraphComplet().keys():
				x = random.randint(0, len(chemins1P)-1)
				y = random.randint(0, len(chemins1P[x])-1)
			return chemins1P[x][y]

		#on joue random
		else:
			x = random.randint(0, self.size*self.size-1)
			while x in GameGraph.getGraphComplet().keys():
				x = random.randint(0, self.size*self.size-1)
		
			return x