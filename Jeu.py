"""
jeu.py
------
Classe principale pour gérer les règles du jeu Snake.

Auteur : Evan
Date : 2024-12-13
"""

from Serpent import Serpent
from Pomme import Pomme
from Mur import Mur

class Jeu:
    """
    Classe pour gérer le déroulement du jeu Snake.
    Combine les éléments Serpent et Pomme, et vérifie les règles.
    """
    def __init__(self, largeur: int = 30, hauteur: int = 30):
        """
        Initialise le jeu avec un serpent et une pomme dans une grille donnée.

        :param largeur: Largeur de la grille (en cases).
        :param hauteur: Hauteur de la grille (en cases).
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.serpent = Serpent(position_initiale=(largeur // 2, hauteur // 2))
        self.pomme = Pomme(largeur, hauteur)
        self.en_cours = True
        self.murs = []
        self.score = 0

    def mise_a_jour(self):
        """
        Met à jour l'état du jeu :
        - Fait avancer le serpent.
        - Vérifie les collisions et la consommation de la pomme.
        """
        if not self.en_cours:
            return

        # Avancer le serpent
        self.serpent.avancer()

        # Vérifier les collisions avec les bords
        tete = self.serpent.corps[0]
        if tete[0] < 0 or tete[1] < 0 or tete[0] >= self.largeur or tete[1] >= self.hauteur:
            self.en_cours = False
            return

        # Vérifier les collisions avec lui-même
        if self.serpent.verifier_collision():
            self.en_cours = False
            return
        
        # Vérifier les collisions avec les murs
        for mur in self.murs:
            if tete == mur.position:
                self.en_cours = False
                return
    
        # Vérifier si le serpent mange la pomme
        if tete == self.pomme.position:
            self.serpent.grandir()
            self.score += 1
            self.pomme.position = self.generer_position_valide_pomme()
            self.generer_mur()

    def generer_position_valide_pomme(self) -> tuple[int, int]:
        """
        Génère une position valide pour la pomme, hors du corps du serpent.

        :return: Tuple représentant une position (x, y).
        """
        while True:
            position = self.pomme.generer_nouvelle_position()
            if position not in self.serpent.corps:
                return position
            
    def generer_mur(self):
        """
        Génère un mur à une position aléatoire.
        """
        while True:
            mur = Mur(self.largeur, self.hauteur)
            if mur.position not in self.serpent.corps and mur.position != self.pomme.position:
                if mur.position not in [m.position for m in self.murs]:
                    self.murs.append(mur)
                    break
       