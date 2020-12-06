import pygame
import os
import time
import random
# -------------FONDOS Y LETRAS
pygame.font.init()
WIDTH, HEIGHT = 400, 600
VEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jueguito")
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("Imagenes", "fondo.jpg")), (WIDTH, HEIGHT))


# ----------IMAGENES---------------
rWall = pygame.image.load("Imagenes/wall.png")
rW = rWall.get_rect()
# --------------------MUSICA
pygame.mixer.pre_init(22050, -16, 2, 256)
pygame.mixer.init()
# pygame.mixer.music.load("Gamepython/Imagenes/musica.mp3")
# pygame.mixer.music.play(-1)
beat = pygame.mixer.Sound("Imagenes/beat.wav")


# ----------------CLASS
class Sprite:
    def __init__(self, x, y, vida=100):
        self.x = x
        self.y = y
        self.vida = vida
        self.Plyr_img = None

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 255), (self.x, self.y, 50, 50))


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 2))

# -----------MAIN LOOP


def main():
    run = True
    FPS = 60
    ywal = 1
    clock = pygame.time.Clock()
    plyr = Sprite((WIDTH-WIDTH/3.3), HEIGHT-60)
    enemy = Wall(0, 100)


# --------------REDRAW SPRITES AND FONTS--------------------

    def redraw_window():
        VEN.blit(BG, (0, 0))
        pygame.draw.rect(VEN, (0, 40, 40), (0, 100, 50, 116))
        plyr.draw(VEN)
        enemy.draw(VEN)

    # --------WHILE RUN-----------------
    while run:

        clock.tick(FPS)
        redraw_window()
        # -------BEAT---------------
        BEAT = 80
        ywal += (BEAT/30)
        if enemy.y <= 216:
            enemy.y += (BEAT/30)
        if enemy.y > 216:
            beat.play()
            enemy.y = 100

        VEN.blit(rWall, (220, ywal))
        VEN.blit(rWall, (20, ywal))
        pygame.display.update()

        # --------WALL--------

        # ----------QUIT----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # --------KEYS----------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and plyr.x > (WIDTH/2):
                    plyr.x = 50
                else:
                    if event.key == pygame.K_a and plyr.x < (WIDTH/2):
                        plyr.x = (WIDTH - 100)


main()
