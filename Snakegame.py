import pygame
import random
pygame.init()

width=1000
height=500

screen = pygame.display.set_mode((width,height))


white = (255,255,255)
black=(0,0,0)
red=(255,0,0)
screen.fill(white)

img=pygame.image.load("frog.png")
coinSound=pygame.mixer.Sound('point.wav')

def gameOver():
    gameOverSound=pygame.mixer.Sound('music_1.wav')
    gameOverSound.play()
    font=pygame.font.SysFont(None,70)
    text=font.render("Game Over",True,red)  

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() #pygame quit
                quit() #python quit 

        screen.blit(text,(width/2-80,height/2-50))
        pygame.display.update()

def score(c):
    font=pygame.font.SysFont(None,40)
    #font=pygame.font.Font('font_1.tff',40) takes font from an external file.
    text=font.render("Score:{}".format(c),True,red)
    screen.blit(text,(100,10))

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,black,[snakeList[i][0],snakeList[i][1],50,50])

def game():
    imgWidth=img.get_width()
    imgHeight=img.get_height()
    imgX=random.randint(0,width-imgWidth)
    imgY=random.randint(0,height-imgHeight)

    x=0
    y=0
    moveX=0
    moveY=0
    counter=0

    snakeList=[]
    snakeLength=1

    FPS=100
    clock=pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    moveX=5
                    moveY=0
                elif event.key==pygame.K_LEFT:
                    moveX=-5
                    moveY=0
                elif event.key==pygame.K_DOWN:
                    moveX=0
                    moveY=5
                elif event.key==pygame.K_UP:
                    moveX=0
                    moveY=-5

        screen.fill(white)
        screen.blit(img,(imgX,imgY))
        rect_1=pygame.Rect(x,y,50,50)
        rect_2=pygame.Rect(imgX,imgY,imgWidth,imgHeight)
        
        x+=moveX
        y+=moveY

        score(counter)

        snakeHead=[]
        snakeHead.append(x)
        snakeHead.append(y)

        snakeList.append(snakeHead)

        snake(snakeList)
        if len(snakeList)>snakeLength:
            del snakeList[0]

        for each in snakeList[:-1]:
            if snakeList[-1]==each:
                gameOver()


        if rect_1.colliderect(rect_2):
            imgX=random.randint(0,width-imgWidth)
            imgY=random.randint(0,height-imgHeight)
            counter+=1
            FPS+=8
            snakeLength+=3
            coinSound.play()

        if x>width:
            x=-50
        elif y > height:
            y = -50
        elif x < -50:
            x = width
        elif y < -50:
            y = height

        pygame.display.update()
        clock.tick(FPS)

game()
                    
