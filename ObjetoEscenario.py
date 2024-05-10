import pygame


class ObjetoEscenario:
    def __init__(self, pos_x, pos_y,medida_x,medida_y, color):
        self.medida_y = medida_y
        self.medida_x = medida_x
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def Pintar(self, finestraJoc):
        pygame.draw.rect(finestraJoc, self.color,
                         (self.pos_x, self.pos_y, self.medida_x, self.medida_y))

    def Pintar_pelota(self, finestraJoc):
        pass