from tkinter import *
from Variables import *
import math

class Hexagon:

    def __init__(self, x0, y0,sizeCote):
        self.x = []
        self.y = []
        self.sizeCote = hexL
        # calculer les 6 sommetes d'une hexagione à partir de son centre
        for i in range(6) :
            angle = math.radians(i*360/6)
            self.x.append(int(x0+self.sizeCote*math.sin(angle)))
            self.y.append(int(y0+self.sizeCote*math.cos(angle)))

        self.__color = "#FFFFFF"
        self.__centre = x0, y0


    # Getters et Setters

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setValue(self, value):
        self.__value = value

    # Methodes Utils
    def estLibre(self):
        return self.getColor() == "#FFFFFF"

    #trouve la distance entre une point et sa centre
    def distance(self, p):
        return math.sqrt(pow((self.__centre[0] - p[0]),2) + pow((self.__centre[1] - p[1]),2))

    def changeColor(self, canvasHex, color):
        self.setColor(color)
        canvasHex.create_polygon(self.x[0],self.y[0], self.x[1],self.y[1],
                                self.x[2],self.y[2], self.x[3],self.y[3],
                                self.x[4],self.y[4], self.x[5],self.y[5],
                                fill = color,
                                outline="#000000")








