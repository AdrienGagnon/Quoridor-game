"""Module de la classe Quoridor

Classes:
    * Quoridor - Classe pour encapsuler le jeu Quoridor.
"""
from copy import deepcopy

from quoridor_error import QuoridorError

from graphe import construire_graphe

import networkx as nx

import matplotlib.pyplot as plt


class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.

    Vous ne devez pas créer d'autre attributs pour votre classe.

    Attributes:
        état (dict): état du jeu tenu à jour.
    """

    def __init__(self, joueurs, murs=None):
        """Constructeur de la classe Quoridor.

        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        Appel la méthode `vérification` pour valider les données et assigne
        ce qu'elle retourne à l'attribut `self.état`.

        Cette méthode ne devrait pas être modifiée.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        """
        self.état = deepcopy(self.vérification(joueurs, murs))
    
    def vérification(self, joueurs, murs):
        """Vérification d'initialisation d'une instance de la classe Quoridor.

        Valide les données arguments de construction de l'instance et retourne
        l'état si valide.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de list [x, y] uniquement.
        Raises:
            okQuoridorError: L'argument 'joueurs' n'est pas itérable.
            okQuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            okQuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            okQuoridorError: La position d'un joueur est invalide.
            okQuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            okQuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            ok à vérifier QuoridorError: La position d'un mur est invalide.
        """
        if isinstance(joueurs['joueurs'], list):
            if isinstance(joueurs['joueurs'][0], str):
                if len(joueurs) != 2:
                    raise QuoridorError(
                        "L'itérable de joueurs en contient un nombre différent de deux."
                    )
        if isinstance(joueurs['joueurs'], list):
            if isinstance(joueurs['joueurs'][0], dict):
                if len(joueurs['joueurs']) != 2:
                    raise QuoridorError(
                        "L'itérable de joueurs en contient un nombre différent de deux."
                    )
                for joueur in joueurs['joueurs']:
                    if joueur["murs"] < 0 or joueur["murs"] > 10:
                        raise QuoridorError(
                            "Le nombre de murs qu'un joueur peut placer est plus grand que 10, ou négatif."
                        )
                    position = joueur["pos"]
                    for axe in position:
                        if axe < 1 or axe > 9:
                            raise QuoridorError("La position d'un joueur est invalide.")
        else:
            raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")
        joueur1 = joueurs['joueurs'][0]
        joueur2 = joueurs['joueurs'][1]
        somme_tous_les_murs = joueur1["murs"] + joueur2["murs"]
        murs = joueurs['murs']
        if type(murs) is not dict:
            raise QuoridorError(
                "L'argument 'murs' n'est pas un dictionnaire lorsque présent."
            )
        for mur in murs["horizontaux"]:
            if mur[0] < 1 or mur[0] > 8 or mur[1] < 2 or mur[1] > 9:
                raise QuoridorError("La position d'un mur est invalide.")
        for mur in murs["verticaux"]:
            if mur[0] < 2 or mur[0] > 9 or mur[1] < 1 or mur[1] > 8:
                raise QuoridorError("La position d'un mur est invalide.")
        somme_murs_places = len(murs["horizontaux"]) + len(murs["verticaux"])
        somme_tous_les_murs += somme_murs_places
        if somme_tous_les_murs != 20:
            raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20.")
        dictio = {}
        dictio["joueurs"] = joueurs
        if murs is None:
            dictio["murs"] = {"horizontaux":[], "verticaux":[]}
        else:
            dictio["murs"] = murs
        return dictio

    def formater_légende(self):
        """Formater la représentation graphique de la légende.

        Returns:
            str: Chaîne de caractères représentant la légende.
        """
        if isinstance(self.état['joueurs'], list):
            self.état = {'joueurs':self.état, 'murs':{'horizontaux':[], 'verticaux':[]}}
        longueur_idul = numero_du_joueur = 0
        for dictio in self.état["joueurs"]["joueurs"]:
            idul = dictio["nom"]
            if len(idul) > longueur_idul:
                longueur_idul = len(idul)
        legende = "Légende:\n"
        for dictio in self.état["joueurs"]["joueurs"]:
            numero_du_joueur += 1
            idul = dictio["nom"]
            murs_restants = dictio["murs"]
            legende += "   {}={},{} murs={}\n".format(
                numero_du_joueur, idul, (longueur_idul - len(idul)) * " ", murs_restants * "|"
            )
        return legende

    def formater_damier(self):
        """Formater la représentation graphique du damier.

        Returns:
            str: Chaîne de caractères représentant le damier.
        """
        damier = ["   -----------------------------------\n",
            "9 | .   .   .   .   .   .   .   .   . |\n",
            "  |                                   |\n",
            "8 | .   .   .   .   .   .   .   .   . |\n",
            "  |                                   |\n",
            "7 | .   .   .   .   .   .   .   .   . |\n",
            "  |                                   |\n",
            "6 | .   .   .   .   .   .   .   .   . |\n",
            "  |                                   |\n",
            "5 | .   .   .   .   .   .   .   .   . |\n",
            "  |                                   |\n",
            "4 | .   .   .   .   .   .   .   .   . |\n",
            "  |                                   |\n",
            "3 | .   .   .   .   .   .   .   .   . |\n",
            "  |                                   |\n",
            "2 | .   .   .   .   .   .   .   .   . |\n",
            "  |                                   |\n",
            "1 | .   .   .   .   .   .   .   .   . |\n",
            "--|-----------------------------------\n",
            "  | 1   2   3   4   5   6   7   8   9\n"]
        liste = []
        for ligne in damier:
            liste_damier = list(ligne)
            liste.append(liste_damier)
        # On a une liste de listes de caractères de chaque ligne.
        numero_du_joueur = 0
        for identite in self.état["joueurs"]["joueurs"]:
            numero_du_joueur += 1
            liste_position = identite["pos"]
            liste[19 - 2 * liste_position[1]][4 + 4 * (liste_position[0] - 1)] = f"{numero_du_joueur}"
        for couple in self.état["joueurs"]["murs"]["horizontaux"]:
            rangee = 19 - 2 * couple[1]
            colonne = couple[0]
            index_a_changer = range(3 + 4 * (colonne - 1), 10 + 4 * (colonne - 1))
            for index, caractere in enumerate(liste[rangee]):
                if index in index_a_changer:
                    liste[20 - 2 * couple[1]][index] = "-"
        for couple in self.état["joueurs"]["murs"]["verticaux"]:
            x = couple[0]
            y = couple[1]
            rangees = range(17 - 2 * y, 20 - 2 * y)
            colonne = (x - 1) * 4 + 2
            for index, ligne in enumerate(liste):
                if index in rangees:
                    liste[index][colonne] = "|"
        damier_corrige = ""
        for ligne in liste:
            damier_corrige += "".join(ligne)
        return damier_corrige

    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.

        Cette représentation est la même que celle du projet précédent.

        Returns:
            str: La chaîne de caractères de la représentation.
        """
        return f"{self.formater_légende()}{self.formater_damier()}"

    def état_courant(self):
        """Produire l'état actuel du jeu.

        Cette méthode ne doit pas être modifiée.

        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)

    def est_terminée(self):
        """Déterminer si la partie est terminée.

        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        if self.état["joueurs"]["joueurs"][0]["pos"][1] == 9:
            return self.état["joueurs"]["joueurs"][0]["noms"]
        if self.état["joueurs"]["joueurs"][1]["pos"][1] == 1:
            return self.état["joueurs"]["joueurs"][1]["noms"]
        return False

    def récupérer_le_coup(self, joueur):
        """Récupérer le coup

        Notez que seul 2 questions devrait être posée à l'utilisateur.

        Notez aussi que cette méthode ne devrait pas modifier l'état du jeu.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            ok QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            ok QuoridorError: Le type de coup est invalide.
            ok QuoridorError: La position est invalide (en dehors du damier).

        Returns:
            tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
        """
        if joueur != 1 and joueur != 2:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        type_coup = input("Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):")
        position = input("Donnez la position où appliquer ce coup (x,y):")
        type_coup = type_coup.upper()
        if type_coup != "D" and type_coup != "MH" and type_coup != "MV":
            raise QuoridorError("Le type de coup est invalide.")
        position = list(position)
        position.pop(1)
        nouvelles_positions = []
        for x in position:
            if int(x) < 1 or int(x) > 9:
                raise QuoridorError("La position est invalide (en dehors du damier).")
            else:
                nouvelles_positions.append(int(x))
        return (type_coup, nouvelles_positions)

    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.

        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (List[int, int]): La liste [x, y] de la position du jeton (1<=x<=9 et 1<=y<=9).

        Raises:
            ok QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            ok QuoridorError: La position est invalide (en dehors du damier).
            ok QuoridorError: La position est invalide pour l'état actuel du jeu.
        """
        if joueur != 1 and joueur != 2:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        for axe in position:
            if axe < 1 or axe > 9:
                raise QuoridorError("La position est invalide (en dehors du damier).")
        graphe = construire_graphe(
            [joueur["pos"] for joueur in self.état["joueurs"]["joueurs"]],
            self.état["murs"]["horizontaux"],
            self.état["murs"]["verticaux"]
        )
        positions_valides = graphe.successors(tuple(self.état["joueurs"]["joueurs"][joueur - 1]["pos"]))
        if not tuple(position) in positions_valides:
            raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
        self.état['joueurs']["joueurs"][joueur - 1]["pos"] = position
        return self.état

    def placer_un_mur(self, joueur, position, orientation):
        """Placer un mur.

        Pour le joueur spécifié, placer un mur à la position spécifiée.

        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (List[int, int]): la liste [x, y] de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').

        Raises:
            ok QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            ok QuoridorError: Un mur occupe déjà cette position.
            ok QuoridorError: La position est invalide pour cette orientation.
            ok QuoridorError: Le joueur a déjà placé tous ses murs.
        """
        if orientation == "horizontal":
            orientation = "horizontaux"
        if orientation == "vertical":
            orientation = "verticaux"
        if joueur != 1 and joueur != 2:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        if self.état["joueurs"]["joueurs"][joueur - 1]["murs"] == 0:
            raise QuoridorError("Le joueur a déjà placé tous ses murs.")
        for mur in self.état["joueurs"]["murs"][orientation]:
            if mur == position:
                raise QuoridorError("Un mur occupe déjà cette position.")
        if orientation == "horizontaux":
            if position[0] < 1 or position[0] > 8 or position[1] < 2 or position[1] > 9:
                raise QuoridorError("La position est invalide pour cette orientation.")
        if orientation == "verticaux":
            if position[0] < 2 or position[0] > 9 or position[1] < 1 or position[1] > 8:
                raise QuoridorError("La position est invalide pour cette orientation.")
        self.état["joueurs"]["joueurs"][joueur - 1]["murs"] = self.état["joueurs"]["joueurs"][joueur - 1]["murs"] - 1
        #ajouter un murs à la liste
        self.état["joueurs"]["murs"][orientation].append(position)
        return self.état

    def jouer_le_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.

        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            ok QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            ok QuoridorError: La partie est déjà terminée.

        Returns:
            Tuple[str, List[int, int]]: Un tuple composé du type et de la position du coup joué.
        """
        if joueur != 1 and joueur != 2:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        if self.est_terminée():
            raise QuoridorError("La partie est déjà terminée.")
        #Le meilleur coup à jouer
        graphe = construire_graphe(
            [joueur["pos"] for joueur in self.état["joueurs"]["joueurs"]],
            self.état['joueurs']["murs"]["horizontaux"],
            self.état['joueurs']["murs"]["verticaux"]
        )
        positions = {'B1': (5, 10), 'B2': [5, 0]}
        chemin = nx.shortest_path(graphe, (self.état["joueurs"]["joueurs"][joueur - 1]["pos"][0], 
                                        self.état["joueurs"]["joueurs"][joueur - 1]["pos"][1]), "B1")
        #mise à jour position
        type_coup = 'D'
        position = chemin[1]
        return (type_coup, position)
