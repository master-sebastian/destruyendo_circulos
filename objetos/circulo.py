import random, pygame
class Circulo:
    def __init__(self, screen, controlador, width, height):
        self.x = None
        self.y = None
        self.screen = screen
        self.width = width
        self.height = height
        self.controlador = controlador
        posicion = self.generarmeEnPantalla()
        self.x = posicion["x"]
        self.y = posicion["y"]
        self.color = None
        self.colorNuevo()
    def colorNuevo(self):
        self.color = (random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1))
    def generarmeEnPantalla(self):
        w = self.screen.get_rect().w
        h = self.screen.get_rect().h
        return {
            "x": random.randrange(self.width/2, w - self.width/2, 1),
            "y": random.randrange(self.height/2, h - self.height/2, 1)
        }
    
    def pintar(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.width/2)

    def destruido(self, x, y):
        if (x >= self.x - self.width/2 and x <= self.x + self.width / 2 and y >= self.y-self.height/2 and y <= self.y+self.height/2):
            self.quitarmeDeLaLista()
            return True
        else:
            return False

    def quitarmeDeLaLista(self):
        i = 0
        encontrado = False
        while(i < len(self.controlador)):
            if(self.controlador[i] is self):
                encontrado = True
                break
            i += 1
        if encontrado:
            del self.controlador[i]