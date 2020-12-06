import pygame
import os
import time
import random
#-------------FONDOS Y LETRAS
pygame.font.init()
WIDTH, HEIGHT = 400, 600
VEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jueguito")
BG = pygame.transform.scale(pygame.image.load(os.path.join("Imagenes", "fondo.jpg")), (WIDTH, HEIGHT))


#----------IMAGENES---------------
rectangulo_feo=pygame.image.load("Imagenes/wall.png")
#rW = rectangulo_feo.get_rect()
# --------------------MUSICA
pygame.mixer.pre_init(22050, -16, 2, 256)
pygame.mixer.init()
beat = pygame.mixer.Sound("Imagenes/beat.wav")
#pygame.mixer.music.load("Gamepython/Imagenes/musica.mp3")
#pygame.mixer.music.play(-1)

#-------------------------------------------------------
#----------------CLASES---------------------------------
#-------------------------------------------------------


class Sprite:
    def __init__(self,x,y, vida=100):
        self.x = x
        self.y = y
        self.vida = vida
        self.Plyr_img = None

    def draw(self, window):
        #rectangulo (en la ventana ( color), (ubicacion, tamaño))
        pygame.draw.rect(window, (255,0,255),(self.x, self.y, 50, 20 ))

class Barra_roja_tempo:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def draw(self, window):
        pygame.draw.rect(window, (255,0,0),(self.x, self.y, 50, 2))


class Barra_enemiga:
    def __init__(self,x,y):
        self.x = x
        self.y = y
       # self.img_barra = pygame.image.load("Imagenes/wall.png")
    
    def draw(self, window):
        window.blit(self.img_barra,(self.x, self.y))

class BarraI(Barra_enemiga):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.img_barra=rectangulo_feo
        self.mask = pygame.mask.from_surface(self.img_barra)

class LineaT:
    def __init__(self,y):
        self.y=y
    
    def draw(self, window):
        pygame.draw.rect(window, (100,40,40),(0, self.y, WIDTH, 2))

#-----------------------------------
#-----------MAIN LOOP---------------
#-----------------------------------


def main():
    run = True
    FPS = 60
    #level = 1
    #lives = 5
    y_speed = 1
    const_tiempo=116
    clock = pygame.time.Clock()

    #main_font = pygame.font.SysFont("comicsans", 30)

    plyr = Sprite(int(WIDTH-WIDTH/3.3),HEIGHT-60)
    barrita = Barra_roja_tempo(0,100)  

    linea3 = LineaT(HEIGHT-60-const_tiempo*4)
    linea2 = LineaT(HEIGHT-60-const_tiempo*2)
    linea1 = LineaT(HEIGHT-60)

    #linea2 = pygame.draw.rect(VEN,(0,40,40),(0,HEIGHT-60-const_tiempo*2,WIDTH, 2))
    #linea1 = pygame.draw.rect(VEN,(200,40,40),(0,HEIGHT-60,WIDTH , 2))

    barra_enemy = BarraI(20,HEIGHT-60-const_tiempo*6-20)
    barra_enemy2= BarraI(220,HEIGHT-60-const_tiempo*6-20)


#--------------REDRAW SPRITES AND FONTS--------------------
    def redraw_window():
        #fondo
        VEN.blit(BG, (0,0))
        #rectangulo del tempo
        const_tiempo=116
        pygame.draw.rect(VEN,(0,40,40),(0,100, 50, const_tiempo))

        #linea tempo
        

        linea3.draw(VEN)
        linea2.draw(VEN)
        linea1.draw(VEN)




        #el jugador
        plyr.draw(VEN)
        #barra tempo
        barrita.draw(VEN)
        #barra enemigos
        barra_enemy.draw(VEN)
        barra_enemy2.draw(VEN)



    #--------WHILE RUN-----------------
    while run:
        
        clock.tick(FPS)
        redraw_window()
        #-------BEAT---------------
        BEAT=60
        y_speed += (int(BEAT/30))
        if barrita.y <= 216:
            barrita.y +=(int(BEAT/30))
            pygame.draw.rect(VEN,(0,40,40),(185,10, 20, 20))
            
        
        if barrita.y > 216:
            beat.play()
            barrita.y = 100
        
        
        if barrita.y >210 or barrita.y < 107:
            pygame.draw.rect(VEN,(100,40,40),(185,10, 20, 20))
        if barrita.y >214: 
            pygame.draw.rect(VEN,(220,40,40),(185,10, 20, 20))

        



        #---paredes----   
        # y_speed, es la coordenada y que va creciendo por el += beat


        if barra_enemy.y <= HEIGHT:
            barra_enemy.y +=(int(BEAT/30*2))
        if barra_enemy.y > HEIGHT:
            barra_enemy.y = (HEIGHT-60-const_tiempo*6)+50
            

        if barra_enemy2.y <= HEIGHT:
            barra_enemy2.y +=(int(BEAT/30*2))
        if barra_enemy2.y > HEIGHT:
            barra_enemy2.y = (HEIGHT-60-const_tiempo*6)+50
        
        if barra_enemy.y == (HEIGHT-60-const_tiempo*4):
            barra_enemy.draw(VEN)
        

        
        #VEN.blit(rectangulo_feo, (20, y_speed*2 - BEAT*2))
       
        


        pygame.display.update()

        #--------WALL--------


        #----------QUIT----------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            #--------KEYS----------------    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and plyr.x > (int(WIDTH/2)):
                    plyr.x = 50
                else:
                    if event.key == pygame.K_a and plyr.x < (int(WIDTH/2)):
                        plyr.x = (WIDTH - 100)

   

main()

