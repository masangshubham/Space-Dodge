#Imports
import pygame
import time
import random
pygame.font.init()

#Define variables at top to make changes easy to manage
WIDTH, HEIGHT = 1000,800

#Create a window with title
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

#Include bg image and transform it to scale the window size.
BG = pygame.transform.scale(pygame.image.load("bg.jpg"),(WIDTH,HEIGHT))
#BG = pygame.image.load("bg.jpg")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
#PLAYER_VEL is the speed of the player by which it will move
PLAYER_VEL = 5


STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3


FONT = pygame.font.SysFont("comicsans",30)

#All drawing/ displays objects in 1 func
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s",1, "white")
    WIN.blit(time_text,(10, 10))

    pygame.draw.rect(WIN,"red",player)

    for star in stars:
        pygame.draw.rect(WIN,"white",star)

    pygame.display.update()

def main():
    run = True
    #create a player in this case a rectangle args(X,Y, objWidth,objHeight)
    player = pygame.Rect(200,HEIGHT-PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)
    #this to make the loop run at same speed / control the loop speed to 60 per min
    clock = pygame.time.Clock()

    start_time = time.time()
    elasped_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    # while loop to allways display the window
    while run:
        star_count += clock.tick(60)
        elasped_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x =random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment - 50)
            star_count=0

        for event in pygame.event.get():
            # always first write code to exit the program i.e when we click on the X button
            if event.type == pygame.QUIT:
                run = False
                break
        
        # code to move the player by listening to the key press also conditions to check the player does not go out of bound
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x-PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x+PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >=player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render("You Lost!", 1 ,"white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2 , HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elasped_time,stars)

    pygame.quit()

if __name__ == "__main__":
    main()