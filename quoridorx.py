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
from api import jouer_coup
from quoridor import Quoridor
from copy import deepcopy
import turtle


class QuoridorX(Quoridor):
    def __init__(self, joueurs, id_partie, args_idul, args_automatique, SECRET, murs=None):
        """Initialise les variables pour l'afifchage du jeu
        """
        self.état = deepcopy(self.vérification(joueurs, murs))
        self.scn = turtle.Screen()
        self.turtle = turtle.Turtle()
        self.turtle2 = turtle.Turtle()
        self.joueur_1_stamp = None
        self.joueur_2_stamp = None
        self.turtle.color('black')
        self.grid_size = 600
        self.positions_possibles = {
            1:-4 * (self.grid_size / 2) / 4.5, 2:-3 * (self.grid_size / 2) / 4.5,
            3:-2 * (self.grid_size / 2) / 4.5, 4:-(self.grid_size / 2) / 4.5, 5:0,
            6:(self.grid_size / 2) / 4.5, 7:2 * (self.grid_size / 2) / 4.5,
            8:3 * (self.grid_size / 2) / 4.5, 9:4 * (self.grid_size / 2) / 4.5
        }
        self.positions_possibles_murs = {
            1:-self.grid_size / 2,
            2:(-4 * (self.grid_size / 2) / 4.5) + (((self.grid_size / 2) / 4.5) / 2),
            3:(-3 * (self.grid_size / 2) / 4.5) + (((self.grid_size / 2) / 4.5) / 2), 
            4:(-2 * (self.grid_size / 2) / 4.5) + (((self.grid_size / 2) / 4.5) / 2),
            5:-((self.grid_size / 2) / 4.5) / 2,
            6:((self.grid_size / 2) / 4.5) / 2,
            7:(1 * (self.grid_size / 2) / 4.5) + (((self.grid_size / 2) / 4.5) / 2),
            8:(2 * (self.grid_size / 2) / 4.5) + (((self.grid_size / 2) / 4.5) / 2),
            9:(3 * (self.grid_size / 2) / 4.5) + (((self.grid_size / 2) / 4.5) / 2)
        }
        self.clic = None
        self.id_partie = id_partie
        self.args_idul = args_idul
        self.args_automatique = args_automatique
        self.SECRET = SECRET
        self.numero_du_tour = 0
        """Notez bien que pour les murs horizontaux, nous avons 
        donc les contraintes 1≤x≤8 et 2≤y≤9, mais que pour les murs verticaux, elles sont plutôt 2≤x≤9 et 1≤y≤8.
        """

    def afficher(self):
        """Affiche la grille du jeu Quoridor à l'écran
        """
        self.turtle2.hideturtle()
        if self.numero_du_tour == 0:
            # Affichage grille
            self.grid_size = 600
            sub_divisions = 9
            cell_size = self.grid_size / sub_divisions
            cell_size = self.grid_size / float(sub_divisions)
            self.scn.title("Quoridor")
            self.scn.setup(width=800, height=800)
            #cacher le turtle
            self.turtle.hideturtle()
            #vitesse maximale
            self.turtle.speed("fastest")
            #aller au départ
            self.turtle.penup()
            self.turtle.goto(-self.grid_size/2, self.grid_size/2)
            self.turtle.pendown()
            #tracer la grille
            angle = 90
            for _ in range(4):
                self.turtle.forward(self.grid_size)
                self.turtle.right(angle)
            for _ in range(2):
                for _ in range(1, sub_divisions):
                    self.turtle.forward(cell_size)
                    self.turtle.right(angle)
                    self.turtle.forward(self.grid_size)
                    self.turtle.left(angle)
                    angle = -angle
                self.turtle.forward(cell_size)
                self.turtle.right(angle)
            # Ajout des chiffres de colonnes et rangées
            self.turtle.penup()
            self.turtle.goto(-self.grid_size/2 + 35, -self.grid_size/2 - 20)
            for x in range(9):
                self.turtle.write(f'{x + 1}', move=False, align='center', font=('Arial', 10, 'normal'))
                self.turtle.setx(-self.grid_size/2 + 35 + (x + 1) * 67)
            self.turtle.goto(-self.grid_size/2 - 20, -self.grid_size/2 + 25)
            for x in range(9):
                self.turtle.write(f'{x + 1}', move=False, align='center', font=('Arial', 10, 'normal'))
                self.turtle.sety(-self.grid_size/2 + 25 + (x + 1) * 67)
            self.turtle.goto(0, 330)
            if self.args_automatique is False:
                self.turtle.write("""Cliquez sur un mur ou au milieu de la grille\nExemple: Cliquer sur la grille inférieure à (5,6)
                              place un mur horizontal entre x = 5 et x = 6""")
        self.numero_du_tour += 1
        if isinstance(self.est_terminée, str):
            self.turtle.goto(0, 0)
            self.turtle.write(f'Bravo à {self.est_terminée} pour votre victoire', align='center', font=('Arial', 16, 'normal'))
            self.scn.listen()
            if self.turtle.onclick():
                self.scn.bye()
        #Ajout de la légende au-dessus de la grille
        self.turtle2.penup()
        self.turtle2.clear()
        self.turtle2.goto(-self.grid_size/2 + 20, self.grid_size/2)
        self.turtle2.write(self.formater_légende(), move=False, align='left', font=('Arial', 14, 'normal'))
        # Pastille des joueurs
        self.turtle.shape('circle')
        #Appel des fonction pour changer emplacement de la pastille des joueurs
        self.turtle.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=10)
        self.pastille_joueur_1()
        self.pastille_joueur_2()
        self.turtle.color('black')
        #Affichage des murs
        self.turtle.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=10)
        self.afficher_murs()
        #vérifier si automatique ou non
        if self.args_automatique is False:
            #clicker sur murs ou sur des emplacements vides
            self.scn.onclick(self.cliquer)
        else:
            self.continuer_partie()
        self.scn.update()
        self.scn.mainloop()
        return self.clic

    def pastille_joueur_1(self):
        if self.joueur_1_stamp is not None:
            self.turtle.clearstamp(self.joueur_1_stamp)
        x = self.état['joueurs']['joueurs'][0]['pos'][0]
        y = self.état['joueurs']['joueurs'][0]['pos'][1]
        self.turtle.setposition(self.positions_possibles[x], self.positions_possibles[y])
        self.turtle.color('blue')
        self.joueur_1_stamp = self.turtle.stamp()

    def pastille_joueur_2(self):
        if self.joueur_2_stamp is not None:
            self.turtle.clearstamp(self.joueur_2_stamp)
        x = self.état['joueurs']['joueurs'][1]['pos'][0]
        y = self.état['joueurs']['joueurs'][1]['pos'][1]
        self.turtle.setposition(self.positions_possibles[x], self.positions_possibles[y])
        self.turtle.color('red')
        self.joueur_2_stamp = self.turtle.stamp()

    def afficher_murs(self):
        murs_horizontaux = self.état['joueurs']['murs']['horizontaux']
        murs_vericaux = self.état['joueurs']['murs']['verticaux']
        self.turtle.color('black')
        self.scn.register_shape("rectangle_horizontal", ((0, -self.grid_size / 15), (0, self.grid_size / 15)))
        self.scn.register_shape("rectangle_vertical", ((-self.grid_size / 15, 0), (self.grid_size / 15, 0)))
        self.turtle.shape('rectangle_horizontal')
        for mur in murs_horizontaux:
            self.turtle.setposition(self.positions_possibles_murs[mur[0]] + (self.grid_size / 9), self.positions_possibles_murs[mur[1]])
            self.turtle.stamp()
        self.turtle.shape('rectangle_vertical')
        for mur in murs_vericaux:
            self.turtle.setposition(self.positions_possibles_murs[mur[0]], self.positions_possibles_murs[mur[1]] + (self.grid_size / 9))
            self.turtle.stamp()

    def cliquer(self, x, y):
        #Déplacer la pastille
        axe_x = None
        axe_y = None
        type_coup = None
        #mur hori ou verti
        for key, value in self.positions_possibles.items():
            if value - 15 < x < value + 15:
                axe_x = key
            if value - 15 < y < value + 15:
                axe_y = key
        if axe_x is not None and axe_y is not None:
            type_coup = 'D'
        for value in self.positions_possibles_murs.values():
            if value - 15 < y < value + 15:
                type_coup = 'MH'
        if type_coup is None:
            type_coup = 'MV'
        for key, value in self.positions_possibles_murs.items():
            if value - 15 < x < value + 15:
                axe_x = key
            if value - 15 < y < value + 15:
                axe_y = key
        if axe_x is None or axe_y is None:
            self.turtle.goto(0, 310)
            self.turtle.write('Assurez-vous de bien cliquer sur un mur ou au milieu de la grille')
            self.afficher()
        self.clic = (type_coup, [axe_x, axe_y])
        self.continuer_partie()

    def continuer_partie(self):
        if self.args_automatique is True:
            type_coup, position = self.jouer_le_coup(1)
        else:
            type_coup, position = self.clic
            # Demander au joueur de choisir son prochain coup
        if type_coup == 'D':
            self.état = self.déplacer_jeton(1, position)
        if type_coup == 'MH':
            self.état = self.placer_un_mur(1, position, 'horizontal')
        if type_coup == 'MV':
            self.état = self.placer_un_mur(1, position, 'vertical')
        # Envoyez le coup au serveur
        self.id_partie, self.état = jouer_coup(
            self.id_partie,
            type_coup,
            position,
            self.args_idul,
            self.SECRET,
        )
        self.afficher()
