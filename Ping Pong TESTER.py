                
"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame, time
import random as rand

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


pygame.init()
pygame.font.init()

# Set the width and height of the screen [width, height]
size = (900, 642)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

# Loop until the user clicks the close button.
done = False

#initiate variables
xcoord1 = 20
ycoord1 = 305

yspeed1 = 0

xcoord2 = 860
ycoord2 = 305

yspeed2 = 0

xcoord3 = 450
ycoord3 = 321

xspeed3 = 5
yspeed3 = 4

p1_score = 0
p2_score = 0

pause = 0
gamepause = 1
settings = 1
gameplay = 1

##X=400
##Y=400
##
##display_surface = pygame.display.set_mode((X, Y ))

ballspeedup = pygame.draw.rect(screen, WHITE, [600,125,40,40])
ballspeeddown = pygame.draw.rect(screen, WHITE, [300,125,40,40])
backbutton = pygame.draw.rect(screen, WHITE, [10,10,40,40])
play_gamebutton = pygame.draw.rect(screen, WHITE, [450,450,120,40],3)




def sprite(yspeed1, yspeed2, yspeed3, xspeed3):
    global p1, p2, ball
    p1 = pygame.draw.rect(screen, RED,[xcoord1,ycoord1,20,100],0)
    p2 = pygame.draw.rect(screen, BLUE,[xcoord2, ycoord2, 20, 100],0)
    ball = pygame.draw.ellipse(screen, WHITE, [xcoord3, ycoord3, 20, 20],0)
    

def lines ():
    ln_start = 0
    for i in range(20):
        "LINES"
        pygame.draw.rect(screen, WHITE, [450, ln_start, 5, 25],0)
        ln_start += 40
        
'''Fonts'''
font = pygame.font.SysFont('Comic Sans MS', 30)
pausefont = pygame.font.SysFont('ARIAL', 60)
settingsfont = pygame.font.SysFont('ARIAL', 60)
optionfont = pygame.font.SysFont('ARIAL', 30)
plus_minus_button = pygame.font.SysFont('Arial', 60)
numberfont = pygame.font.SysFont('ARIAL', 30)
textsurface = font.render(str(p1_score), False, (0, 0, 0))

'''images'''
fish = pygame.image.load(r'fish.png')
settingsicon = pygame.image.load(r'settings.png')
settingsicon = pygame.transform.scale(settingsicon, (40, 40))
backarrow = pygame.image.load(r'back arrow.jfif')
backarrow = pygame.transform.scale(backarrow, (50, 50))


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                yspeed1 = -7
            elif event.key == pygame.K_s:
                yspeed1 = 7
            elif event.key == pygame.K_UP:
                yspeed2 = -7
            elif event.key == pygame.K_DOWN:
                yspeed2 = 7
            elif event.key == pygame.K_ESCAPE:
                quit()
            elif event.key == pygame.K_p:
                gamepause *= -1
            elif event.key == pygame.K_TAB:
                if gamepause == -1:
                    print("Settings")
                    settings *= -1
                    
                else:
                    pass

            
##            elif event.type == pygame.MOUSEBUTTONDOWN:
##                # If the user clicked on the input_box rect.
##                if input_box.collidepoint(event.pos):
##                    # Toggle the active variable.
##                    active = not active
##                    print("YAY")
##                else:
##                    active = False
            
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                yspeed1 = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yspeed2 = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:
                    # If the user clicked on the input_box rect.
                    if pausebutton.collidepoint(mouse_pos):
                        gamepause *= -1


        ### Makes ball speed faster
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                
                if ballspeedup.collidepoint(mouse_pos):
                    xspeed3 = xspeed3 + 1
                    yspeed3 = yspeed3 + 1
                    print(xspeed3, yspeed3)


        ### Makes ball speed slower
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                
                if ballspeeddown.collidepoint(mouse_pos):
                    xspeed3 = xspeed3 - 1
                    yspeed3 = yspeed3 - 1
                    print(xspeed3, yspeed3)

                    
        #Back Button - for settings
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if event.button == 1:
                
                if backbutton.collidepoint(mouse_pos):
                    settings *= -1
                    #print("input")

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            mouse_pos = pygame.mouse.get_pos()

            if event.button == 1:
                
                if play_gamebutton.collidepoint(mouse_pos):
                    gameplay *= -1

        

    
    
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing and logic code should go here
    score_text_p2 = font.render(str(p1_score), False, (RED))
    score_text_p1 = font.render(str(p2_score), False, (BLUE))
    screen.blit(score_text_p2, (475, 0))
    screen.blit(score_text_p1, (415, 0))

    lines()
    
    pausebutton = pygame.draw.rect(screen, WHITE, [866, 5, 5, 40],0)
    pausebutton = pygame.draw.rect(screen, WHITE, [879, 5, 5, 40],0)
    
    pausebutton = pygame.draw.rect(screen, BLACK, [855,5,40,40],3)
    play_gamebutton = pygame.draw.rect(screen, WHITE, [450,450,120,40],3)

    #display_surface.fill(BLACK)
  
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.


    screen.blit(fish, (0, 0))
    

    ###ballspeedup = pygame.draw.rect(screen, WHITE, [100,100,40,40])
    if gameplay == 1:
        screen.fill (BLACK)
        play_gamebutton = pygame.draw.rect(screen, WHITE, [450,450,120,40],3)

    if gameplay == -1:
            
        if ycoord1 > 550 or ycoord1 < 0:
            yspeed1 *= -1
        if ycoord2 > 550 or ycoord2 < 0:
            yspeed2 *= -1
        if ycoord3 > 622 or ycoord3 < 0:
            yspeed3 *= -1
        
        if gamepause == 1:
            ycoord1 += yspeed1
            ycoord2 += yspeed2

            if pause < 0:
                xcoord3 += xspeed3
                ycoord3 += yspeed3
            

            
            
            sprite(yspeed1, yspeed2, yspeed3, xspeed3)
            p1_wall = pygame.draw.rect(screen, BLACK, [0, 0, 0, 642],0)
            p2_wall = pygame.draw.rect(screen, BLACK, [899, 0, 0, 642],0)
            
            
            

            
            if ball.colliderect(p2):
                xspeed3 = xspeed3 * -1
                yspeed3 = rand.randint(-5,-1)
            if ball.colliderect(p1):
                xspeed3 = xspeed3 * -1
                yspeed3 = rand.randint(1,5)
            if ball.colliderect(p1_wall):
                p2_score += 1
                print(p2_score)
                xcoord3 = 450
                ycoord3 = 321
                xcoord1 = 20
                ycoord1 = 200
                yspeed1 = 0
                xcoord2 = 860
                ycoord2 = 200
                yspeed2 = 0
                pause = 180
            if ball.colliderect(p2_wall):
                p1_score += 1
                print(p1_score)
                xcoord3 = 450
                ycoord3 = 321
                xcoord1 = 20
                ycoord1 = 200
                yspeed1 = 0
                xcoord2 = 860
                ycoord2 = 200
                yspeed2 = 0
                pause = 180

            pause -= 1

        
            

    if gamepause == -1:

        screen.fill(BLACK)
        score_text_p2 = font.render(str(p1_score), False, (RED))
        score_text_p1 = font.render(str(p2_score), False, (BLUE))
        screen.blit(score_text_p2, (475, 0))
        screen.blit(score_text_p1, (415, 0))
        sprite(0, 0, 0, 0)
        pausebutton = pygame.draw.rect(screen, WHITE, [866, 5, 5, 40],0)
        pausebutton = pygame.draw.rect(screen, WHITE, [879, 5, 5, 40],0)
    
        pausebutton = pygame.draw.rect(screen, BLACK, [855,5,40,40],3)
        
        gamepausetexty = pausefont.render('GAME PAUSED', True, (WHITE))
        screen.blit(gamepausetexty, (275, 321))
        screen.blit(settingsicon, (10, 10))

    
        #ballspeedup = pygame.draw.rect(screen, WHITE, [500,400,40,40])
        #ballspeeddown = pygame.draw.rect(screen, WHITE, [395,600,40,40])

    if settings == -1:

        screen.fill(BLACK)
        #score_text_p2 = font.render(str(p1_score), False, (RED))
        #score_text_p1 = font.render(str(p2_score), False, (BLUE))
        #screen.blit(score_text_p2, (475, 0))
        #screen.blit(score_text_p1, (415, 0))
        #sprite(0, 0, 0, 0)
        '''Header'''
        settingsheadertext = settingsfont.render('Settings', True, (WHITE))
        screen.blit(settingsheadertext, (375, 0))

        '''Option'''
        optiontext = optionfont.render('Ball Speed:', True, (WHITE) )
        screen.blit(optiontext, (400, 120))

        optiontext = optionfont.render('Paddle Speed:', True, (WHITE) )
        screen.blit(optiontext, (385, 220))
        
        '''Button Hitboxes'''
        ballspeedup = pygame.draw.rect(screen, WHITE, [600,125,40,40])
        ballspeeddown = pygame.draw.rect(screen, WHITE, [300,125,40,40])
        
        '''Plus or Minus for speeds '''
        minusbutton = plus_minus_button.render('-', True, (GREEN))
        screen.blit(minusbutton, (375, 200))

        '''Back Button'''        
        backbutton = pygame.draw.rect(screen, WHITE, [10,10,40,40])
        screen.blit(backarrow, (10, 10))
        #'''To display ballspeed text'''

        '''Deafult Value'''

        if xspeed3 == 5 and yspeed3 == 4:
            ballspeed = numberfont.render('1', True, (WHITE))
            screen.blit(ballspeed, (450, 160))
            
        elif xspeed3 == 6 and yspeed3 == 5:
            ballspeed = numberfont.render('2', True, (WHITE))
            screen.blit(ballspeed, (450, 160))

        #'''Highest Speed'''

        elif xspeed3 == 7 and yspeed3 == 6:
            ballspeed = numberfont.render('3', True, (WHITE))
            screen.blit(ballspeed, (450, 160))
        #'''Slower Speeds'''
        
        elif xspeed3 == 4 and yspeed3 == 3:
            ballspeed = numberfont.render('-1', True, (WHITE))
            screen.blit(ballspeed, (442.5, 160))

        elif xspeed3 == 3 and yspeed3 == 2:
            ballspeed = numberfont.render('-2', True, (WHITE))
            screen.blit(ballspeed, (442.5, 160))
        #'''Slowest Speed'''
        
        elif xspeed3 == 2 and yspeed3 == 1:
            ballspeed = numberfont.render('-3', True, (WHITE))
            screen.blit(ballspeed, (442.5, 160))
        
        

##    if event.type == pygame.MOUSEBUTTONDOWN:
##        # If the user clicked on the input_box rect.
##        if pausebutton.collidepoint(event.pos):
##        x = 100
##        y = 100
##                 print("hello")

        
        

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
