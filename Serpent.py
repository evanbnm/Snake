"""
Serpent.py
----------
Classe pour gérer la logique du serpent dans le jeu Snake.

Auteur : Evan
Date : 2024-12-13
"""

class Serpent:
    """
    Représente le serpent dans le jeu Snake.
    Gère sa position, sa direction, sa croissance, et les collisions.
    """
    def __init__(self, position_initiale: tuple[int, int], taille_initiale: int = 3):
        """
        Initialise le serpent avec une position et une taille initiales.

        :param position_initiale: Position de départ du serpent (x, y).
        :param taille_initiale: Longueur initiale du serpent.
        """
        self.corps = [position_initiale]  # Liste des segments (x, y)
        for i in range(1, taille_initiale):
            self.corps.append((position_initiale[0] - i, position_initiale[1]))
        self.direction = (1, 0)  # Direction initiale (droite).

    def changer_direction(self, nouvelle_direction: tuple[int, int]):
        """
        Change la direction du serpent, si elle n'est pas opposée à la direction actuelle.

        :param nouvelle_direction: Nouvelle direction (dx, dy).
        """
        dx, dy = nouvelle_direction
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = nouvelle_direction

    def avancer(self):
        """
        Fait avancer le serpent dans sa direction actuelle.
        Supprime la dernière partie du corps (si pas de croissance).
        """
        tete = self.corps[0]
        nouvelle_tete = (tete[0] + self.direction[0], tete[1] + self.direction[1])
        self.corps = [nouvelle_tete] + self.corps[:-1]

    def grandir(self):
        """
        Fait grandir le serpent d'une unité.
        Garde l'ancienne queue intacte.
        """
        self.corps.append(self.corps[-1])

    def verifier_collision(self) -> bool:
        """
        Vérifie si le serpent entre en collision avec lui-même.

        :return: True si collision détectée, False sinon.
        """
        tete = self.corps[0]
        return tete in self.corps[1:]