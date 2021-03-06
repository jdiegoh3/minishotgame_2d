from func import *
from loser import game_over
from winner import *

def level2(ANCHO,ALTO, vidalifemago, level = 2):

    aux_oleada = 1 #para que sepa que oleada va a mandar
    contador_vida = 0 #Para saber cuando mandar vidas

    #Inicializacion de pantalla
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO+50))#, pygame.FULLSCREEN)
    pygame.display.set_caption("Magician-zombie v0.1 - Level 2 ", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 15)
    pantalla_s=load_sound('background.ogg',curdir)
    shot_s=load_sound('shot.wav',curdir)
    pantalla.fill((0,0,0))
    #Fin de inicializacion de pantalla

    #Cargando imagenes
    posinif = [0,0]

    #Grupos de sprites
    ls_todos = pygame.sprite.Group()
    ls_balaj = pygame.sprite.Group()
    ls_enemigos = pygame.sprite.Group()
    ls_balase = pygame.sprite.Group()
    ls_jugadores = pygame.sprite.Group()
    ls_vidas = pygame.sprite.Group()
    ls_boss = pygame.sprite.Group()
    ls_balae = pygame.sprite.Group()
    #Creamos los personajes

    #-----------------magician------------------------------------------------
    magician = Magician('dere_1.png',[0,0], ANCHO, ALTO)
    bottom = [(ANCHO / 2) - (magician.getRect()[2] / 2), ALTO - (magician.getRect()[3] / 2 + 50)]
    magician.setPos(bottom) #posiciona el magician en la mitad de la pantalla

    #Agrega las imagenes del magician
    magician.imaged.append(load_image('dere_1.png',curdir,alpha=True))
    magician.imaged.append(load_image('dere_2.png',curdir,alpha=True))
    magician.imagenar.append(load_image('up_1.png',curdir,alpha=True))
    magician.imagenar.append(load_image('up_2.png',curdir,alpha=True))
    magician.imagei.append(load_image('iz_1.png',curdir,alpha=True))
    magician.imagei.append(load_image('iz_2.png',curdir,alpha=True))
    magician.imagena.append(load_image('ab_1.png',curdir,alpha=True))
    magician.imagena.append(load_image('ab_2.png',curdir,alpha=True))
    magician.setLife(vidalifemago)
    ls_todos.add(magician)
    ls_jugadores.add(magician)

    #------------------BOSS-------------------------------------
    #Creamos el jefe 26 x 33 or 32 x 48
    table=0
    boss = Boss('boss_ini.png',[0,0],ANCHO, ALTO - 50)
    up = [(ANCHO / 2) - (boss.getRect()[2] / 2), 0]
    boss.setPos(up)
    ls_todos.add(boss)
    ls_boss.add(boss)
    boss_s=load_sound('boss.wav',curdir)

    #------------------------PANTALLA--------------------------
    fondo = load_image('fondo2.jpg',curdir, alpha=False)
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO+10))
    pantalla.fill(negro)
    ambiente_s=load_sound('ambiente.ogg',curdir)
    ambiente_s.play()
    pantalla.blit(fondo,posinif)
    splash = False
    ls_todos.draw(pantalla)
    ls_enemigos.draw(pantalla)
    ls_boss.draw(pantalla)

    pygame.mouse.set_visible(False) #Oculta el puntero del mouse
    pygame.display.flip()
    reloj = pygame.time.Clock()
    terminar = False
    disparo = False
    player_current = 0
    flag = False
    cont = 0

    #Variables del reloj
    con_cuadros=0
    tasa_cambio=60
    tiempo_ini=10
    seflim=0

    #--------------------APARICION INICIAL DEL BOSS---------------
    boss_s.play()



    cont_balas = 60
    terminar = False
    middle = [(ANCHO / 2) - (boss.getRect()[2] / 2), (ALTO / 2) - (boss.getRect()[3] / 2)]
    boss.restartMovements(middle)#se va hasta la mitad de la pantalla
    while(not terminar):

        pantalla.blit(fondo,[0,0])
        ls_todos.draw(pantalla)
        ls_boss.draw(pantalla)
        ls_todos.update()
        pygame.display.flip()
        reloj.tick(60)#Era 60

        if(boss.getPos() == middle):
            reloj.tick(0.3)
            terminar = True #se sale de este ciclo cuando llegue a la mitad


    bala_boss = CircleBullet('bala_b.png',boss.getPos(), boss.getMargen()[0] + boss.getMargen()[0]/2,ANCHO,ALTO)
    ls_balae.add(bala_boss)
    ls_todos.add(bala_boss)

    bala_boss.restartMovements(boss.getPos())


    for i in range (0, len(bala_boss.moves)):
        #bala_boss.update()
        pantalla.blit(fondo,[0,0])
        ls_todos.draw(pantalla)
        ls_boss.draw(pantalla)
        ls_balae.draw(pantalla)
        ls_todos.update()
        pygame.display.flip()
        reloj.tick(100)


    terminar = False
    bala_boss2 = RectBullet('bala_b.png',boss.getPos())
    bala_boss2.restartMovements(magician.getPos())

    ls_balae.add(bala_boss2)
    ls_todos.add(bala_boss2)
    ls_balae.remove(bala_boss)
    ls_todos.remove(bala_boss)

    for i in range (0, len(bala_boss2.moves)):

        pantalla.blit(fondo,[0,0])
        ls_todos.draw(pantalla)
        ls_boss.draw(pantalla)
        ls_balae.draw(pantalla)
        ls_todos.update()
        pygame.display.flip()
        reloj.tick(60)

    risa_s=load_sound('lau.ogg',curdir)
    impact_s=load_sound('impact.flac',curdir)

    impact_s.play()



    ls_balae.remove(bala_boss2)
    ls_todos.remove(bala_boss2)

    ls_balae.remove(bala_boss)
    ls_todos.remove(bala_boss)
    pantalla.blit(fondo,[0,0])
    pygame.display.flip()


    terminar = False
    up = [(ANCHO / 2) - (boss.getRect()[2] / 2), -1*boss.getRect()[3]]
    boss.restartMovements(up)#se va hasta la mitad de la pantalla


    while(not terminar): #se va

        pantalla.blit(fondo,[0,0])
        ls_todos.draw(pantalla)
        ls_boss.draw(pantalla)
        ls_todos.update()
        pygame.display.flip()
        reloj.tick(60)

        if(boss.getPos()[1]<= 100):
            risa_s.play()
        if(boss.getPos() == up):
            terminar = True
            ls_todos.remove(bala_boss)
            reloj.tick(0.3)



    boss_s.stop()
    magician.setLife(magician.getLife()-30)#porque el boss le pego


    terminar = False
    pantalla_s.play()
    flag = False
    flagoleada=True
    ls_todos.remove(boss)
    boss.restartMovements(magician.getPos())

    while(not terminar):

        if(magician.getLife() <= 0): #vuelve al menu ppal
          ls_todos.draw(pantalla)
          pygame.display.flip()
          magician.image = load_image("muerte.png", curdir, alpha=True)
          ls_todos.draw(pantalla)
          pygame.display.flip()
          pantalla_s.stop()
          reloj.tick(0.3)
          game_over(ANCHO,ALTO)
          terminar=True
          return 3 #level3

        if((len(ls_enemigos) == 0 ) and flag and not terminar):
          flagoleada=False
          pantalla_s.stop()
          reloj.tick(0.6)
          level+=1
          terminar=True
          winner(ANCHO,ALTO)


        """if(boss.getLife() <= 0):
            pantalla_s.stop()
            reloj.tick(0.6)
            level+=1
            terminar=True
            winner(ANCHO,ALTO)"""

        #----------------ENEMIGOS-------------------------
        if(flagoleada):
            if(len(ls_enemigos) == 0): #si ya los mato a todos
              tipo2 = pygame.font.SysFont("comicsansms", 50)
              texto_oleada = tipo2.render("READY? ",1, (255,255,255))
              pantalla.blit(texto_oleada,(ANCHO/2 - 100,ALTO/2 - 30))
              pygame.display.flip()
              reloj.tick(0.5)
              pantalla.blit(fondo,[0,0])
              texto_oleada = tipo2.render("GO! ",1, (255,255,255))
              pantalla.blit(texto_oleada,(ANCHO/2 - 100,ALTO/2 - 30))
              pygame.display.flip()
              reloj.tick(0.5)
              oleadas(aux_oleada,ANCHO, ALTO, ls_enemigos, ls_todos,magician,level)
              contador_vida = 0
              flag = True

        events = pygame.event.get()
        #print "cont : " , contador_vida
        if(magician.getLife() < 35 and contador_vida >= 300):#si se va a morir, debe coger una vida
          anciano = OldMan('viejo_vida.png',[0,0],ANCHO, ALTO)
          anciano.setPos([random.randrange(ANCHO - anciano.getRect()[2]),random.randrange(ALTO - 50 - anciano.getRect()[3])])
          ls_todos.add(anciano)
          ls_vidas.add(anciano)
          contador_vida = 0

        total_segundos=con_cuadros // tasa_cambio
        minutos= total_segundos // 60
        segundos = total_segundos % 60
        tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos,segundos)
        if total_segundos >60:
          total_segundos=0

        reloj2=tipo.render(tiempo_final, True, blanco)
        tipo = pygame.font.SysFont("monospace", 15)
        blood = tipo.render("Vida actual: " ,1, (255,0,0))
        pantalla.blit(blood, (0, ALTO))
        point = tipo.render(("Puntos: " + str(magician.getScore())),1, (0,0,0))

        if(magician.getLife() > 0):
          point = tipo.render(("Puntos: " + str(magician.getScore())),1, (255,0,0))

        pantalla.fill(pygame.Color(0,0,0))

        keys = pygame.key.get_pressed()

        for event in events:

            if event.type  == pygame.QUIT:
              pantalla_s.stop()
              terminar = True
              level=3

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    bala = Bullet('bala.png',magician.getPos())#la posicion inicial depende de objeto que este disparando
                    dir = magician.getDir()
                    bala.setDir(dir)
                    shot_s.play()
                    if(dir == 0):#derecha
                        bala.setPos([magician.getPos()[0] + magician.getRect()[2]/2,magician.getPos()[1]])
                    if(dir == 1):#izquierda
                        bala.setPos([magician.getPos()[0] - magician.getRect()[2]/2,magician.getPos()[1]])
                    if(dir == 2):#arriba
                        bala.setPos([magician.getPos()[0],magician.getPos()[1] - magician.getRect()[3]])
                    if(dir == 3):#abajo
                        bala.setPos([magician.getPos()[0],magician.getPos()[1] + magician.getRect()[3]])

                    ls_balaj.add(bala)
                    ls_todos.add(bala)
                    disparo = True

                if event.key == pygame.K_ESCAPE:
                    pantalla_s.stop()
                    terminar=True
                    level=3



        if keys[pygame.K_a]:
            player_current = (player_current+1)%len(magician.imagei)
            magician.image = magician.imagei[player_current]
            magician.moveLeft()
            magician.setDir(1)

            for e in ls_enemigos:
              e.restartMovements(magician.getPos())

        if keys[pygame.K_w]:
            player_current = (player_current+1)%len(magician.imagenar)
            magician.image = magician.imagenar[player_current]
            magician.moveUp()
            magician.setDir(2)

            for e in ls_enemigos:
                e.restartMovements(magician.getPos())

        if keys[pygame.K_d]:
            player_current = (player_current+1)%len(magician.imaged)
            magician.image = magician.imaged[player_current]
            magician.moveRight()
            magician.setDir(0)

            for e in ls_enemigos:
                e.restartMovements(magician.getPos())

        if keys[pygame.K_s]:
            player_current = (player_current+1)%len(magician.imagena)
            magician.image = magician.imagena[player_current]
            magician.moveDown()
            magician.setDir(3)

            for e in ls_enemigos:
                e.restartMovements(magician.getPos())

            for b in ls_boss:
                b.restartMovements(magician.getPos())
            boss.restartMovements(magician.getPos())


        magician.enemigos=len(ls_enemigos)

        for enemigo in ls_enemigos:
            if(checkCollision(magician,enemigo)): # si se choco
                if(cont == 0):
                    magician.crash()
                    lifebars(magician,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida
                    flag = True

        if(flag):
            cont+=1
        if(cont >= 8):
            cont=0

        #lista de balas
        for b in ls_balaj:
            for enemigo in ls_enemigos:
                if(checkCollision(b,enemigo)):
                    enemigo.setLife(enemigo.getLife()-random.randrange(15))
                    ls_balaj.remove(b)
                    ls_todos.remove(b)
                    magician.setScore(5)

        for b in ls_balaj:
            for bossesito in ls_boss:
                if(checkCollision(b,bossesito)):
                    bossesito.setLife(bossesito.getLife()-random.randrange(15))
                    ls_balaj.remove(b)
                    ls_todos.remove(b)
                    impact_s.play()
                    magician.setScore(15)



        for enemigo in ls_enemigos:
            enemigo.jugador = magician.getPos()
            if(enemigo.getLife() <= 0):
                ls_enemigos.remove(enemigo)
                ls_todos.remove(enemigo)

        magician.mov=0

        for v in ls_vidas:
            ls_vidas_i = pygame.sprite.spritecollide(magician, ls_vidas, True)
            for vida in ls_vidas_i:
                ls_vidas.remove(vida)
                ls_todos.remove(vida)
                magician.setLife(magician.getLife()+10)
                lifebars(magician,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida



        pantalla.blit(fondo,[0,0])
        pantalla.blit(blood,[0,ALTO+15])
        pantalla.blit(point,[300,ALTO+15]) #+ 15])
        pantalla.blit(reloj2, [500,ALTO+15])
        lifebars(magician,pantalla,[120,ALTO+18])
        ls_todos.draw(pantalla)
        ls_boss.draw(pantalla)
        ls_enemigos.draw(pantalla)
        ls_todos.update()

        pygame.display.flip()

        con_cuadros+=1
        reloj.tick(tasa_cambio)
        contador_vida += 1

    return level
