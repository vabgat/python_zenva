import pygame

def checkCollision(x,y,treasureX,treasureY):
    global screen,textWin
    collisionState = False
    if y >= treasureY and y <= treasureY+25: #if head is in between top and bottom
        if x >= treasureX and x<= treasureX+20: # if left of player is in between left and right of treasure 
            y = 450
            collisionState = True
        elif x+20 >= treasureX and x+20 <= treasureX+2: # if right of player is in between left and right of treaure
            y = 450
            collisionState = True
    elif y + 25>= treasureY and y+25 <= treasureY +25: # if tail is in between top and bottom
        if x >= treasureX and x<= treasureX+20: # if left of player is in between left and right of treasure
            y = 450
            collisionState = True
        elif x+20 >= treasureX and x+20 <= treasureX + 20: # if right of player is in between left and right of treaure
            y = 450
            collisionState = True
    return collisionState,y
    
pygame.init()
screen = pygame.display.set_mode((500,500))
finished = False
x = 250 - 12.5
y = 450
level = 1

## player image
playerImage = pygame.image.load("Player.png")
playerImage = pygame.transform.scale(playerImage,(20,25))
playerImage = playerImage.convert_alpha() # made ready for use
# convert into alpha removes black around of image

## enemy image
enemyImage = pygame.image.load("enemy.png")
enemyImage = pygame.transform.scale(enemyImage,(20,25))
enemyImage = enemyImage.convert_alpha()
enemyX = 200
enemyY = 350

## background
backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage,(500,500))
screen.blit(backgroundImage,(0,0))

## treasure
treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage,(20,25))
treasureImage = treasureImage.convert_alpha()
treasureX = 250 - 12.5
treasureY = 100
screen.blit(treasureImage, (treasureX,treasureY))

# font when teasure is hit
font = pygame.font.SysFont("comicsans",50)                           
frame = pygame.time.Clock() # define a clock
collisionTreasure = False
collisionEnemy = False
movingRight = True

# list of enemies
enemies = [(enemyX,enemyY,movingRight)]

while finished == False: # while our game is not finished
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pressedKeys = pygame.key.get_pressed()

## enemy movement computation
    enemyIndex = 0
    for enemyX,enemyY,movingRight in enemies: 
        if enemyX >= 420:
            movingRight = False
        elif enemyX < 50:
            movingRight = True
        if movingRight == True:
            enemyX +=5*level
        else:
            enemyX -=5*level
        enemies[enemyIndex] = (enemyX,enemyY,movingRight)
        enemyIndex+=1
    
    if pressedKeys[pygame.K_SPACE] == 1:
        y -= 5
#    rectOne = pygame.Rect(x,y,30,30) #x,y(start position) , width, height
#    color = (0,0,255) #R,G,B
    screen.blit(backgroundImage,(0,0))
    screen.blit(treasureImage, (treasureX,treasureY))
    screen.blit(playerImage,(x,y))
    for enemyX,enemyY,movingRight in enemies:
        screen.blit(enemyImage,(enemyX,enemyY))
        ## Collion with enemy
        collisionEnemy,y = checkCollision(x,y,enemyX,enemyY)
    
## Check for collision
    collisionTreasure,y = checkCollision(x,y,treasureX,treasureY)
    if collisionTreasure == True:
        level+=1
        enemies.append((enemyX-50*level,enemyY-50*level,False))
        textWin = font.render("You've reached the level %d !!" % level,True,(0,0,0))
        x_pos = textWin.get_width()/2
        y_pos = textWin.get_height()/2
        screen.blit(textWin,(250 - x_pos,250 - y_pos))
        pygame.display.flip() #update the screen and change the frame rate
        frame.tick(1)
        
 #   pygame.draw.rect(screen,color,rectOne)
    pygame.display.flip() # to update the screen
    frame.tick(20) # when it reaches this point the screen is paused by
    # 1/30th of time. This reduces the frequency with which
    # the object is diplayed
