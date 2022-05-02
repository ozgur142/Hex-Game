from Variables import *

class Graph:
    
    def __init__(self,size):
        self.__size = size
        
        self.__Ra = self.__size*self.__size #Indice invisible haut de graphe rouge 
        self.__Rb = self.__size*self.__size+1 #Indice invisible bas de graphe rouge 

        self.__Ba = self.__size*self.__size #Indice invisible droite de graphe bleu
        self.__Bb = self.__size*self.__size+1 #Indice invisible gauche de graphe bleu
        
        self.__graphR = self.initGraphR() #LA GRAPHE DE CONNEXTION ROUGE
        self.__graphB = self.initGraphB()
   


    
    #getters 
    def getSize(self):
        return self.__size

    def getGraphR(self):
        return self.__graphR

    def getGraphB(self):
        return self.__graphB

    def setGraphR(self, GR):
        self.__graphR = GR.copy()

    def setGraphB(self, GB):
        self.__graphB = GB.copy()

    def getGraphComplet(self):   # combine 2 graphe dans une seule graphe
        return {**self.getGraphR(), **self.getGraphB()}
 
    def initGraphR(self):
        graph = {}
        graph[self.__Ra] = [i for i in range(self.__size) ]#indices de la premiere rangée
        graph[self.__Rb] = [self.__size * (self.getSize() - 1) + i  for i in range(self.getSize()) ]#indices de la dernier rangée
        return graph

    def initGraphB(self):
        graph = {}
        graph[self.__Ba] = [i * self.getSize() for i in range(self.getSize()) ]
        graph[self.__Bb] = [(self.getSize() - 1) + i * self.getSize() for i in range(self.getSize()) ]
        return graph
        

    
    
    def ajoutSommet(self, couleur, x): # couleur Bleu ou Rouge 

        if x in self.getGraphComplet():
            raise ValueError(x, " est déjà dans le graphe")

        if (couleur == ROUGE): #rouge
            self.__graphR[x] = []
        
            #converir l'indice k en deux coordonnes (x,y), pour verifier les depassements
            i = int(x / self.__size)
            j = x % self.__size


            #pour chaque voisin possible, on verifie le depassment, si c'est bon on cherche s'il appartient a liste des keys de grapheB / grapheR

            if x in self.__graphR[self.__Ra]:
                self.__graphR[x].append(self.__Ra)

            if x in self.__graphR[self.__Rb]:
                self.__graphR[x].append(self.__Rb)


            v = (i-1)*self.__size+j  #reconvertir en indice unidimensionnel
    
            if i-1 >= 0 and v in self.__graphR.keys():#ajouter les voisins dans les deux sens
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i+1)*self.__size+j

            if i+1 < self.__size and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = i*self.__size+j-1

            if j-1 >= 0 and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = i*self.__size+j+1

            if j+1 < self.__size and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i-1)*self.__size+j+1

            if j+1 < self.__size and i-1 >= 0 and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)

            v = (i+1)*self.__size+j-1

            if i+1 < self.__size and j-1 >= 0 and v in self.__graphR.keys():
                self.__graphR[x].append(v)
                self.__graphR[v].append(x)




        elif(couleur == BLUE): #bleu
            self.__graphB[x] = []

            if x in self.__graphB[self.__Ba]:
                self.__graphB[x].append(self.__Ba)

            if x in self.__graphB[self.__Bb]:
                self.__graphB[x].append(self.__Bb)
        

            i = int(x / self.__size)
            j = x % self.__size

            v = (i-1)*self.__size+j

            if i-1 >= 0 and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i+1)*self.__size+j

            if i+1 < self.__size and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = i*self.__size+j-1

            if j-1 >= 0 and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = i*self.__size+j+1

            if j+1 < self.__size and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i-1)*self.__size+j+1

            if j+1 < self.__size and i-1 >= 0 and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)

            v = (i+1)*self.__size+j-1

            if i+1 < self.__size and j-1 >= 0 and v in self.__graphB.keys():
                self.__graphB[x].append(v)
                self.__graphB[v].append(x)
        else:
            print("wrong usage of couleur: Blue or Rouge")



    def gagnant(self, color):
        # initialise tous les sommets comme non visité
        visited =[False]*(self.__size * self.__size + 2)

         # creation de notre file
        queue=[]

        # marquer le point de départ
        if color == BLUE:
            queue.append(self.__Ba)
            visited[self.__Ba] = True
        if color == ROUGE:
            queue.append(self.__Ra)
            visited[self.__Ra] = True

        while queue:
     
            #defiler
            n = queue.pop(0)

            if color == BLUE:
                # si sommet adjacence est le destination alors retourner True
                if n == self.__Bb:
                    return True
         
                #  Else, continue 
                for i in self.__graphB[n]:
                    if visited[i] == False and i in self.__graphB.keys():
                        queue.append(i)
                        visited[i] = True

            if color == ROUGE:
                # si sommet adjacence est le destination alors retourner True
                if n == self.__Rb:
                    return True
     
                #  Else, continue 
                for i in self.__graphR[n]:
                    if visited[i] == False and i in self.__graphR.keys():
                        queue.append(i)
                        visited[i] = True

        return False



    def supprimeSommet(self, couleur, x):
        if x not in self.getGraphComplet():
            raise ValueError(x, " n'est pas dans le graphe")

        if (couleur == ROUGE): #rouge
            for i in self.__graphR.keys():
                if i == self.__Ra or i == self.__Rb:
                    continue
                if x in self.__graphR[i]:
                    self.__graphR[i].remove(x)

            del self.__graphR[x]

        if (couleur == BLUE): 
            for i in self.__graphB.keys():
                if i == self.__Ba or i == self.__Bb:
                    continue
                if x in self.__graphB[i]:
                    self.__graphB[i].remove(x)

            del self.__graphB[x]



    

"""


        self.__moves = []
        self.__dernierJouerCouleur = None

            self.__moves.append(x)
            self.__dernierJouerCouleur = BLUE

    def reverse(self):
        if self.__moves == []:
            raise ValueError("pas de move precedent")

        x = self.__moves.pop()

        if self.__dernierJouerCouleur == ROUGE:
            for i in self.__graphR.keys():
                if i == self.__Ra or i == self.__Rb:
                    continue
                if x in self.__graphR[i]:
                    self.__graphR[i].remove(x)

            del self.__graphR[x]

        if self.__dernierJouerCouleur == BLUE:
            for i in self.__graphB.keys():
                if i == self.__Ba or i == self.__Bb:
                    continue
                if x in self.__graphB[i]:
                    self.__graphB[i].remove(x)

            del self.__graphB[x]

    """


