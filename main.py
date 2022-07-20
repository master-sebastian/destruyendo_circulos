import sys, pygame, os
from objetos.circulo import Circulo

pygame.init()

size = width, height = 800, 700
speed = [2, 2]
black = 255, 87, 51

screen = pygame.display.set_mode(size)

ball = pygame.image.load("img"+os.sep+"asistente-robot.png")
ball= pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
disparo = False
contador = 0
puntos = 12
listado_circulos = []
for i in range(puntos):
    listado_circulos.append(Circulo(screen, listado_circulos, 50, 50))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        evento_sistema = dict(event.dict)
        if('pos' in evento_sistema):
            componentes = evento_sistema["pos"]
            ballrect.x = componentes[0] - ball.get_rect().w/2
            ballrect.y = componentes[1] - ball.get_rect().h/2
        if ("button" in evento_sistema):
            componentes = evento_sistema["pos"]
            i = 0
            while i < len(listado_circulos):
                if not disparo and evento_sistema["button"] == 1 and listado_circulos[i].destruido(componentes[0], componentes[1]):
                    contador +=1
                i += 1
            for circulo in listado_circulos:
                nueva_posicion = circulo.generarmeEnPantalla()
                circulo.colorNuevo()
                circulo.x = nueva_posicion["x"]
                circulo.y = nueva_posicion["y"]
    

    screen.fill(black)
    
    if contador < 12:
        for circulo in listado_circulos:
            circulo.pintar()
    else:
        font1 = pygame.font.Font(None, 64)
        text1 = font1.render("Ganaste el juego", True, (10, 10, 10))
        textpos1 = text1.get_rect(centerx=screen.get_width() / 2, y=350)
        screen.blit(text1, textpos1)
    
    screen.blit(ball, ballrect)

    font = pygame.font.Font(None, 64)
    text = font.render("Puntos: "+ str(contador) +"/"+ str(puntos), True, (10, 10, 10))
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
    screen.blit(text, textpos)


    pygame.display.flip()
    