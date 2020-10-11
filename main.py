import pygame
import math
import time

pygame.init()

SCREENX = 1500
SCREENY = 750

FONT = pygame.font.SysFont('Arial', 32)

screen = pygame.display.set_mode((SCREENX, SCREENY))
screen.fill((255,255,255))
pygame.display.update()

running = True
CALC = True

def draw_axis(pos, screen):
    screen.fill((255,255,255))
    x, y = pos
    pygame.draw.line(screen, (0,0,0), (0, y), (SCREENX, y), 1)
    pygame.draw.line(screen, (0,0,0), (x, 0), (x, SCREENY), 1)
    pygame.display.update()

# def next_point(equation, known):
#     return known

# x0, y0 = (int(SCREENX/2), int(SCREENY/2))

# for x in range(x0, SCREENX, 10):
#     nextpoint = next_point(0, x)
#     pygame.draw.circle(screen, (0,0,0), (x, SCREENY - nextpoint), 2)
#     pygame.display.update()

def doshit(screen, centre):
    coords = []
    y = 0
    Step = 0.01
    x = -centre[0]
    drawX = 0
    drawY = 0
    print("Calculating")
    #centre = (int(SCREENX/2), int(SCREENY/2))
    #for x in range(-SCREENX, SCREENX, 1):
    while x <= (SCREENX - centre[0]):                               #Type Functions here -- Note, math, automaticallty uses radians, math.sin(math.radians(x)) will return the degree value of sin(x)
        #y = int(math.tan(math.tan(x))*100)
        #y = int(math.sin(math.radians(3*x + 5)*x**2)*100)
        #y = int((x + 5*x)*math.sin(math.radians(x**2))/10)
        #y = int((x)*math.sin(math.radians(x)))
        y = int(math.sin(math.radians(x))*100)
        #y = int((0.01)*(x**2)-(3*x)+10)
        if y < -100000:
            y = -100000
        if y > 100000:
            y = 100000

        drawX = int(x + centre[0])
        drawY = centre[1] - y
        coords.append((drawX, drawY))
        # coords.append((drawX, centre[1]-int(math.cos(math.radians(x))*100)))
        # coords.append((drawX, centre[1]-int(math.sin(math.radians(x*math.pi))*100)))
        x += Step

    ycoords = []
    for coord in coords: ycoords.append(coord[1])
    maxY = max(ycoords)
    factor = centre[1]/maxY

    screen.fill((255,255,255))
    draw_axis(centre, screen)
    print("Drawing")
    for coord in coords:
        pygame.event.pump()
        pygame.draw.circle(screen, (0,0,0), coord, 2)
        #pygame.display.update()
    print("Done")
    pygame.display.update()

# def doothershit(screen, centre, data):
#     draw_axis(centre, screen)
#     for coord in data:
#         pygame.event.pump()
#         pygame.draw.circle(screen, (0,0,0), coord, 2)
#         pygame.display.update()

# for x in range(0, SCREENX, 1):
#     y = int(0.25*x)
#     pygame.draw.circle(screen, (0,0,0), (x, SCREENY - y), 2)
#     pygame.display.update()

what = False
what2 = True
centre = (0, 0)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                what = True
                what2 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                what = False
    if what:
        centre = pygame.mouse.get_pos()
        draw_axis(centre, screen)
    if not what and not what2:
        if CALC:
            start = time.time()
            doshit(screen, centre)
            print(time.time()-start)
        else:
            doothershit(screen, centre, data)
        what2 = True
