import pygame
from sys import exit
from random import randint
pygame.mixer.init()

    # function for getting score

def get_time(x,y):
    current_time = (pygame.time.get_ticks() - start_time)//1000
    score_text = test_font.render(f"Score: {current_time} ",False,'red')
    score_rect = score_text.get_rect(midleft = (x,y))
    pygame.draw.rect(win,'white',score_rect,0,5)
    win.blit(score_text,score_rect)
    return current_time

    # function for the enemy movement and motion and position

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5 + int(score)/10
            if obstacle_rect.bottom == 349 : 
                win.blit(snail_img,obstacle_rect)
            else :               
                win.blit(fly_img,obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100 ]
        return obstacle_list
    else : return []

    # function for the collisions

def collisions(player,obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player.collidepoint(obstacle_rect.center):
                collision_sound.play(1)
                return False
    return True

    # function for the player animation

def player_animation():
    global player_img,player_index
    if player_rect.bottom < 349:
        player_img = player_jump
    else : 
        player_index += 0.09
        if player_index >= len(player_walking): player_index=0
        player_img=player_walking[int(player_index)]
            
pygame.init()      

obstacle_rect_list = []

    #creating display
win = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
pygame.display.set_caption("Escape Runner")
    # Heading and game name
test_font = pygame.font.Font(None,40)
name_text = test_font.render("Escape Runner",False,(100,100,100))
name_text_rect = name_text.get_rect(center=(300,350))

score = 0
        # creating ground
ground_img = pygame.image.load('./pygameImgs/Ground_(front_layer).png').convert_alpha()
        # creating sky
sky_img = pygame.image.load('pygameImgs/pngtree-beautiful-fantasy-animation-background-picture-image_1595640.jpg').convert_alpha()

over_display = pygame.Surface((600,400))
over_display.fill('White')
over_img = pygame.image.load("pygameImgs/mario_PNG17.png")
over_rect = over_img.get_rect(center = (300,200))

instructions_text = test_font.render("Press R-Shift To Start",False,(200,200,200))
instructions_text_rect = instructions_text.get_rect(center = (310,50))
pygame.draw.rect(over_display,(0,0,100),instructions_text_rect,0,15)

        #snail1
snail1_img = pygame.image.load('pygameImgs/images__1_-removebg-preview.png').convert_alpha()
snail2_img = pygame.image.load('pygameImgs/th__1_-removebg-preview.png').convert_alpha()
snail = [snail1_img,snail2_img]
snail_index = 0
snail_img = snail[snail_index] 
        # flying enemy
fly1_img = pygame.image.load("pygameImgs/th__3_-removebg-preview.png")
fly2_img = pygame.image.load("pygameImgs/th__3_-removebg-preview (2).png")
fly = [fly1_img,fly2_img]
fly_index = 0
fly_img = fly[fly_index]

        # creating player character
player_walking_1 = pygame.image.load('pygameImgs/mario_PNG115.png').convert_alpha()
player_walking_2 = pygame.image.load('pygameImgs/ddb07kl-db41f6fd-0d2d-4df6-941e-9b84b604c50d.png').convert_alpha()
player_walking = [player_walking_1,player_walking_2]
player_index = 0
player_img = player_walking[player_index]

player_rect = player_img.get_rect(midbottom=(70,349))

background_sound = pygame.mixer.Sound('Escape-Runner-BG.mp3')
background_sound.set_volume(0.6)
jump_sound = pygame.mixer.Sound('ER-Jump.mp3')
collision_sound = pygame.mixer.Sound('ER-collided.mp3')
start_time = 0
player_gravity = 0 
game_active = False

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,800)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,60)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,600)

background_sound.play(loops=-1)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if game_active: 
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.y >= 180:
                    player_jump = pygame.image.load('pygameImgs/mario_PNG38.png').convert_alpha()
                    jump_sound.play()
                    player_gravity = -22
                
            if event.type == obstacle_timer :
                if randint(0,2): 
                    obstacle_rect_list.append(snail_img.get_rect(midbottom=(randint(600,750),349)))   
                else :
                    obstacle_rect_list.append(fly_img.get_rect(midbottom=(randint(600,750),250)))

            if event.type == snail_animation_timer:
                if snail_index == 0: snail_index=1      
                else : snail_index =0
                snail_img=snail[snail_index]
            if event.type == fly_animation_timer:
                if fly_index == 0: fly_index =1
                else : fly_index =0
                fly_img=fly[fly_index]

        else :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    game_active = True 
                    start_time = pygame.time.get_ticks()
        
    if game_active :   
        collision_sound.stop() 
        win.blit(sky_img,(0,0)) 
        win.blit(ground_img,(0,-50))          
        score = get_time(400,50)
        player_gravity += 1
        player_rect.y += player_gravity  

        if player_rect.y >= 250:
            player_rect.y = 250
        win.blit(player_img,player_rect)
        player_animation()
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect,obstacle_rect_list)

    else :
        win.blit(over_display,(0,0))
        win.blit(over_img,over_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (70,349)
        player_gravity = 0
        end_score = test_font.render(f"Score: {score}",False,(250,250,250))
        end_score_rect = end_score.get_rect(center = (320,50))
        if score == 0:
            win.blit(instructions_text,instructions_text_rect)
        if score != 0 :
            win.blit(end_score,end_score_rect)
        win.blit(name_text,name_text_rect)
        
    pygame.display.update()
    clock.tick(60) 