"""
Mur.py
------------
Classe pour gérer les murs du jeu Snake avec Tkinter.

Auteur : Evan
Date : 2024-12-13
"""

import random

class Mur:
    """
    Classe pour gérer les murs dans le jeu Snake.
    """
    def __init__(self, largeur: int, hauteur: int):
        """
        Initialise les murs du jeu.

        :param largeur: Largeur de la grille (en cases).
        :param hauteur: Hauteur de la grille (en cases).
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.position = self.generer_nouvelle_position()

    def generer_nouvelle_position(self) -> tuple[int, int]:
        """
        Génère une nouvelle position aléatoire pour un mur.

        :return: Tuple représentant la position (x, y).
        """
        x = random.randint(0, self.largeur - 1)
        y = random.randint(0, self.hauteur - 1)
        return (x, y)