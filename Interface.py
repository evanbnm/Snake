"""
interface.py
------------
Classe pour gérer l'interface graphique du jeu Snake avec Tkinter.

Auteur : Evan
Date : 2024-12-13
"""

import tkinter as tk
from Jeu import Jeu

class Interface:
    """
    Classe pour l'interface graphique du jeu Snake.
    """
    def __init__(self, taille_case: int = 20):
        """
        Initialise la fenêtre Tkinter et le jeu.

        :param taille_case: Taille d'une case en pixels.
        """
        self.taille_case = taille_case
        self.jeu = Jeu()
        self.fenetre = tk.Tk()
        self.fenetre.title("Snake")
        self.fenetre.geometry("620x670")

        # Canvas pour afficher la grille
        self.canvas = tk.Canvas(
            self.fenetre,
            width=self.jeu.largeur * self.taille_case,
            height=self.jeu.hauteur * self.taille_case,
            bg="black"
        )
        self.canvas.pack()

        # Afficher un message de démarrage
        self.message_start = self.canvas.create_text(
            self.jeu.largeur * self.taille_case // 2,
            self.jeu.hauteur * self.taille_case // 2,
            text="Appuyez sur une touche pour commencer",
            fill="white",
            font=("Arial", 16)
        )

        # Ajouter le bouton Rejouer
        self.bouton_rejouer = tk.Button(self.fenetre, text="Rejouer", command=self.rejouer)
        self.bouton_rejouer.pack()
        self.bouton_rejouer.pack_forget()

        self.scoreLabel = tk.Label(self.fenetre, text="Score: " + str(self.jeu.score), font=("Arial", 16))
        self.scoreLabel.pack()

        self.fenetre.bind("<Key>", self.demarrer_jeu)

        # Désactiver la boucle de mise à jour avant le démarrage
        self.jeu_lance = False

    def demarrer_jeu(self, event=None):
        """
        Lance le jeu lorsque l'utilisateur appuie sur une touche.
        """
        if not self.jeu_lance:
            # Enlever le message de démarrage
            self.canvas.delete(self.message_start)

            # Associer les touches pour déplacer le serpent
            self.fenetre.bind("<Up>", lambda event: self.jeu.serpent.changer_direction((0, -1)))
            self.fenetre.bind("<Down>", lambda event: self.jeu.serpent.changer_direction((0, 1)))
            self.fenetre.bind("<Left>", lambda event: self.jeu.serpent.changer_direction((-1, 0)))
            self.fenetre.bind("<Right>", lambda event: self.jeu.serpent.changer_direction((1, 0)))

            self.jeu_lance = True
            self.mettre_a_jour()

    def dessiner_grille(self):
        """
        Dessine le serpent et la pomme sur le canvas.
        """
        self.canvas.delete("all")  # Effacer le contenu précédent

        # Dessiner le serpent
        for segment in self.jeu.serpent.corps:
            x1 = segment[0] * self.taille_case
            y1 = segment[1] * self.taille_case
            x2 = x1 + self.taille_case
            y2 = y1 + self.taille_case
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="")

        # Dessiner la pomme
        x1 = self.jeu.pomme.position[0] * self.taille_case
        y1 = self.jeu.pomme.position[1] * self.taille_case
        x2 = x1 + self.taille_case
        y2 = y1 + self.taille_case
        self.canvas.create_oval(x1, y1, x2, y2, fill="red", outline="")

        # Dessiner les murs
        for mur in self.jeu.murs:
            x1 = mur.position[0] * self.taille_case
            y1 = mur.position[1] * self.taille_case
            x2 = x1 + self.taille_case
            y2 = y1 + self.taille_case
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray", outline="")

    def mettre_a_jour(self):
        """
        Met à jour l'état du jeu et l'affichage.
        """
        if self.jeu.en_cours:
            self.jeu.mise_a_jour()
            self.dessiner_grille()
            self.fenetre.after(100, self.mettre_a_jour)  # Répéter après 100 ms
            self.scoreLabel.config(text="Score: " + str(self.jeu.score))
        else:
            self.afficher_message_fin()
            self.bouton_rejouer.pack()

    def afficher_message_fin(self):
        """
        Affiche un message de fin lorsque le jeu se termine.
        """
        self.canvas.create_text(
            self.jeu.largeur * self.taille_case // 2,
            self.jeu.hauteur * self.taille_case // 2,
            text="Game Over",
            fill="white",
            font=("Arial", 24)
        )

    def demarrer(self):
        """
        Lance la boucle principale de Tkinter.
        """
        self.fenetre.mainloop()

    def rejouer(self):
        """
        Réinitialise le jeu pour une nouvelle partie.
        """
        self.jeu = Jeu()
        self.jeu_lance = False
        self.bouton_rejouer.pack_forget()
        self.demarrer_jeu()