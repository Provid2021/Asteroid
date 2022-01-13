import random

from pygame.math import Vector2

import core


class Proie:
        def __init__(self):
            self.position=Vector2(random.randint(0,600),random.randint(0,600))
            self.vitesse = Vector2(0,0)
            self.acceleration = Vector2(0,0)


            self.couleur = (0,0,255)
            self.taille = 4

            self.maxVitesse = 3
            self.maxAcceleration = 1

        def afficher(self):
            if self.vivante:
                core.Draw.circle(self.couleur, self.position, self.taille)
            else:
                core.Draw.circle((0, 0, 0), self.position, self.taille)

        def deplacement(self):

            if self.acceleration.length() > self.maxAcceleration:
                        self.acceleration.scale_to_length(self.maxAcceleration)

            self.vitesse = self.vitesse + self.acceleration

            if self.vitesse.length() > self.maxVitesse:
                        self.vitesse.scale_to_length(self.maxVitesse)
            self.position = self.position + self.vitesse

            self.acceleration = Vector2(0, 0)
