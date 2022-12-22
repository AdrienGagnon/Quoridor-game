"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
import argparse
from api import débuter_partie, jouer_coup
from quoridor import Quoridor
from quoridorx import QuoridorX

# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = "af9cf9ec-a74d-401f-a0ac-56161ecf6e3a"


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par `parser.parse_args()`.
                    Cet objet a trois attributs: « idul » représentant l'idul
                    du joueur, « parties » qui est un booléen `True`/`False`
                    et « local » qui est un booléen `True`/`False`.
    """
    parser = argparse.ArgumentParser(description = 'Jeu Quoridor - phase 3')
    parser.add_argument(
        'idul', help='IDUL du joueur'
    )
    parser.add_argument(
        '-a', '--automatique', action="store_true",
        help='Activer le mode graphique.'
    )
    parser.add_argument(
        '-x', '--graphique', action="store_true",
        help='Activer le mode automatique.'
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = analyser_commande()
    if args.automatique:
        if args.graphique:
            #Manuel et graphique
            id_partie, état = débuter_partie(args.idul, SECRET)
            args_automatique = args.automatique
            args_idul = args.idul
            a = QuoridorX(état, id_partie, args_idul, args_automatique, SECRET)
            # Afficher la partie
            a.afficher()
        else:
            #Automatique non graphique
            id_partie, état = débuter_partie(args.idul, SECRET)
            # Instance de la classe
            while True:
                a = Quoridor(état)
                # Afficher la partie
                print(a)
                # Jouer automatiquement le prochain coup
                type_coup, position = a.jouer_le_coup(1)
                if type_coup == 'D':
                    état = a.déplacer_jeton(1, position)
                if type_coup == 'MH':
                    état = a.placer_un_mur(1, position, 'horizontal')
                if type_coup == 'MV':
                    état = a.placer_un_mur(1, position, 'vertical')
                # Envoyez le coup au serveur
                id_partie, état = jouer_coup(
                    id_partie,
                    type_coup,
                    position,
                    args.idul,
                    SECRET,
                )
    if args.graphique:
        #Manuel et graphique
        id_partie, état = débuter_partie(args.idul, SECRET)
        args_automatique = args.automatique
        args_idul = args.idul
        a = QuoridorX(état, id_partie, args_idul, args_automatique, SECRET)
        # Afficher la partie
        a.afficher()

    else:
        #Manuel non graphique
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            # Instance de la classe
            a = Quoridor(état)
            # Afficher la partie
            print(a)
            # Demander au joueur de choisir son prochain coup
            type_coup, position = a.récupérer_le_coup(1)
            if type_coup == 'D':
                état = a.déplacer_jeton(1, position)
            if type_coup == 'MH':
                état = a.placer_un_mur(1, position, 'horizontal')
            if type_coup == 'MV':
                état = a.placer_un_mur(1, position, 'vertical')
            # Envoyez le coup au serveur
            id_partie, état = jouer_coup(
                id_partie,
                type_coup,
                position,
                args.idul,
                SECRET,
            )
