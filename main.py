import sys

import pygame

import Constantes
from Jugador import Jugador

pygame.init()

finestraJoc = pygame.display.set_mode(Constantes.TAMANO_VENTANA)

rellotge = pygame.time.Clock()

gameOver = False

posicion_vertical_central = (Constantes.TAMANO_VENTANA[1] - Constantes.MEDIDA_Y) // 2

jugador1 = Jugador(pos_x=Constantes.POSICION_JUG_1_X, pos_y=posicion_vertical_central, color=Constantes.COLOR_JUG_1,
                   medida_x=Constantes.MEDIDA_X, medida_y=Constantes.MEDIDA_Y)
jugador2 = Jugador(pos_x=Constantes.POSICION_JUG_2_X, pos_y=posicion_vertical_central, color=Constantes.COLOR_JUG_2,
                   medida_x=Constantes.MEDIDA_X, medida_y=Constantes.MEDIDA_Y)


def PrintObjetos():
    finestraJoc.fill(Constantes.COLOR_BORDE)
    pygame.draw.rect(finestraJoc, Constantes.COLOR_TABLERO, Constantes.ZONA_JUEGO)
    pygame.draw.rect(finestraJoc, jugador1.color, (jugador1.pos_x, jugador2.pos_y, jugador1.medida_x, jugador1.medida_y))
    pygame.draw.rect(finestraJoc, jugador2.color, (jugador2.pos_x, jugador2.pos_y, jugador2.medida_x, jugador2.medida_y))


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
