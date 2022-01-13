import random

from pygame.math import Vector2

import core


class Ennemie:
    def __init__(self):
            self.position = Vector2(random.randint(0, 600), random.randint(0, 600))
            self.vitesse = Vector2(0, 0)
            self.acceleration = Vector2(0, 0)

            self.couleur = (0, 255, 0)
            self.taille = 10

            self.maxVitesse = 4
            self.maxAcceleration = 2

            self.vision = 100


    def afficher(self):
        core.Draw.circle(self.couleur, self.position, self.taille)


    def deplacement(self, vaisseau):
        vaisseauDansVision = []
        cable = None
        distanceCable = 10000

        # Emplacement
        self.rect = self.image.get_rect()
        self.position = (random.randrange(20, cfg.SCREENSIZE[0] - 20), -64)
        self.rect.left, self.rect.top = self.position

        # Vitesse
        self.speed = random.randrange(3, 9)
        self.angle = 0
        self.angular_velocity = random.randrange(1, 5)
        self.rotate_ticks = 3



        for p in vaisseau:
            if p.position.distance_to(self.position) < self.vision and p.vivante:
                vaisseauDansVision.append(p)
                if p.position.distance_to(self.position) < distanceCable:
                    cible = p
                    distanceCible = p.position.distance_to(self.position)

        if cable is not None:
            force = cable.position - self.position
            self.acceleration = force
        else:
            self.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        if self.acceleration.length() > self.maxAcceleration:
            self.acceleration.scale_to_length(self.maxAcceleration)

        self.vitesse = self.vitesse + self.acceleration

        if self.vitesse.length() > self.maxVitesse:
            self.vitesse.scale_to_length(self.maxVitesse)

        self.position = self.position + self.vitesse

        self.acceleration = Vector2(0, 0)





