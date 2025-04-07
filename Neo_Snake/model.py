import pygame
import random

pygame.init()

ANCHO_TABLERO = 600
ALTO_TABLERO= 600
TAM_CELDA = 30
ANCHO_CELDAS = ANCHO_TABLERO // TAM_CELDA
ALTO_CELDAS = ANCHO_TABLERO // TAM_CELDA

tablero = pygame.display.set_mode((ANCHO_TABLERO, ALTO_TABLERO))
pygame.display.set_mode("Neo_Snake")

Verde = (0, 128, 0)
Morado = (128, 0, 128)

class Alimentos:
    def __init__(self, tipo: str, ancho_tablero: int, alto_tablero: int, color: int):
        self.tipo = tipo
        self.ancho_tabelro = ancho_tablero
        self.alto_tablero = alto_tablero
        self.color = color
        self.nueva_posicion()