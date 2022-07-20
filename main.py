import sys, pygame, os

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
            if not disparo and evento_sistema["button"] == 1 and componentes[0] >= 100-30 and componentes[0] <= 100+30 and componentes[1] >= 100-30 and componentes[1] <= 100+30:
                disparo = True
                contador +=1
    
    screen.fill(black)
    
    if not disparo:
        pygame.draw.circle(screen, (0, 0, 255), (100,100), 30)
    else:
        font1 = pygame.font.Font(None, 64)
        text1 = font1.render("Ganaste el juego", True, (10, 10, 10))
        textpos1 = text1.get_rect(centerx=screen.get_width() / 2, y=350)
        print("Gano")
        screen.blit(text1, textpos1)
    
    screen.blit(ball, ballrect)

    font = pygame.font.Font(None, 64)
    text = font.render("Tiros: "+ str(contador), True, (10, 10, 10))
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
    screen.blit(text, textpos)


    pygame.display.flip()
