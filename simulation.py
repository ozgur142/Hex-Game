# simulation des algorithmes
from Variables import *

import matplotlib.pyplot as plt
import sys
sys.path.append('AI')
from RandomAI import *
from AlphaBeta import *
from MinMax import *
from RandomAlphaBeta import *
from OptiAlphaBeta import *
from AlphaHex import *

def ploting(AI1, AI2, statistic):
	plt.figure("jeu en temps", figsize=(12,6))

	numeroJeu = [i for i in range(1, len(statistic)+1)]

	plt.plot(numeroJeu, statistic) 

	plt.title(AI1.name + " vs " + AI2.name)

	plt.xlabel("Numéro de Jeu")

	plt.ylabel(" gagnant 0 si " + AI1.name + " 1 si " + AI2.name)


	# 2ème plot
	plt.figure("proportion de condition gagner")

	nbrGagneAI1 = statistic.count(0)
	nbrGagneAI2 = statistic.count(1)
	y = [nbrGagneAI1, nbrGagneAI2]
	names = [AI1.name, AI2.name]

	plt.pie(y, labels = names, autopct='%1.2f%%')


	plt.show()

def simulation(AI1, AI2, nombreJeu, size):

	# 0 si AI1 gagne
	# 1 si AI2 gagne

	statistic = [-1 for i in range(int(nombreJeu/2)*2)]

	for i in range(0, int(nombreJeu/2)*2, 2):
		GameGraph = Graph(size)

		while True:
			a = AI1.algo(GameGraph)
			GameGraph.ajoutSommet(AI1.color, a)
			if GameGraph.gagnant(AI1.color):
				statistic[i] = 0
				print(AI1.name + " a gagné")
				break

			a = AI2.algo(GameGraph)
			GameGraph.ajoutSommet(AI2.color, a)
			if GameGraph.gagnant(AI2.color):
				statistic[i] = 1
				print(AI2.name + " a gagné")
				break

		# ici on change l'AI qui commence en premier 
		# donc pas d'avantage pour le AI qui commence en premier

		GameGraph = Graph(size)

		while True:
			a = AI2.algo(GameGraph)
			GameGraph.ajoutSommet(AI2.color, a)
			if GameGraph.gagnant(AI2.color):
				statistic[i+1] = 1
				print(AI2.name + " a gagné")
				break

			a = AI1.algo(GameGraph)
			GameGraph.ajoutSommet(AI1.color, a)
			if GameGraph.gagnant(AI1.color):
				statistic[i+1] = 0
				print(AI1.name + " a gagné")
				break

	ploting(AI1, AI2, statistic)



c1 = ROUGE
c2 = BLUE

AI1 = None
AI2 = None



nombreJeu = int(input("Entrez le nombre de jeu à realiser: "))
size = int(input("Entrez le taille de la grille de jeu: "))
choix1 = int(input("""Choisez le premier AI :
		1- AlgoRandom
		2- MinMax
		3- AlphaBeta
		4- RandomAlphaBeta
		5- OptiAlphaBeta
		6- AlphaHex
->"""))
if choix1 == 1:
	AI1 = AlgoRandom(size, c1)
elif choix1 == 2:
	AI1 = MinMax(size, c1)
elif choix1 == 3:
	AI1 = AlphaBeta(size, c1)
elif choix1 == 4:
	AI1 = RandomAlphaBeta(size, c1)
elif choix1 == 5:
	AI1 = OptiAlphaBeta(size, c1)
elif choix1 == 6:
	AI1 = AlphaHex(size, c1)
else:
	print("non definie")
	exit()

choix2 = int(input("""Choisez le deuxieme AI :
		1- AlgoRandom
		2- MinMax
		3- AlphaBeta
		4- RandomAlphaBeta
		5- OptiAlphaBeta
		6- AlphaHex
->"""))
if choix2 == 1:
	AI2 = AlgoRandom(size, c2)
elif choix2 == 2:
	AI2 = MinMax(size, c2)
elif choix2 == 3:
	AI2 = AlphaBeta(size, c2)
elif choix2 == 4:
	AI2 = RandomAlphaBeta(size, c2)
elif choix2 == 5:
	AI2 = OptiAlphaBeta(size, c2)
elif choix2 == 6:
	AI2 = AlphaHex(size, c2)
else:
	print("non definie")
	exit()

print(AI1.name, " VS ", AI2.name)
print("simulation commence... \n")
simulation(AI1, AI2, nombreJeu, size)

"""
nombreJeu = 100
size = 5

AI1 = AlgoRandom(size, ROUGE)
AI2 = MinMax(size, BLUE)
AI3 = AlphaBeta(size, ROUGE)
AI4 = RandomAlphaBeta(size, ROUGE)
AI5 = OptiAlphaBeta(size, BLUE)

simulation(AI4, AI5, nombreJeu, size)
"""
