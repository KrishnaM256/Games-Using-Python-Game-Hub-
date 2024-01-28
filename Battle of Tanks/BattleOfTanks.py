import pygame
from sys import exit
pygame.mixer.init()

def shot1_movement(shot1_rect_list):
    if shot1_rect_list:
        for shot1_rect in shot1_rect_list:
            shot1_rect.x += 5
            screen.blit(shot1_img,shot1_rect)
        return shot1_rect_list
    else : return []
                    
def shot2_movement(shot2_rect_list):
    if shot2_rect_list:
        for shot2_rect in shot2_rect_list:
            shot2_rect.x -= 5
            screen.blit(shot2_img,shot2_rect)
        return shot2_rect_list
    else : return []

def collision1(tank,shot):
    for shot in shot2_rect_list:
        if shot.collidepoint(tank.center) :
            Hit_sound.play()
            shot2_rect_list.remove(shot)
            pygame.event.post(pygame.event.Event(shot1_Hit))
            return screen.blit(collision_img,tank.midtop)
        elif shot.x>= 640:
            shot2_rect_list.remove(shot)

def collision2(tank,shot):
    for shot in shot1_rect_list:
        if shot.collidepoint(tank.center):
            Hit_sound.play()
            shot1_rect_list.remove(shot)
            pygame.event.post(pygame.event.Event(shot2_Hit))
            return screen.blit(collision_img,tank)
        elif shot.x <=0:
            shot1_rect_list.remove(shot)

def health1():
    tank1health = test_text.render(f"Health:{tank1_health}",False,'white')
    screen.blit(tank1health,(50,50))

def health2():
    tank2health = test_text.render(f"Health:{tank2_health}",False,'white')
    screen.blit(tank2health,(400,50))

def winner():
    if win_text == "RED TANK WINS!!":
        win = test2_text.render(f"{win_text}",False,(100,100,100))   
        win_rect = win.get_rect(center = (310,100))
        pygame.draw.rect(screen,(200,0,0),win_rect,0,10)     
        screen.blit(win,win_rect)
    if win_text == "BLUE TANK WINS!!":
        win = test2_text.render(f"{win_text}",False,(100,100,100))
        win_rect = win.get_rect(center = (310,100))     
        pygame.draw.rect(screen,(0,0,250),win_rect,0,10)
        screen.blit(win,win_rect)
    pygame.display.update()

pygame.init()
#Loading Music
background_sound = pygame.mixer.Sound('Battle-of-Tanks-BG.mp3')
background_sound.set_volume(0.5)
shot1_sound = pygame.mixer.Sound('shot1-sound.mp3')
shot1_sound.set_volume(1)
shot2_sound = pygame.mixer.Sound('shot2-sound.mp3')
shot2_sound.set_volume(0.5)
Hit_sound = pygame.mixer.Sound("collision-of-shot-with-tank.mp3")
Blast_sound = pygame.mixer.Sound('heavy-beam-weapon-7052.mp3')
Blast_sound.set_volume(1)

shot1_rect_list = []
shot2_rect_list = []

# creating a blank screen
screen = pygame.display.set_mode((640,400))
pygame.display.set_caption("Battle of Tanks")
clock = pygame.time.Clock()
#adding background img
background_img = pygame.image.load("pygameImgs/tanks/10_Cinesite_ML2_MOR1580_v43.1068-BURN.jpg")
begin_img = pygame.image.load("pygameImgs/tanks/th.jpg")
over_img = pygame.image.load('pygameImgs/tanks/95-951065_avengers-endgame-final-battle-background.jpg')
#adding tank imgs
tank1_img = pygame.image.load("pygameImgs/tanks/52-523806_preview-top-down-tank-png-transparent-png-removebg-preview-removebg-preview.png")
tank1_rect = tank1_img.get_rect(topleft = (5,200))
tank2_img = pygame.image.load("pygameImgs/tanks/png-transparent-tank-shooter-game-game-asset-angle-video-game-game-asset-thumbnail-removebg-preview-removebg-preview.png")
tank2_rect = tank2_img.get_rect(topleft = (520,250))
#adding shot imgs
shot1_img = pygame.image.load("pygameImgs/tanks/53ff38ae114a6-removebg-preview.png")
shot1_rect = shot1_img.get_rect(center = tank1_rect.midright)
shot2_img = pygame.image.load("pygameImgs/tanks/fire_bullet-removebg-preview.png")
shot2_rect = shot2_img.get_rect(center = tank2_rect.midleft)
#adding collision img
collision_img = pygame.image.load('pygameImgs/tanks/d2r7iy0-86b6de58-cf29-4373-8267-9e915488e909.png')
# Text Part of Our Game
test2_text = pygame.font.Font(None,70)
test_text = pygame.font.Font(None,40)
#adding game name 
name_text = test2_text.render("BATTLE OF TANKS",False,'grey')
name_rect = name_text.get_rect(center = (310,200))
#adding instruction text
instruction1_text = test_text.render("Press R-Shift to Start",False,'white')
instruction1_rect = instruction1_text.get_rect(center = (310,300))
instruction2_text = test_text.render("Press R-Shift to Restart",False,'white')
instruction2_rect = instruction2_text.get_rect(center = (310,300))
win_text=""
tank1_health = 10
tank2_health = 10

shot1_Hit = pygame.USEREVENT + 1
shot2_Hit = pygame.USEREVENT + 2

game_active = False
background_sound.play(loops = -1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_e :    
                    shot1_rect_list.append(shot1_img.get_rect(center = tank1_rect.midright))
                    shot1_sound.play()     
                if event.key== pygame.K_u :
                    shot2_rect_list.append(shot2_img.get_rect(center = tank2_rect.midleft))
                    shot2_sound.play()

            if event.type == shot1_Hit:
                tank1_health -= 1

            if event.type == shot2_Hit:
                tank2_health -= 1
            
            if tank1_health <=0:
                win_text = "RED TANK WINS!!"
                shot1_sound.stop()
                shot2_sound.stop()
                Blast_sound.play()
                pygame.time.delay(2000)        
                # Blast_sound.stop()
                game_active=False

            if tank2_health <=0:
                win_text = "BLUE TANK WINS!!"
                shot1_sound.stop()
                shot2_sound.stop()
                Blast_sound.play()
                pygame.time.delay(2000)
                # Blast_sound.stop()
                game_active=False

        else:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RSHIFT:
                    game_active=True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if tank1_rect.y >=0: tank1_rect.y -=5
    if keys[pygame.K_i]:
        if tank2_rect.y >=0: tank2_rect.y -= 5

    if keys[pygame.K_s]:
        if tank1_rect.y<=300:tank1_rect.y += 5
    if keys[pygame.K_k]:
        if tank2_rect.y<=300:tank2_rect.y += 5

    if keys[pygame.K_a]:
        if tank1_rect.x >= 0:tank1_rect.x -=3
    if keys[pygame.K_d]:
        if tank1_rect.x <= 220:tank1_rect.x +=3

    if keys[pygame.K_j]:
        if tank2_rect.x >= 320: tank2_rect.x -=3
    if keys[pygame.K_l]:
        if tank2_rect.x <= 530:tank2_rect.x +=3


    if game_active:
        Blast_sound.stop()
        screen.blit(background_img,(0,0))
        screen.blit(tank1_img,tank1_rect)
        screen.blit(tank2_img,tank2_rect)                
        pygame.draw.line(screen,'gold',(320,0),(320,400),1)
        shot1_rect_list =shot1_movement(shot1_rect_list)
        shot2_rect_list =shot2_movement(shot2_rect_list)
        collision1(tank1_rect,shot2_rect)
        collision2(tank2_rect,shot1_rect)
        health1()
        health2()

    else :
        if win_text == "":
            screen.blit(begin_img,(0,0))
            screen.blit(instruction1_text,instruction1_rect)
            screen.blit(name_text,name_rect)
        else:
            screen.blit(over_img,(0,0))
            screen.blit(instruction2_text,instruction2_rect)
            screen.blit(name_text,name_rect)

        shot1_rect_list.clear()
        shot2_rect_list.clear()
        tank1_rect.topleft = (5,170)
        tank2_rect.topleft = (520,170)
        tank1_health = 10
        tank2_health = 10
        winner()
    
    pygame.display.update()
    clock.tick(60)
    