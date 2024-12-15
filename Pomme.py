"""
pomme.py
--------
Classe pour gérer la logique de la pomme dans le jeu Snake.

Auteur : Evan
Date : 2024-12-13
"""

import random

class Pomme:
    """
    Représente la pomme dans le jeu Snake.
    Gère sa position sur la grille.
    """
    def __init__(self, largeur: int, hauteur: int):
        """
        Initialise une nouvelle pomme dans la grille.

        :param largeur: Largeur de la grille (en cases).
        :param hauteur: Hauteur de la grille (en cases).
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.position = self.generer_nouvelle_position()

    def generer_nouvelle_position(self) -> tuple[int, int]:
        """
        Génère une nouvelle position aléatoire pour la pomme.

        :return: Tuple représentant la position (x, y).
        """
        x = random.randint(0, self.largeur - 1)
        y = random.randint(0, self.hauteur - 1)
        return (x, y)