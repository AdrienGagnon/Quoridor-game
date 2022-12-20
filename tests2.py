from graphe import construire_graphe
import networkx as nx
import matplotlib.pyplot as plt
"""
if __name__ == "__main__":
    état = {
        "joueurs": [
            {"nom": "Alfred", "murs": 7, "pos": [5, 5]},
            {"nom": "Robin", "murs": 3, "pos": [8, 6]},
        ],
        "murs": {
            "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
            "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]],
        },
    }
    graphe = construire_graphe(
        [joueur['pos'] for joueur in état['joueurs']],
        état['murs']['horizontaux'],
        état['murs']['verticaux']
    )
    objectif = {"B1": (5, 10)}
    #construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    #déplacements possibles
    print(list(graphe.successors((5,6))))
    #vérifier si chemin vers victoire
    print(nx.has_path(graphe, (5,6), "B1"))
    #chemin le plus rapide
    print(nx.shortest_path(graphe, (5,6), "B1"))
"""


import turtle


class App:
    def __init__(self, largeur, hauteur):
        self.fen = turtle.Screen()
        self.fen.setup(largeur, hauteur)
        self.fen.onclick(self.changerOrientation, btn=1)
        self.fen.onkeypress(self.changerModeEcriture, 'space')
        self.fen.listen()
        self.alex = turtle.Turtle()
        self.alex.speed('fastest')
        self.clic = None

    def changerOrientation(self, x, y):
        self.clic = turtle.Vec2D(x, y)

    def changerModeEcriture(self):
        self.fen.onkeypress(None, 'space')
        if self.alex.isdown():
            self.alex.penup()
            self.alex.fillcolor('white')
        else:
            self.alex.pendown()
            self.alex.fillcolor('black')
        self.fen.onkeypress(self.changerModeEcriture, 'space')

    def go(self):
        if self.clic:
            self.alex.setheading(self.alex.towards(self.clic))
            self.clic = None
        self.alex.forward(100)
        turtle.ontimer(x.go, 0)


x = App(800, 600)
turtle.ontimer(x.go, 0)
turtle.mainloop()