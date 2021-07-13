
#--------------IMPORTS-----------------
import pygame 
import random
import time 
#--------------------------------------

#--------------GLOBAL VARS-------------
swidth, sheight = 500, 500 
run = True
r, b = 0, 0
pressed = False 
#--------------------------------------

#--------------PYGAME INITIALISATION------------------
pygame.init()
window = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("RACE SIM")
#-----------------------------------------------------

#--------------MAIN LOOP------------------------------
while run:
    pygame.time.delay(55)
    window.fill((0,0,0))

    #-----------LOCAL VARS----------------------------
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    keys = pygame.key.get_pressed()
    red = "Red: " + str(r) 
    blue = "Blue: " + str(b) 
    x1, y1, x2, y2 = 215, 470, 295, 470 # (the coordinates of the red and the blue ball resp.)
    #-------------------------------------------------

    Rscore = myfont.render(red, False, (255, 255, 255))
    Bscore = myfont.render(blue, False, (255,255,255))
    window.blit(Rscore, (0,0))
    window.blit(Bscore, (420, 0))
    pygame.draw.circle(window, (255, 0, 0), (x1, y1), 20)
    pygame.draw.circle(window, (0, 0, 255), (x2, y2), 20)
    pygame.display.update() 

    for event in pygame.event.get(): # (if the window is closed)
        if event.type == pygame.QUIT : 
            run = False 

    if keys[pygame.K_SPACE]: # (if space is pressed)
        pressed = True 
        pygame.draw.circle(window, (255, 0, 0), (x1, y1), 20)
        pygame.draw.circle(window, (0, 0, 255), (x2, y2), 20)
        v1, v2 = random.randrange(10, 31), random.randrange(10, 31)
        

        while (y1 >= 45) and (y2 >= 45):
            if pressed: 
                v1, v2 = random.randrange(10, 31), random.randrange(10, 31)# giving random speeds at every step

            y1 -= v1
            y2 -= v2
            window.fill((0,0,0))
            pygame.draw.circle(window, (255, 0, 0), (x1, y1), 20)
            pygame.draw.circle(window, (0, 0, 255), (x2, y2), 20) 
            Rscore = myfont.render(red, False, (255, 255, 255))
            Bscore = myfont.render(blue, False, (255,255,255))
            window.blit(Rscore, (0,0))
            window.blit(Bscore, (420, 0))
            pygame.display.update() 
            time.sleep(0.15)
        if y1 < y2 : 
            r += 1
        elif y2 < y1 : 
            b += 1   
        
        pygame.display.update() 

final = red + " " + blue  
myfont = pygame.font.SysFont('Comic Sans MS', 30)
Fscore = myfont.render(final, False, (255,255,255))
window.blit(Fscore, (150, 225))
pygame.display.update()
time.sleep(3)
pygame.quit()
#------------------------------------------------------------
