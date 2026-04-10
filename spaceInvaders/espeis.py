import pygame
import random
import os

carpeta_script = os.path.dirname(os.path.abspath(__file__))
os.chdir(carpeta_script)

pygame.init()

ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("ESPEIS INVAIDIERS 👽")

BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)

clock = pygame.time.Clock()

# cargar las imagenes del videojuego
fondo_img = pygame.image.load("fondo.png")
nave_img = pygame.image.load("nave.png")
alien_img = pygame.image.load("alien.png")

# Reescalar las imagenes del videojuego
nave_img = pygame.transform.scale(nave_img, (64, 64))
alien_img = pygame.transform.scale(alien_img, (64, 64))
fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))

#obtener medida del alien para poder disparar
jugador_ancho, jugador_alto = nave_img.get_rect().size
enemigo_ancho, enemigo_alto = alien_img.get_rect().size

#configurar al usuario (nave)
jugador_x = (ANCHO / 2) - (jugador_ancho / 2)
jugador_y = ALTO - jugador_alto - 20
jugador_velocidad = 5

#configurar disparo
bala_ancho, bala_alto = 10, 20
bala_velocidad = 10
bala_activa = False
bala_x = 0
bala_y = 0

#configurar enemigo
num_enemigos = 5
enemigos = []
enemigo_velocidad = 2
for i in range(num_enemigos):
    enemigo_x = random.randint(0, ANCHO - enemigo_ancho)
    enemigo_y = random.randint(50, 200)
    enemigo_velocidad_x = 2
    enemigos.append([enemigo_x, enemigo_y, enemigo_velocidad_x])

def dibujar_jugador(x, y):
    VENTANA.blit(nave_img, (x, y))

def dibujar_bala(x, y):
    pygame.draw.rect(VENTANA, VERDE, (x, y, bala_ancho, bala_alto))

def dibujar_enemigo(x, y):
    VENTANA.blit(alien_img, (x, y))

def hay_colision(rect1, rect2):
    return rect1.colliderect(rect2)

#bucle_principal
jugando = True
puntaje = 0
fuente = pygame.font.SysFont(None, 30)
while jugando:
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
    #teclas del juego
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_x -= jugador_velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += jugador_velocidad
    if not bala_activa:
        bala_activa = True
        bala_x = jugador_x + (jugador_ancho / 2) - (bala_ancho / 2)
        bala_y = jugador_y
    if jugador_x < 0:
        jugador_x = 0
    if jugador_x > ANCHO - jugador_ancho:
        jugador_x = ANCHO - jugador_ancho
    
    #movimiento de la bala
    if bala_activa:
        bala_y -= bala_velocidad
        if bala_y + bala_alto < 0:
            bala_activa = False

    #movimiento de los enemigos
    for enemigo in enemigos:
        enemigo[0] += enemigo[2]
        if enemigo[0] <= 0 or enemigo[0] >= ANCHO - enemigo_ancho:
            enemigo[2] =- enemigo[2]
            enemigo[1] += 20
        
        jugador_rect = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)
        enemigo_rect = pygame.Rect(enemigo[0], enemigo[1], enemigo_ancho, enemigo_alto)
        
        if bala_activa:
            bala_rect = pygame.Rect(bala_x, bala_y, bala_ancho, bala_alto)
            if hay_colision(bala_rect, enemigo_rect):
                bala_activa = False
                enemigo[0] = random.randint(0, ANCHO - enemigo_ancho)
                enemigo[1] = random.randint(50, 200)
                puntaje += 1

    #dibujar
    VENTANA.blit(fondo_img, (0, 0))
    dibujar_jugador(jugador_x, jugador_y)
    if bala_activa:
        dibujar_bala(bala_x, bala_y)
    for enemigo in enemigos:
        dibujar_enemigo(enemigo[0], enemigo[1])
    puntaje_texto = fuente.render("Puntaje: " + str(puntaje), True, BLANCO)
    VENTANA.blit(puntaje_texto, (10, 10))
    pygame.display.flip()