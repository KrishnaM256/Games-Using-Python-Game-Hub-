import pygame
from sys import exit
import random

pygame.mixer.init()

def winText():
    if pressed_num == secret_num:
        return False
    elif Life<=0:
        return False
    return game_active

def over_text():
    if win_text == "You Won!":
        wining_text = test_text.render(f"{win_text}",False,(100,10,100))
        wining_text_rect = wining_text.get_rect(center = (300,200))
        screen.blit(wining_text,wining_text_rect)
    if win_text == "You Lost!" :
        wining_text = test_text.render(f"{win_text}",False,"Red")
        wining_text_rect = wining_text.get_rect(center = (300,200))
        screen.blit(wining_text,wining_text_rect)
    pygame.display.update()

def life(Life):
    Life_text = Life_test_text.render(f"Life:{Life}",False,"red")
    Life_text_rect = Life_text.get_rect(center = (500,50))
    pygame.draw.rect(screen,(250,250,250),Life_text_rect,0,10)
    screen.blit(Life_text,Life_text_rect)

def guide_less(pressed_num,secret_num):
        guide_text = Life_test_text.render("You guessed lesser number",False,(0,100,100))
        guide_text_rect = guide_text.get_rect(center = (300,170))
        screen.blit(guide_text,guide_text_rect)
def guide_high(pressed_num,secret_num):
        guide_text = Life_test_text.render("You guessed higher number",False,(0,100,100))
        guide_text_rect = guide_text.get_rect(center = (300,170))
        screen.blit(guide_text,guide_text_rect)

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("NumberGuessingGame")
clock = pygame.time.Clock()

background_img = pygame.image.load("pygameImgs/numguessinggame/depositphotos_45805773-stock-photo-colorful-random-number-background-illustration.jpg")
number_img = pygame.image.load("pygameImgs/numguessinggame/pngtree-creative-font-stereo-effect-of-pink-arabic-numerals-9-button-png-image_9752-removebg-preview.png")
number_img_rect = number_img.get_rect(center=(300,290))
over_display =pygame.Surface((600,400))
over_display.fill("sky blue")

test_text = pygame.font.Font(None,70)
Life_test_text = pygame.font.Font(None,50)
guess_text = test_text.render("Let's Guess !", False,'white')
guess_text_rect = guess_text.get_rect(center = (300,50))
main_text = test_text.render("Press Number (0 To 9)",False,'white')
main_text_rect=main_text.get_rect(center = (300,100))
secret_num = random.randint(0,10)

instruction_text = test_text.render("Press R-Shift to restart!",False,"orange")
instruction_text_rect = instruction_text.get_rect(center=(300,300))
win_text = ""
guide =""
pressed_num = None
Life = 3

background_sound = pygame.mixer.Sound('empty-mind-93787.mp3')

Life_sound = pygame.mixer.Sound('error-2-126514.mp3')

Right_sound = pygame.mixer.Sound('level-win-6416.mp3')

wrong_sound = pygame.mixer.Sound('failure-2-89169.mp3')

secret_num = random.randint(0,9)
game_active = True

background_sound.play(loops=-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    pressed_num = 0
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -=1

                if event.key == pygame.K_1:
                    pressed_num = 1
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1
                
                if event.key == pygame.K_2:
                    pressed_num = 2
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1

                if event.key == pygame.K_3:
                    pressed_num = 3
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1

                if event.key == pygame.K_4:
                    pressed_num = 4
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1

                if event.key == pygame.K_5:
                    pressed_num = 5
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1

                if event.key == pygame.K_6:
                    pressed_num = 6
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        win_text = "You Won!"
                        Right_sound.play()
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1

                if event.key == pygame.K_7:
                    pressed_num = 7
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1

                if event.key == pygame.K_8:
                    pressed_num = 8
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1

                if event.key == pygame.K_9:
                    pressed_num = 9
                    if pressed_num < secret_num:
                        guide = "You guessed lesser number"
                    if pressed_num > secret_num:
                        guide = "You guessed higher number"
                    if pressed_num == secret_num:
                        Right_sound.play()
                        win_text = "You Won!"
                        game_active=False
                    else :
                        Life_sound.play()
                        Life -= 1

                if Life<=0:
                    wrong_sound.play()
                    win_text ="You Lost!"

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    game_active=True

    if game_active:
        screen.blit(background_img,(0,0))
        pygame.draw.rect(screen,(250,250,250),number_img_rect,0,10)
        pygame.draw.rect(screen,(250,50,90),guess_text_rect,0,10)
        screen.blit(guess_text,guess_text_rect)
        pygame.draw.rect(screen,(50,90,250),main_text_rect,0,10)
        screen.blit(main_text,main_text_rect)
        screen.blit(number_img,number_img_rect)
        game_active = winText()
        secret_num2 = secret_num
        life(Life)
        if guide == "You guessed lesser number":
            guide_less(pressed_num,secret_num)
        if guide == "You guessed higher number":
            guide_high(pressed_num,secret_num)
        
    else: 
        screen.blit(over_display,(0,0))
        secret_num_text = test_text.render(f"Secret Number is:{secret_num2}",False,'brown')
        secret_num_text_rect = secret_num_text.get_rect(center = (300,100)) 
        pygame.draw.rect(screen,'red',secret_num_text_rect,1,5)
        screen.blit(secret_num_text,secret_num_text_rect)
        pygame.draw.rect(screen,"chocolate",instruction_text_rect,1,10)
        screen.blit(instruction_text,instruction_text_rect)
        over_text()
        Life = 3
        pressed_num = 100
        
        guide = ""
        secret_num = random.randint(0,9)

    pygame.display.update()
    clock.tick(60)
            