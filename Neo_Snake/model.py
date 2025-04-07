import pygame
import random
import sys

pygame.init()

TAM_CELDA = 30
ANCHO, ALTO = 600, 600
ANCHO_CELDAS = ANCHO // TAM_CELDA
ALTO_CELDAS = ALTO // TAM_CELDA
FPS = 10

NEGRO = (0, 0, 0)
VERDE = (0, 128, 0)
MORADO = (128, 0, 128)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)

class Alimentos:
    def __init__(self, tipo: str, ancho_tablero: int, alto_tablero: int, color):
        self.tipo = tipo
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.color = color
        self.nueva_posicion()

    def nueva_posicion(self):
        self.x = random.randint(0, self.ancho_tablero - 1)
        self.y = random.randint(0, self.alto_tablero - 1)

    def dibujar(self, superficie):
        rect = pygame.Rect(self.x * TAM_CELDA, self.y * TAM_CELDA, TAM_CELDA, TAM_CELDA)
        pygame.draw.rect(superficie, self.color, rect)

class Pera(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int):
        super().__init__("Pera", ancho_tablero, alto_tablero, VERDE)

class Ciruela(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int):
        super().__init__("Ciruela", ancho_tablero, alto_tablero, MORADO)

class Cabeza:
    def __init__(self, x, y):
        self.posicion = (x, y)
        self.direccion = "DERECHA"

    def mover(self):
        x, y = self.posicion
        if self.direccion == "ARRIBA":
            y -= 1
        elif self.direccion == "ABAJO":
            y += 1
        elif self.direccion == "IZQUIERDA":
            x -= 1
        elif self.direccion == "DERECHA":
            x += 1
        self.posicion = (x, y)

    def cambiar_direccion(self, nueva_direccion):
        opuestos = {"ARRIBA": "ABAJO", "ABAJO": "ARRIBA", "IZQUIERDA": "DERECHA", "DERECHA": "IZQUIERDA"}
        if nueva_direccion != opuestos.get(self.direccion, None):
            self.direccion = nueva_direccion

class Cuerpo:
    def __init__(self):
        self.segmentos = []

    def mover(self, nueva_posicion):
        self.segmentos.insert(0, nueva_posicion)
        if len(self.segmentos) > 1:
            self.segmentos.pop()

    def crecer(self):
        if self.segmentos:
            self.segmentos.append(self.segmentos[-1])

class Cola:
    def __init__(self):
        self.posicion = None

    def actualizar(self, nueva_posicion):
        self.posicion = nueva_posicion

class Serpiente:
    def __init__(self):
        self.cabeza = Cabeza(5, 5)
        self.cuerpo = Cuerpo()
        self.cola = Cola()
        self.longitud = 1

    def mover(self):
        pos_anterior = self.cabeza.posicion
        self.cabeza.mover()
        self.cuerpo.mover(pos_anterior)
        if len(self.cuerpo.segmentos) == self.longitud - 1 and self.cuerpo.segmentos:
            self.cola.actualizar(self.cuerpo.segmentos[-1])

    def cambiar_direccion(self, nueva_direccion):
        self.cabeza.cambiar_direccion(nueva_direccion)

    def crecer(self):
        self.longitud += 1
        self.cuerpo.crecer()

    def obtener_posiciones(self):
        return [self.cabeza.posicion] + self.cuerpo.segmentos

    def colisionar(self, ancho_celdas, alto_celdas, obstaculos=None):
        if obstaculos is None:
            obstaculos = []

        x, y = self.cabeza.posicion

        if not (0 <= x < ancho_celdas and 0 <= y < alto_celdas):
            return True

        if self.cabeza.posicion in self.cuerpo.segmentos:
            return True

        if self.cabeza.posicion in obstaculos:
            return True

        return False

class Obstaculo:
    def __init__(self, ancho_tablero, alto_tablero, tam_celda):
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.tam_celda = tam_celda
        self.x = random.randint(0, ancho_tablero - 1)
        self.y = random.randint(0, alto_tablero - 1)
        self.color = BLANCO

    def dibujar(self, superficie):
        rect = pygame.Rect(
            self.x * self.tam_celda, self.y * self.tam_celda,
            self.tam_celda, self.tam_celda
        )
        pygame.draw.rect(superficie, self.color, rect)

obstaculos = []
for _ in range(5):
    obstaculo = Obstaculo(ANCHO_CELDAS, ALTO_CELDAS, TAM_CELDA)
    obstaculos.append(obstaculo)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Neo-Snake con Frutas")
clock = pygame.time.Clock()

serpiente = Serpiente()
pera = Pera(ANCHO_CELDAS, ALTO_CELDAS)
ciruela = Ciruela(ANCHO_CELDAS, ALTO_CELDAS)

corriendo = True

while corriendo:
    clock.tick(FPS)
    pantalla.fill(NEGRO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                serpiente.cambiar_direccion("ARRIBA")
            elif evento.key == pygame.K_DOWN:
                serpiente.cambiar_direccion("ABAJO")
            elif evento.key == pygame.K_LEFT:
                serpiente.cambiar_direccion("IZQUIERDA")
            elif evento.key == pygame.K_RIGHT:
                serpiente.cambiar_direccion("DERECHA")

    serpiente.mover()

    x, y = serpiente.cabeza.posicion
    pygame.draw.rect(
        pantalla,
        AMARILLO,
        pygame.Rect(x * TAM_CELDA, y * TAM_CELDA, TAM_CELDA, TAM_CELDA)
    )

    for x, y in serpiente.cuerpo.segmentos:
        pygame.draw.rect(
            pantalla,
            VERDE,
            pygame.Rect(x * TAM_CELDA, y * TAM_CELDA, TAM_CELDA, TAM_CELDA)
        )

    for obstaculo in obstaculos:
        obstaculo.dibujar(pantalla)

    pera.dibujar(pantalla)
    ciruela.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()
sys.exit()
