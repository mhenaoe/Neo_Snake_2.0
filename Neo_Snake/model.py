import pygame
import sys

TAMANO_CELDA = 30
ANCHO, ALTO = 600, 600
FPS = 10

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

        if not (0 <= x < ancho_celdas and 0 <= y <alto_celdas):
            return True

        if self.cabeza.posicion in self.cuerpo.segmentos:
            return True

        if self.cabeza.posicion in self.cuerpo.segmentos:
            return True

        if self.cabeza.posicion in obstaculos:
            return True

        return False

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Neo-Snake - Básico")
clock = pygame.time.Clock()

serpiente = Serpiente()

corriendo = True

while corriendo:
    clock.tick(FPS)
    pantalla.fill((0, 0, 0))

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
        (255, 255, 0),
        pygame.Rect(x * TAMANO_CELDA, y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
    )

    for x, y in serpiente.cuerpo.segmentos:
        pygame.draw.rect(
            pantalla,
            (0, 255, 0),
            pygame.Rect(x * TAMANO_CELDA, y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
        )

    pygame.display.flip()

pygame.quit()
sys.exit()