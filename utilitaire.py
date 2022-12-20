"""Module de fonctions utilitaires pour le jeu jeu Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
"""

import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par `parser.parse_args()`.
                    Cet objet a trois attributs: « idul » représentant l'idul
                    du joueur, « parties » qui est un booléen `True`/`False`
                    et « local » qui est un booléen `True`/`False`.
    """
    parser = argparse.ArgumentParser(description = 'Quoridor')
    parser.add_argument(
        '-p', '--parties', action="store_true", 
        help='Lister les parties existantes'
    )
    parser.add_argument(
        'idul', help='IDUL du joueur'
    )
    return parser.parse_args()


def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.
    Args:
        parties (list): Liste des parties
    Returns:
        str: Représentation des parties
    """
    numero_partie = 0
    text = []
    for partie in parties:
        numero_partie += 1
        joueurs_noms = partie["joueurs"]
        if partie["gagnant"] == None:
            text.append("{} : {}, {} vs {}".format(
                numero_partie, partie["date"], joueurs_noms[0], joueurs_noms[1]
            ))
        else:
            text.append("{} : {}, {} vs {}, gagnant: {}".format(
                numero_partie, partie["date"], joueurs_noms[0], joueurs_noms[1], partie["gagnant"]
            ))
    return "\n".join(text)
