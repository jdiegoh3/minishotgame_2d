import pygame
import random
import sys
import os
curdir = os.getcwd()+"/sources"

blanco=(255,255,255)
rojo=(255,0,0)
#Algoritmo de Bresenham para la recta
def Bresenhamecta((x0,y0),(x1,y1),pantalla):
    dx=x1-x0
    dy=y1-y0
    res=[]
    if(dy < 0 ):
        dy=-1*dy
        stepy=-1
    else:
        stepy=1
    if(dx<0):
        dx=-1*dx
        stepx=-1
    else:
        stepx=1
        x=x0
        y=y0
    res.append((x,y))
    if(dx>dy):
        p=2*dy-dx
        incE=2*dy
        incNE=2*(dy-dx)
        while(x != x1):
            x=x+stepx
            if(p<0):
                p=p+incE
            else:
                y=y+stepy
                p=p+incNE
        res.append((x,y))
    else:
        p=2*dx-dy
        incE=2*dx
        incNE=2*(dx-dy)
        while(y != y1):
            y=y+stepy
            if(p<0):
                p=p+incE
            else:
                x=x+stepx
                p=p+incNE
        res.append((x,y))
#fin Algoritmo de Bresenham para la recta

#Dibuja los 8 octantes para el Algoritmo de Bresenham para la circunferencia
def plotpoint((x0,y0),(x,y),pantalla,res):
    res.append((x0+x,y0+y))
    res.append((x0-x,y0+y))
    res.append((x0+x,y0-y))
    res.append((x0-x,y0-y))
    res.append((x0+y,y0+x))
    res.append((x0-y,y0+x))
    res.append((x0+y,y0-x))
    res.append((x0-y,y0-x))
#Fin dibuja 8 octantes Algoritmo de Bresenham para la circunferencia

#Algoritmo de Bresenham para la circunferencia
def CircunfPtoMedio((x0,y0),r, pantalla):
    x=0
    y=r
    p=1-r
    res=[]
    #pygame.draw.line(pantalla, blanco, (x0,y0), (x,y), 1 )
    plotpoint((x0,y0),(x,y),pantalla,res)
    while(x<y):
        x=x+1
        if(p<0):
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*(x-y)+1
    plotpoint((x0,y0),(x,y),pantalla)
    return res
#fin Algoritmo de Bresenham para la circunferencia


#Carga los sonidos verificando la ruta
def load_sound(nombre_s,dir_son):
    ruta = os.path.join(dir_son+"/sounds", nombre_s)
    try:
        sound = pygame.mixer.Sound(ruta)
    except:
        print "Error, no se puede cargar el sonido, verifique el formato: ", ruta
        sys.exit(1)
    return sound

#Funcion para verificar que las imagenes se cargan correctamente
def load_image(nombre_a, dir_img, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_img+"/images", nombre_a)
    try:
        image = pygame.image.load(ruta)
    except:
        print "Error, no se puede cargar la imagen: ", ruta
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


class Enemigo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.rect = self.image.get_rect()
        self.direccion=0
    def update(self):
        if(self.rect.x >= (ANCHO-self.rect[2])):
            self.direccion=1
        if(self.rect.x <= (self.rect[2])):
            self.direccion=0
        if (self.direccion == 0):
            self.rect.x+=5
        else:
            self.rect.x-=5

class Bala(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.rect = self.image.get_rect()
        self.velocidad=5
    def update(self):
        self.rect.x+=self.velocidad


class Jugador(pygame.sprite.Sprite):

    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.rect = self.image.get_rect()
        self.vida = 100
        self.score=0
    def chocar(self):
        self.vida-=10

def menu(waves,dif,ANCHO,ALTO):
    pygame.init()
    tipo = pygame.font.SysFont("monospace", 13)
    menu_d=pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
    backgroundm=load_image('backgroundm.jpg',curdir,alpha=False)
    ad1 = tipo.render(("Presiona +/- para manejar las oleadas por nivel" + " Oleadas: " + str(waves)),1, blanco)
    ad2 = tipo.render(("Presiona d/r para manejar la dificultad" + " Dificultad: " + str(dif)),1, blanco)
    ad3 = tipo.render("Escape para salir",1, blanco)
    s_fondo=load_sound('fondo1.sf',curdir)
    s_fondo.play()
    menu_d.blit(backgroundm,(0,0))
    menu_d.blit(ad1, (ANCHO/2-ANCHO/4, ALTO/2))
    menu_d.blit(ad2, (ANCHO/2-ANCHO/4, (ALTO/2)+30))
    menu_d.blit(ad3, (ANCHO/2-ANCHO/4, (ALTO/2)+60))

    pygame.display.flip()

    terminar=False
    max_waves=False
    min_waves=False
    while(not terminar):
        ad1 = tipo.render(("Presiona +/- para manejar las oleadas por nivel" + " Oleadas: " + str(waves)),1, blanco)
        ad2 = tipo.render(("Presiona d/r para manejar la dificultad" + " Dificultad: " + str(dif)),1, blanco)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.K_SPACE or event.type == pygame.QUIT:
                terminar=True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS:
                    if(not waves>=10):
                        waves+=1
                if event.key == pygame.K_KP_MINUS:
                    if(not waves<=5):
                        waves-=1
                if event.key == pygame.K_d:
                    if(not dif>=3):
                        dif+=1
                if event.key == pygame.K_r:
                    if(not dif <= 1):
                        dif-=1
                if event.key == pygame.K_ESCAPE:
                    terminar=True


        menu_d.blit(backgroundm,(0,0))
        menu_d.blit(ad1, (ANCHO/2-ANCHO/4, ALTO/2))
        menu_d.blit(ad2, (ANCHO/2-ANCHO/4, (ALTO/2)+30))
        menu_d.blit(ad3, (ANCHO/2-ANCHO/4, (ALTO/2)+60))
        pygame.display.flip()


    return waves,dif

def main():
    ANCHO = 800
    ALTO = 600
    waves=5
    dificultad=1
    waves,dificultad = menu(waves,dificultad,ANCHO,ALTO)

    #Inicializacion de pantalla
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Magician-zombie v0.1 - Level 1 ", 'Spine Runtime')
    pantalla.fill(blanco)
    #Fin de inicializacion de pantalla




if __name__ == "__main__":
    main()
