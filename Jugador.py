import pygame

import Constantes
from ObjetoEscenario import ObjetoEscenario


class Jugador(ObjetoEscenario):
    def __init__(self, pos_x, pos_y, color, medida_x, medida_y, velocidad=10):
        super().__init__(pos_x, pos_y, medida_x, medida_y, color)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.medida_x = medida_x
        self.medida_y = medida_y
        self.velocidad = velocidad
        self.puntuacion = 0

    def movimiento_arriba(self, tecla_presionada, jugador, arriba_tecla):
        if tecla_presionada[arriba_tecla] and jugador.pos_y > Constantes.ZONA_JUEGO[1]:
            jugador.pos_y -= jugador.velocidad

    def movimiento_abajo(self, tecla_presionada, jugador, abajo_tecla):
        if tecla_presionada[abajo_tecla] and jugador.pos_y + jugador.medida_y < Constantes.ZONA_JUEGO[3] + 15:
            jugador.pos_y += jugador.velocidad

    def Pintar(self, finestraJoc):
        super().Pintar(finestraJoc)

    def sumar_puntucacion(self):
        self.puntuacion = self.puntuacion + 1
