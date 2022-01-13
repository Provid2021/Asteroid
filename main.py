import pygame

from jeuAsteroids import core
from jeuAsteroids.Ennemie import Ennemie
from jeuAsteroids.Vaisseau import Vaisseau


def setup():
        print('SetUp :')
        core.WINDOW_SIZE=[600,600]
        core.fps=30

        core.memory("Vaisseau",[])
        core.memory("Ennemie",[])

        core.memory("nbVaisseau",1)
        core.memory("nbEnnemie",100)

        for i in range(0,core.memory("nbVaisseau")):
            core.memory("Vaisseau").append(Vaisseau())

        for i in range(0,core.memory("nbEnnemie")):
            core.memory("Ennemie").append(Ennemie())



def run():
        core.cleanScreen()


        #AFFICHAGE
        for p in core.memory("vaisseau"):
            p.afficher()
        for p in core.memory("ennemie"):
            p.afficher()

        #MISE A JOUR DES POSITIONS
        for p in core.memory("ennemie"):
            p.deplacement()
            p.bordure(core.WINDOW_SIZE)

        for p in core.memory("ennemie"):
            p.deplacement(core.memory("vaisseau"))
            p.bordure(core.WINDOW_SIZE)

        for p in core.memory("ennemie"):
            p.manger(core.memory("vaisseau"))




        # --Dessiner des balles
        for bullet in bullet_group:
            bullet.move()
        if pygame.sprite.spritecollide(bullet, asteroid_group, True, None):
            bullet_group.remove(bullet)
        if bullet.player_idx == 1:
            score_1 += 1
        else:
            score_2 += 1

        bullet.draw(screen)

        # --Dessiner un ennemie
        for ennemie in ennemie_group:
            ennemie.move()
            ennemie.rotate()
            ennemie.draw(screen)

        # MISE A JOUR DES POSITIONS
            for p in core.memory("vaisseau"):
                p.deplacement()
                p.bordure(core.WINDOW_SIZE)

            for p in core.memory("ennemie"):
                p.deplacement(core.memory("vaisseau"))
                p.bordure(core.WINDOW_SIZE)

            for p in core.memory("ennemie"):
                p.manger(core.memory("vaisseau"))

        # --Rafraîchissement de l'écran
            pygame.display.update()
            clock.tick(60)


core.main(setup,run)