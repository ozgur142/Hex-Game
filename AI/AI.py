import random

import sys
sys.path.append('../')

from Graph import *

class AI:

	def __init__(self, size, color): # color pour voir 
		self.name = None
		self.color = color
		self.size = size
		self.center = int(self.size / 2) * self.size + int(self.size / 2)

	def algo(self, GameGraph):
		raise NotImplementedError("""Cette fonction serre à rien car c'est la classe abstract
				  si vous voulez implementer votre propre AI créez une nouvelle fichier dans le dossier AI 
				  cette AI devrait être herité de class AI avec une method 'algo' qui renvoit la valeur
				  de case choisi puis vous pouvez selectioner votre algo par le menu de configuraation. """)
		
	
	def connextionFort(self): #controle s'il y a une connextion fort .:.
		rcolor = None
		if self.color == ROUGE:
			rcolor = BLUE
		else:
			rcolor = ROUGE

		for i in range(self.size):
			for j in range(self.size):
				pass