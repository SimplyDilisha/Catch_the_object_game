import pygame
import random

pygame.init()

score=0
speed=5
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,30)

#screen
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("Catch the object game")

#player
player=pygame.Rect(180,350,50,15)

#object
object=pygame.Rect(random.randint(0,350),0,30,30)

game=True
while game:
    clock.tick(60)
    screen.fill((255,255,255))

    # Exit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    
    # Movements
    move=pygame.key.get_pressed()
    if move[pygame.K_LEFT]:
        player.x-=5
    if move[pygame.K_RIGHT]:
        player.x+=5

    #Control movements, keep player inside the screen
    if player.x<0:
        player.x=0
    if player.x>345:
        player.x=345

    # Object
    object.y+=speed
    if object.colliderect(player):
        score+=1
        object.y=0
        object.x=random.randint(0,350)

    if object.y>400:
        object.y=0
        object.x=random.randint(0,350)
    
    # Draw, also for txt render() is used
    pygame.draw.rect(screen,(0,0,255),player)
    pygame.draw.rect(screen,(255,0,0),object)

    text=font.render(f"Score: {score}",True,(0,0,0))
    screen.blit(text,(10,10))

    pygame.display.update()

pygame.quit()

