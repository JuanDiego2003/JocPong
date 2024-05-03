import pygame

import Constantes
from ObjetoEscenario import ObjetoEscenario


class Pelota(ObjetoEscenario):
    # Atributos estáticos
    velocidad = 5
    medida = 10

    def __init__(self, posicion_x, posicion_y, velocitad_x, velocitad_y, color):
        super().__init__(posicion_x, posicion_y, color)
        self.posicio_x = posicion_x
        self.posicio_y = posicion_y
        self.velocitad_x = velocitad_x
        self.velocitad_y = velocitad_y
        self.color = color

    def Pintar(self, finestraJoc):
        pygame.draw.rect(finestraJoc, self.color,
                         (self.posicio_x, self.posicio_y, self.medida, self.medida))

    def Reaccion_pelota(self, jugador1, jugador2, posicion_horizontal_central, posicion_vertical_central_self):

        # Mover la pelota
        self.posicio_x += self.velocitad_x
        self.posicio_y += self.velocitad_y

        # Detectar colisión con los bordes superior e inferior
        if (self.posicio_y <= Constantes.ZONA_JUEGO[1] or self.posicio_y + self.medida >=
                Constantes.ZONA_JUEGO[3]
                + 15):
            # Invertir la componente Y de la velocidad
            self.velocitad_y *= -1
        #
        if (self.posicio_x - self.velocitad_x < jugador1.pos_x + jugador1.medida_x and jugador1.pos_y <
                self.velocitad_y > jugador1.medida_y):
            self.posicio_x = jugador1.pos_x + jugador1.medida_x
        if (jugador1.pos_x <= self.posicio_x + self.medida / 2 <= jugador1.pos_x + jugador1.medida_x and
                jugador1.pos_y <= self.posicio_y + self.medida <= jugador1.pos_y +
                jugador1.medida_y):

            if jugador1.pos_y <= self.posicio_y + self.medida <= jugador1.pos_y + jugador1.medida_y:
                self.comprobar_positivo_negativo()
            else:
                self.comprobar_positivo_negativo()
        #
        if (self.posicio_x + self.velocitad_x + self.medida > jugador2.pos_x and jugador2.pos_y <
                self.velocitad_y > jugador2.medida_y):
            self.posicio_x = jugador2.pos_x
        if (jugador2.pos_x <= self.posicio_x + self.medida <= jugador2.pos_x + jugador2.medida_x and
                jugador2.pos_y <= self.posicio_y + self.medida <= jugador2.pos_y +
                jugador2.medida_y):

            if jugador2.pos_y <= self.posicio_y + self.medida <= jugador2.pos_y + jugador2.medida_y:
                self.comprobar_positivo_negativo()
            else:
                self.comprobar_positivo_negativo()

        # fuera de la zona de juego
        if self.posicio_x + self.medida >= Constantes.TAMANO_VENTANA[
            0] + 15 or self.posicio_x - self.medida <= -15:
            self.reset_Pelota(posicion_horizontal_central, posicion_vertical_central_self)

    def comprobar_positivo_negativo(self, ):
        if self.velocitad_x <= 15 or self.velocitad_x >= -15:
            if self.velocitad_x <= 0:
                self.velocitad_x -= 5
            else:
                self.velocitad_x += 5
        self.velocitad_x *= -1

    def reset_Pelota(self, posicion_horizontal_central, posicion_vertical_central_self):
        self.posicio_x = posicion_horizontal_central - 5
        self.posicio_y = posicion_vertical_central_self
        self.velocitad_x = 5
        self.velocitad_y = 5
