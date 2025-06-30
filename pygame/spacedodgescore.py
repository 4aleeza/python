import pygame
import time
import random 
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
clock = pygame.time.Clock()
start_time = time.time()


PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40
PLAYER_VEL = 3
STAR_VEL = 5
STAR_WIDTH = 5
STAR_HEIGHT = 10
GOLD_VEL = 7
GOLD_HEIGHT = 5
GOLD_WIDTH = 5

FONT = pygame.font.SysFont("display", 20)


BG = pygame.image.load("bg.png")
def draw(player, elapsed_time, stars, golds, score):
    WIN.blit(BG, (0,0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 30))
    score_text = FONT.render(f"Score: {score}",1,"white")
    pygame.draw.rect(WIN, "blue", player)
    WIN.blit(score_text, (10,10))
    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    

    for gold in golds:
        pygame.draw.rect(WIN, "yellow", gold)

    pygame.display.update()


def main():
    score = 0
    run = True
    player = pygame.Rect(400, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    star_add_increment = 2000
    gold_add_increment = 4000
    gold_count = 0 
    golds = []
    gold_hit = False
    star_count = 0
    stars = []
    hit = False
    while run:
        gold_count += clock.get_time()

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
   

        if star_count > star_add_increment: #as soon as you cross 2000 miliseconds you add another star
            for i in range(3):
             star_x = random.randint(0, WIDTH-STAR_WIDTH)
             star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
             stars.append(star)
            star_add_increment = max(200, star_add_increment-50)
            star_count = 0
        if gold_count > gold_add_increment and len(golds)==0 :
                gold_x = random.randint(0, WIDTH-GOLD_WIDTH) ###
                gold = pygame.Rect(gold_x, -GOLD_HEIGHT, GOLD_WIDTH, GOLD_HEIGHT)
                golds.append(gold)
                gold_count = 0
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (player.x - PLAYER_VEL )>=0 :
            player.x -= PLAYER_VEL #x = x - vel (cords it shifts by on x axis)
        if keys[pygame.K_RIGHT] and (player.x + (PLAYER_WIDTH+PLAYER_VEL))<=800:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and (player.y - PLAYER_VEL ) >= 0 :
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and (player.y + (PLAYER_HEIGHT+PLAYER_VEL)) <=600 :
            player.y += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("Game Over!", 35, "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        for gold in golds[:]:
            gold.y += GOLD_VEL
            if gold.y > HEIGHT: 
                golds.remove(gold)
            elif gold.y + gold.height >= player.y and gold.colliderect(player):
                golds.remove(gold)
                gold_hit = True
                break

        if gold_hit:
            score = score + 1
            gold_hit = False

        draw(player, elapsed_time, stars, golds, score)

 
    pygame.quit()

if __name__ == "__main__":
    main()
