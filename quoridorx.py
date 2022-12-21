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
from copy import deepcopy
import turtle


class QuoridorX(Quoridor):
    def __init__(self, joueurs, murs=None):
        """Initialise les variables pour l'afifchage du jeu
        """
        self.état = deepcopy(self.vérification(joueurs, murs))
        self.scn = turtle.Screen()
        self.turtle = turtle.Turtle()
        self.joueur_1_stamp = None
        self.joueur_2_stamp = None
        self.turtle.color('black')
        self.positions_possibles = {1:-267, 2:-200, 3:-133, 2:-66.7, 5:0, 6:66.7, 7:133, 8:200, 9:267}
        self.positions_possibles_murs_horiz = {1:-300, 2:-200, 3:-100, 2:-33.3,6:33.3, 7:100, 8:166., 9:300}
        self.positions_possibles_murs_verti = {1:-300, 2:-200, 3:-100, 2:-33.3, 6:33.3, 7:100, 8:166., 9:300}
        self.clic = None
        """Notez bien que pour les murs horizontaux, nous avons 
        donc les contraintes 1≤x≤8 et 2≤y≤9, mais que pour les murs verticaux, elles sont plutôt 2≤x≤9 et 1≤y≤8.
        """

    def afficher(self):
        """Affiche la grille du jeu Quoridor à l'écran
        """
        # Affichage grille
        GRID_SIZE = 600
        sub_divisions = 9
        cell_size = GRID_SIZE / sub_divisions
        cell_size = GRID_SIZE / float(sub_divisions)
        self.scn.title("Quoridor")
        self.scn.setup(width=800, height=800)
        #cacher le turtle
        self.turtle.hideturtle()
        #vitesse maximale
        self.turtle.speed("fastest")
        #aller au départ
        self.turtle.penup()
        self.turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
        self.turtle.pendown()
        #tracer la grille
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
        # Ajout des chiffres de colonnes et rangées
        self.turtle.penup()
        self.turtle.goto(-GRID_SIZE/2 + 35, -GRID_SIZE/2 - 20)
        for x in range(9):
            self.turtle.write(f'{x + 1}', move=False, align='center', font=('Arial', 10, 'normal'))
            self.turtle.setx(-GRID_SIZE/2 + 35 + (x + 1) * 67)
        self.turtle.goto(-GRID_SIZE/2 - 20, -GRID_SIZE/2 + 25)
        for x in range(9):
            self.turtle.write(f'{x + 1}', move=False, align='center', font=('Arial', 10, 'normal'))
            self.turtle.sety(-GRID_SIZE/2 + 25 + (x + 1) * 67)
        #Ajout de la légende au-dessus de la grille
        self.turtle.goto(-GRID_SIZE/2 + 100, GRID_SIZE/2)
        self.turtle.write(self.formater_légende(), move=False, align='center', font=('Arial', 14, 'normal'))
        # Pastille des joueurs
        self.turtle.shape('circle')
        #supprimer pastille précédente
        if self.joueur_1_stamp is not None:
            turtle.clearstamp(self.joueur_1_stamp)
        if self.joueur_2_stamp is not None:
            turtle.clearstamp(self.joueur_2_stamp)
        #Appel des fonction pour changer emplacement de la pastille des joueurs
        self.turtle.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=10)
        self.pastille_joueur_1()
        self.pastille_joueur_2()
        self.turtle.color('black')
        #Affichage des murs
        self.turtle.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=10)
        self.afficher_murs()
        #clicker sur murs ou sur des emplacements vides
        def remplir(x, y):
            self.turtle.setposition(x // 800, y)
            self.turtle.stamp()
            position = self.turtle.pos()  
            print(position)
        
        self.turtle.onclick(remplir)
        self.scn.mainloop()

    def pastille_joueur_1(self):
        x = self.état['joueurs']['joueurs'][0]['pos'][0]
        y = self.état['joueurs']['joueurs'][0]['pos'][1]
        self.turtle.setposition(self.positions_possibles[x], self.positions_possibles[y])
        self.turtle.color('blue')
        joueur_1_stamp = self.turtle.stamp()
        return joueur_1_stamp

    def pastille_joueur_2(self):
        x = self.état['joueurs']['joueurs'][1]['pos'][0]
        y = self.état['joueurs']['joueurs'][1]['pos'][1]
        self.turtle.setposition(self.positions_possibles[x], self.positions_possibles[y])
        self.turtle.color('red')
        joueur_2_stamp = self.turtle.stamp()
        return joueur_2_stamp

    def afficher_murs(self):
        pass

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
