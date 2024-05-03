import random
import sys

import pygame

import Constantes
from Jugador import Jugador
from Pelota import Pelota

pygame.init()

finestraJoc = pygame.display.set_mode(Constantes.TAMANO_VENTANA)

rellotge = pygame.time.Clock()

gameOver = False
inicio_lado = 1

posicion_vertical_central = (Constantes.TAMANO_VENTANA[1] - Constantes.MEDIDA_Y) // 2
posicion_horizontal_central = (Constantes.TAMANO_VENTANA[0] - Constantes.TAMANO_PELOTA) // 2
posicion_vertical_central_pelota = (Constantes.TAMANO_VENTANA[1] - Constantes.TAMANO_PELOTA) // 2

jugador1 = Jugador(pos_x=Constantes.POSICION_JUG_1_X, pos_y=posicion_vertical_central, color=Constantes.COLOR_JUG_1,
                   medida_x=Constantes.MEDIDA_X, medida_y=Constantes.MEDIDA_Y)
jugador2 = Jugador(pos_x=Constantes.POSICION_JUG_2_X, pos_y=posicion_vertical_central, color=Constantes.COLOR_JUG_2,
                   medida_x=Constantes.MEDIDA_X, medida_y=Constantes.MEDIDA_Y)

pelota = Pelota(posicion_x=posicion_horizontal_central - 5, posicion_y=posicion_vertical_central_pelota, velocitad_x=5,
                velocitad_y=5, color=Constantes.COLOR_PELOTA)
numero_entero = random.randint(1, 4)

if numero_entero == 1:
    pelota.velocitad_x *= 1
    pelota.velocitad_y *= 1
elif numero_entero == 2:
    pelota.velocitad_x *= -1
    pelota.velocitad_y *= 1
elif numero_entero == 3:
    pelota.velocitad_x *= 1
    pelota.velocitad_y *= -1
else:
    pelota.velocitad_x *= -1
    pelota.velocitad_y *= -1


def PrintObjetos():
    finestraJoc.fill(Constantes.COLOR_BORDE)
    pygame.draw.rect(finestraJoc, Constantes.COLOR_TABLERO, Constantes.ZONA_JUEGO)

    jugador1.Pintar(finestraJoc)
    jugador2.Pintar(finestraJoc)
    pelota.Pintar(finestraJoc)


def DetectarEventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


while not gameOver:
    PrintObjetos()

    DetectarEventos()

    # Control de los frames
    rellotge.tick(Constantes.RELOJ)
    pygame.display.update()

    tecla_presionada = pygame.key.get_pressed()

    # Llamada para mover jugador 1 (teclas "w" y "s")
    jugador1.movimiento_arriba(tecla_presionada, jugador1, pygame.K_w)
    jugador1.movimiento_abajo(tecla_presionada, jugador1, pygame.K_s)

    # Llamada para mover jugador 2 (flechas arriba y abajo)
    jugador2.movimiento_arriba(tecla_presionada, jugador2, pygame.K_UP)
    jugador2.movimiento_abajo(tecla_presionada, jugador2, pygame.K_DOWN)

    pelota.Reaccion_pelota(jugador1, jugador2, posicion_horizontal_central, posicion_vertical_central_pelota)

