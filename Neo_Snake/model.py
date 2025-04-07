import pygame
import random

pygame.init()

ANCHO_TABLERO = 600
ALTO_TABLERO= 600
TAM_CELDA = 30
ANCHO_CELDAS = ANCHO_TABLERO // TAM_CELDA
ALTO_CELDAS = ANCHO_TABLERO // TAM_CELDA

tablero = pygame.display.set_mode((ANCHO_TABLERO, ALTO_TABLERO))
pygame.display.set_mode(600, 600)

Verde = (0, 128, 0)
Morado = (128, 0, 128)

class Alimentos:
    def __init__(self, tipo: str, ancho_tablero: int, alto_tablero: int, color: int):
        self.tipo = tipo
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.color = color
        self.nueva_posicion()
    def nueva_posicion(self):
        self.x = random.randint(0, self.ancho_tabelro - 1)
        self.y = random.randint(0, self.alto_tablero - 1)
    def dibujar(self, tablero: int):
        rect = pygame.Rect(self.x * TAM_CELDA, self.y * TAM_CELDA, TAM_CELDA, TAM_CELDA)
        pygame.draw.rect(tablero, self.color, rect)

class Pera(Alimentos):
        def __init__(self, ancho_tablero: int, alto_tablero: int):
            super().__init__("Pera", ancho_tablero, alto_tablero, Verde)

class Ciruela(Alimentos):
        def __init__(self, ancho_tablero: int, alto_tablero: int):
            super().__init__("Ciruela", ancho_tablero, alto_tablero, Morado)

Pera = Pera(ANCHO_CELDAS, ALTO_CELDAS)
Ciruela = Ciruela(ANCHO_CELDAS, ALTO_CELDAS)

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

pygame.quit()