from tkinter import *
from Hexagon import *
from Variables import *
import math

class Grille:

    def __init__(self, size, canva):
        self.__size = size
        self.__matrice = self.__createMatrice(self.__size)
        self.GridCanvas = canva
    

    
    #tableau pour stocker les positions des centres des hexagones
    def __createMatrice(self, size): 
        self.__tourCount = 0
        x0 = 50
        y0 = 50
        M = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                M[i][j] = Hexagon(x0+i*hexL*math.sqrt(3)+j*(hexL/2)*math.sqrt(3) ,y0+j*(hexL*1.5),size)
        return M

    def traceGrille(self, canvasGrille):
        for i in range(self.getSize()):
            for j in range(self.getSize()):
                canvasGrille.create_polygon(self.getMatrice()[i][j].x[0],self.getMatrice()[i][j].y[0],self.getMatrice()[i][j].x[1],self.getMatrice()[i][j].y[1],
                                self.getMatrice()[i][j].x[2],self.getMatrice()[i][j].y[2],self.getMatrice()[i][j].x[3],self.getMatrice()[i][j].y[3],
                                self.getMatrice()[i][j].x[4],self.getMatrice()[i][j].y[4],self.getMatrice()[i][j].x[5],self.getMatrice()[i][j].y[5],
                                fill = self.getMatrice()[i][j].getColor(),
                                outline="#000000")
        #pour les bordures   
        n = self.getSize()                     
        for i in range(n):
            #bordures rouges haut
            canvasGrille.create_line(self.getMatrice()[i][0].x[4], self.getMatrice()[i][0].y[4], self.getMatrice()[i][0].x[3], self.getMatrice()[i][0].y[3],
                                    self.getMatrice()[i][0].x[2], self.getMatrice()[i][0].y[2], width=6, fill=ROUGE)
            #bordures bleus gauche
            canvasGrille.create_line(self.getMatrice()[0][i].x[4], self.getMatrice()[0][i].y[4], self.getMatrice()[0][i].x[5], self.getMatrice()[0][i].y[5],
                                    self.getMatrice()[0][i].x[0], self.getMatrice()[0][i].y[0], width=6, fill=BLUE)
            #bordures rouges bas
            canvasGrille.create_line(self.getMatrice()[i][n-1].x[5], self.getMatrice()[i][n-1].y[5], self.getMatrice()[i][n-1].x[0], self.getMatrice()[i][n-1].y[0],
                                    self.getMatrice()[i][n-1].x[1], self.getMatrice()[i][n-1].y[1], width=6, fill=ROUGE)
            #bordures bleus droit
            canvasGrille.create_line(self.getMatrice()[n-1][i].x[3], self.getMatrice()[n-1][i].y[3], self.getMatrice()[n-1][i].x[2], self.getMatrice()[n-1][i].y[2],
                                    self.getMatrice()[n-1][i].x[1], self.getMatrice()[n-1][i].y[1], width=6, fill=BLUE)

    # Getters and Setters

    def getMatrice(self):
        return self.__matrice

    def getSize(self):
        return self.__size


    




