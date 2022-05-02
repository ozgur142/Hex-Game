from asyncio import tasks
from time import sleep
from Grille import *
from tkinter import *
from Graph import *
from tkinter import messagebox
from os import listdir, mkdir
from os.path import isfile, join
from functools import partial
from Variables import *
import threading
import sys
sys.path.append('AI')
from RandomAI import *
from MinMax import *
from AlphaBeta import *
from RandomAlphaBeta import *
from OptiAlphaBeta import *
from AlphaHex import *


class Jeu:
    
    def __init__(self):
        self.size = None
        self.__turnCount = 0
        self.__saveName = ""
        
        self.__saves = []
        
        self.menu()
        
        
        self.Window = Tk()
        self.Window.title("Hex Game")
        self.Window.geometry("1400x1400")
        self.Window.config(background='#FFFFFF')

        self.myCanvas = Canvas(self.Window, width=1800, height=1800, bg="#FFFFFF")
        self.myCanvas.pack(pady = 10)
        
        self.Window.withdraw()
        self.Window.mainloop()   

          
    def commencer(self):        
        self.Window.config(cursor="dot red")
        
        self.Window.after(1000,self.nextTurnAi())
        
        self.myCanvas.bind("<Button-1>", self.nextTurnHuman)
    
            
        
    
    def nextTurnAi(self):#buna type Ai eklenicek
        if self.joueurs[(self.getTurnCount()%2)] == str(1):
            if self.getTurnCount() % 2 == 0:
                color = ROUGE
                self.Window.config(cursor="dot blue")
                moveAi = self.jouer1.algo(self.notreGraph)
            else:
                color = BLUE
                self.Window.config(cursor="dot red")
                moveAi = self.jouer2.algo(self.notreGraph)
            self.incTurnCount()
            self.notreGraph.ajoutSommet(color,moveAi)
            j = int(moveAi / self.size)
            i = moveAi % self.size
            self.FirstGrille.getMatrice()[i][j].changeColor(self.myCanvas,color)
            self.writeToSave(moveAi)
            if self.notreGraph.gagnant(ROUGE):
                try:
                    messagebox.showinfo("Victoire","Le Ai rouge a gagné.")
                    self.Window.destroy()
                except:
                    print("fin du jeu")
            elif self.notreGraph.gagnant(BLUE):
                try:
                    messagebox.showinfo("Victoire","Le Ai bleu a gagné.")
                    self.Window.destroy()
                except:
                    print("fin du jeu")
            elif self.joueurs[(self.getTurnCount()%2)] == str(1):
                self.Window.after(1000,self.nextTurnAi)
        
        

    def nextTurnHuman(self,event):
        color = ""
        if self.joueurs[(self.getTurnCount()%2)] == str(0):
            if self.getTurnCount() % 2 == 0:
                color = ROUGE
                self.Window.config(cursor="dot blue")
            else:
                color = BLUE
                self.Window.config(cursor="dot red")
            #Récuperation des points cliqée
            pointCliquee = event.x, event.y
            #trouver la hexagone associée aux points
            hexagonCliquee = self.trouverHexagonCliqueHuman(pointCliquee)
            if hexagonCliquee[0]:
                hexCliquee = hexagonCliquee[1]
                pointIetJ = hexagonCliquee[2]
                if hexCliquee.estLibre():
                    hexCliquee.changeColor(self.myCanvas, color)
                    self.writeToSave(pointIetJ)
                    self.incTurnCount()
                    self.notreGraph.ajoutSommet(color, pointIetJ)
                    #print(self.notreGraph.getGraphB())
                    #print(self.notreGraph.getGraphR())
            if self.notreGraph.gagnant(ROUGE):
                messagebox.showinfo("Victoire","Le joueur rouge a gagné.")
                self.Window.destroy()
            elif self.notreGraph.gagnant(BLUE):
                messagebox.showinfo("Victoire","Le joueur bleu a gagné.")
                self.Window.destroy()
            elif self.joueurs[(self.getTurnCount()%2)] == str(1):
                self.Window.after(1000,self.nextTurnAi)
            
                
        
    #trouver la hexagone associée aux points cliquées
    def trouverHexagonCliqueHuman(self, p):
        for i in range(self.FirstGrille.getSize()):
            for j in range(self.FirstGrille.getSize()):
                if self.FirstGrille.getMatrice()[i][j].distance(p) <= hexL:
                    x = j * self.FirstGrille.getSize() + i
                    return True, self.FirstGrille.getMatrice()[i][j], x
        return False, None, (-1, -1)
    
    def menu(self):
        self.__saves = self.getSaves()
        fenetreMenu = Tk(className='configuration')
        fenetreMenu.resizable(width=False, height=False)
        fenetreMenu.geometry('520x500+700+300')
        
        FrameNomFichier = Frame(fenetreMenu,pady=10,padx=10)
        texteNomFichier = Label(FrameNomFichier, text="Nom d'Enregistrement : ", font="Arial 15")
        texteNomFichier.pack(side='left')
        fichier = Text(FrameNomFichier,font="Arial 15",width=15,height=1)
        fichier.pack(side='right')
        FrameNomFichier.pack()

        FrameTaille = Frame(fenetreMenu,pady=10,padx=10)
        texteTaille = Label(FrameTaille, text="Taille : ", font="Arial 15")
        texteTaille.pack(side='left')
        taille = Spinbox(FrameTaille,from_=2, to=11,font="Arial 15",width=15)
        taille.pack(side='right')
        FrameTaille.pack()
        

        FrameJoueur = Frame(fenetreMenu,pady=10)
        Frame1 = Frame(FrameJoueur)
        choix1 = [("Joueur","Joueur"),("IA","IA")]

        texteJoueur1 = Label(Frame1,text="Joueur 1 : ",fg='#FF0000', font="Arial 15")
        texteJoueur1.pack(side='left')

        choix1 = [("Joueur",0),("IA",1)]
        var1 = StringVar()
        for text, val in choix1 :
            rb = Radiobutton(Frame1, text=text, variable=var1, value=val, font="Arial 15")
            # valeur par defaut : joueur 1 IA
            if (val == 1):
                rb.select()
            rb.pack(side='right')
        
        Frame1.pack()
        Frame2 = Frame(FrameJoueur, pady=10)
        texteJoueur2 = Label(Frame2,text="Joueur 2 : ", fg='#0000FF',font="Arial 15")
        texteJoueur2.pack(side='left')
            

        choix2 = [("Joueur",0),("IA",1)]
        var2 = StringVar()
        for text, val in choix2:
            rb2 = Radiobutton(Frame2, text=text, variable=var2, value=val, font="Arial 15")
            # valeur par defaut : joueur 2 Joueur
            if (val == 0):
                rb2.select()
            rb2.pack(side='right')
        Frame2.pack()
        FrameJoueur.pack()
        
        FrameSaves = Frame(FrameJoueur, pady=10)
        FrameSaves.pack(side = 'top')
        
        Frame3 = Frame(FrameSaves, pady=10)
        savesLabel = Label(FrameSaves,text= "Saves:",fg='#FF0000', font="Arial 15")
        savesLabel.pack(side='top')
        
        for i in self.__saves:
            buttonSave = Button(Frame3,text= i[2:],command=lambda i = i: self.ouvrirSave(i))
            buttonSave.pack(side='top')
            #fenetreMenu.update()
        Frame3.pack()
        FrameSaves.pack()
            
        
        

        b = Button(fenetreMenu,text="Jouer",command=lambda : self.playGame(fenetreMenu,fichier.get(1.0, "end-1c"),taille.get(),var1.get(),var2.get())) 
        b.pack()
        

        

    def playGame(self, menu, nomFichier, taille, player1, player2): # mettre en place les configurations
        print(player1)
        print(player2)
        #print(taille)
        if(nomFichier ==""):
            messagebox.showinfo("ERROR", "Vous devez chosir un valid nom d'enregistrement")
        elif int(taille) > 11 or int(taille) < 2 or taille == None:
            messagebox.showinfo("ERROR", "Vous devez chosir une taille entre 2 et 11")
        else:
            self.size = int(taille)
            self.joueurs = [player1,player2]
            
            if player1 == str(1):
                """
                POUR CHANGER LES AI 1
                """
                self.jouer1 = AlphaHex(self.size, ROUGE)
                #self.jouer1 = AlphaBeta(self.size, ROUGE)
                #self.jouer1 = OptiAlphaBeta(self.size, ROUGE)
                #self.jouer1 = RandomAlphaBeta(self.size, ROUGE)
                #self.jouer1 = AlgoRandom(self.size, ROUGE)
                #self.jouer1 = MinMax(self.size, ROUGE)
                
            else:
                self.jouer1 = "Player"
            
            if player2 == str(1):
                """
                POUR CHANGER LES AI 2
                """
                self.jouer2 = AlphaHex(self.size, BLUE)
                #self.jouer2 = AlphaBeta(self.size, BLUE)
                #self.jouer2 = OptiAlphaBeta(self.size, BLUE)
                #self.jouer2 = RandomAlphaBeta(self.size, BLUE)
                #self.jouer2 = AlgoRandom(self.size, BLUE)
                #self.jouer2 = MinMax(self.size, BLUE)
                
            else:
                self.jouer2 = "Player"
                
            dirPath = "saves/" + str(taille)
            try:
                mkdir(dirPath)
            except:
                print("file already exists")
            nom_save = dirPath + "/" + nomFichier + ".txt"
            print(nom_save)
            f = open(nom_save, "a")
            self.__saveName = nom_save
            
            self.notreGraph = Graph(self.size) # initialize de graphe
            self.FirstGrille = Grille(self.size, self.myCanvas)
            self.FirstGrille.traceGrille(self.myCanvas)
            
            self.Window.update()
            self.Window.deiconify()
            
            menu.destroy()
            self.commencer()

            
            
    def writeToSave(self,x):
        if self.__saveName =="":
            messagebox.showinfo("ERROR", "Vous devez chosir les parametres de la menu premierement, fermez et relancer le jeu!")
        else:
            f = open(self.__saveName, "a")
            if self.__turnCount%2==0:
                f.write(str(x)+":")
            else: 
                f.write(str(x)+"\n")
        f.close()
                     
    def ouvrirSave(self,fileName):
        sizeFile = fileName.split("/")[0] 
        self.size = int(sizeFile)
        WindowSave = Tk()
        WindowSave.title("Saved Game")
        WindowSave.geometry("1000x1000")
        WindowSave.config(background='#FFFFFF')

        CanvasSave = Canvas(WindowSave, width=1100, height=1100, bg="#FFFFFF")
        CanvasSave.pack(pady = 100)
        listI_J = []
        with open("saves/"+fileName,'r') as f:
            line = f.readlines()
            for l in line:
                updatedL = l.rstrip(l[-1]).split(':')
                #print(updatedL)
                ix = int(int(updatedL[0]) / self.size)
                jx = int(updatedL[0]) % self.size
                
                #print("ix : " + str(ix) + " jx : " + str(jx))
                listI_J.append((ix,jx))
                try:
                    iy = int(int(updatedL[1]) / self.size)
                    jy = int(updatedL[1]) % self.size
                    #print("iy : " ,iy , " jy : " , jy)
                    listI_J.append((iy,jy))
                except:
                    print("no second move")
        #print(sizeFile)    
        GrilleSave = Grille(int(sizeFile), CanvasSave)
        GrilleSave.traceGrille(CanvasSave)
        cpt = 0
        while cpt < len(listI_J):
            if(cpt%2 != 0):
                color = "#0000FF"
                p = listI_J[cpt][0]
                k = listI_J[cpt][1]
                GrilleSave.getMatrice()[k][p].changeColor(CanvasSave,color)
                #print("if: ",k,p)
                sleep(0.5)
            else:
                try:
                    color = "#FF0000"
                    p = listI_J[cpt][0]
                    k = listI_J[cpt][1]
                    #print("else: ",k,p)
                    GrilleSave.getMatrice()[k][p].changeColor(CanvasSave,color) 
                    sleep(0.5) 
                except:
                    print("no second move")
            WindowSave.update()
            cpt += 1
            
    def incTurnCount(self):
        self.__turnCount += 1
        
    def getSaves(self):
        saveFiles = []
        savesDir = "saves/"
        for i in listdir(savesDir):
            directorySearch = "saves/" + str(i) + "/"
            #print(directorySearch)
            for f in listdir(directorySearch):
                if isfile(join(directorySearch, f)):
                    #print(f)
                    saveFiles.append(str(i) + "/" + f)
                    #print(saveFiles)
        #print(saveFiles)
        return saveFiles
    
    def getTurnCount(self):
        return self.__turnCount
    




Jeu()

