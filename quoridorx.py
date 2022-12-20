"""Module de la classe QuoridorX

Classes:
    * QuoridorX - Classe pour afficher graphiquement le jeu quoridor.
"""

"""Pour implanter le mode graphique, on vous demande de développer une classe graphique nommée QuoridorX 
qui hérite de votre classe Quoridor. Votre nouvelle classe doit permettre de faire tout ce que la classe 
de base peut faire, mais en ajoutant une méthode afficher pour afficher l'état actuel du damier dans une 
scêtre graphique. Définissez votre classe QuoridorX dans un module nommé quoridorx. 

Prenez garde de ne pas redéfinir inutilement dans QuoridorX ce qui est déjà défini dans Quoridor. Dans le constructeur de 
QuoridorX, commencez par faire appel au constructeur de Quoridor, puis faites les initialisations nécessaires 
pour créer la scêtre graphique, puis appelez votre méthode afficher. 

Pour créer votre scêtre graphique et y dessiner un damier avec l'état actuel du jeu, vous devez 
obligatoirement utiliser le module de la librairie standard nommé turtle. N'utilisez aucun autre 
module graphique. Vous trouverez un mini tutoriel sur turtle à l'onglet des documents afférents de ce 
projet. Si vous rencontrez des difficultés, n'hésitez pas à poser vos questions sur le forum.
"""
from quoridor import Quoridor
import turtle


class QuoridorX(Quoridor):
    def __init__(self):
        """Initialise les variables pour l'afifchage du jeu
        """
        super().__init__(self)
        self.scn = turtle.Screen()
        self.turtle = turtle.Turtle()
        self.clic = None

    def afficher(self):
        """Affiche la grille du jeu Quoridor à l'écran
        """
        GRID_SIZE = 600
        sub_divisions = 9
        cell_size = GRID_SIZE / sub_divisions
        cell_size = GRID_SIZE / float(sub_divisions)
        self.scn = self.turtle.Screen()
        self.scn.title("Quoridor")
        self.scn.setup(width=800, height=800)
        self.turtle.hideturtle()
        self.turtle.speed("fastest")
        self.turtle.penup()
        self.turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
        self.turtle.pendown()
        angle = 90
        for _ in range(4):
            self.turtle.forward(GRID_SIZE)
            self.turtle.right(angle)
        for _ in range(2):
            for _ in range(1, sub_divisions):
                self.turtle.forward(cell_size)
                self.turtle.right(angle)
                self.turtle.forward(GRID_SIZE)
                self.turtle.left(angle)
                angle = -angle
            self.turtle.forward(cell_size)
            self.turtle.right(angle)
        self.turtle.penup()
        self.turtle.goto(-GRID_SIZE/2 + 35, -GRID_SIZE/2 - 20)
        for x in range(9):
            self.turtle.write(f'{x + 1}', move=False, align='center', font=('Arial', 10, 'normal'))
            self.turtle.setx(-GRID_SIZE/2 + 35 + (x + 1) * 67)
        self.turtle.goto(-GRID_SIZE/2 - 20, -GRID_SIZE/2 + 25)
        for x in range(9):
            self.turtle.write(f'{x + 1}', move=False, align='center', font=('Arial', 10, 'normal'))
            self.turtle.sety(-GRID_SIZE/2 + 25 + (x + 1) * 67)
        
        def remplir(x, y):
            self.turtle.setposition(x // 800, y)
            self.turtle.stamp()
            position = self.turtle.pos()  
            print(position)
        
        self.turtle.onclick(remplir)
        scn.mainloop()



    def tracerClic(self, x, y):
        self.sc.onclick(None, btn=1)
        self.alex.setheading(self.alex.towards(x, y))
        self.alex.goto(x, y)
        self.sc.onclick(self.tracerClic, btn=1)

    def changerModeEcriture(self):
        self.sc.onkeypress(None, 'space')
        if self.alex.isdown():
            self.alex.penup()
            self.alex.fillcolor('white')
        else:
            self.alex.pendown()
            self.alex.fillcolor('black')
        self.sc.onkeypress(self.changerModeEcriture, 'space')
        
