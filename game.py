import pygame
import random
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_UNKNOWN
pygame.mixer.init() 
def control(self, x, y):
  pass

#set screen
screen = pygame.display.set_mode((500,400))
screen.fill((164, 164, 164))

#set images and clock
banana = pygame.image.load('imageedit_2_7794499956.png')
monkey = pygame.image.load('imageedit_2_6810712034.png')
missile = pygame.image.load('MISSILE BANAN.png')
jungle = pygame.image.load('Jungle.png')
fire = pygame.image.load('Fire.jpg')
boom_sound = pygame.mixer.Sound('mixkit-fast-game-explosion-1688.wav')
banan_sound = pygame.mixer.Sound('mixkit-arcade-game-jump-coin-216.wav')
clock = pygame.time.Clock()

# render text variables
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 32)
bigfont = pygame.font.SysFont('Comic Sans MS', 40)

#sprite class
class sprite(pygame.sprite.Sprite):
  def __init__(self, image, x, y):
    self.image = image
    self.x = x
    self.y = y

#make sprites
player = sprite(monkey, 200, 180)
banana = sprite(banana, random.randint(50, 450), random.randint(50, 350))
missile = sprite(missile, 0, 500)
background_jungle = sprite(jungle, 0, 0)
background_fire = sprite(fire, 0, 0)
background_jank = sprite(pygame.image.load('Colors.jpeg'), 0, 0)

pygame.mixer.music.load("Child's Nightmare.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

#start page
crashed = False

# display everything

while True:

        #start music
    if 'Godmode' not in globals() or Godmode == True:
        pygame.mixer.music.unload()
        pygame.mixer.music.load("Child's Nightmare.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    #set variables for gamemodes
    Godmode = False
    Jank = False
    Invincibility = False

    while not crashed:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True 
        
        pygame.display.set_caption('Monkey Game')
        screen.fill((164, 164, 164))
        screen.blit(background_jungle.image, (0, 0))
        screen.blit(bigfont.render("Select Difficulty", False, (255, 255, 255)), (130,230))
        screen.blit(font.render("1:Easy 2:Medium 3:Hard", False, (255, 255, 255)), (115, 280))
        screen.blit(font.render("Press F for Godmode", False, (255, 255, 255)), (130, 310))
        screen.blit(player.image, (200, 180 + random.randint(-5, 5)))
        screen.blit(banana.image, (150, 180 + random.randint(-5, 5)))
        screen.blit(banana.image, (280, 180 + random.randint(-5, 5)))
        pygame.display.flip()

        #set speed
        if pygame.key.get_pressed()[pygame.K_1]:
            speed = 10000
            break
        if pygame.key.get_pressed()[pygame.K_2]:
            speed = 2500
            break
        if pygame.key.get_pressed()[pygame.K_3]:
            speed = 10000/9
            break
        if pygame.key.get_pressed()[pygame.K_f]:
            speed = 1000
            Godmode = True
            break
        if pygame.key.get_pressed()[pygame.K_j] and pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_n] and pygame.key.get_pressed()[pygame.K_k]:
            speed = 800
            Godmode = True
            Jank = True
            break
        if pygame.key.get_pressed()[pygame.K_i]:
            Invincibility = True
        if pygame.key.get_pressed()[K_ESCAPE]:
            pygame.quit()
            quit()

    if Godmode == True and Jank == False:
        pygame.mixer.music.unload()
        pygame.mixer.music.load("Ravager.mp3")
        pygame.mixer.music.play(-1)
    elif Jank == True:
        pygame.mixer.music.unload()
        pygame.mixer.music.load("big funky.mp3")
        pygame.mixer.music.play(-1)
    #set variables
    player.x = 200
    player.y = 180
    missile.x = 0
    missile.y = 450
    time = 0
    score = 0
    boolmissile = False
    goback=False
    Jank_y = random.randint(50, 350)
    Jank_x = random.randint(50,450)
    died_bang, died_wall, died_attack = False,False,False

    #gameplay
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True 
        #framerate
        clock.tick(120) 

        #display objects
        pygame.display.set_caption('Monkey Game')
        monkey_x, monkey_y = 180, 180
        screen.fill((164, 164, 164))
        if Godmode == False:
            screen.blit(background_jungle.image, (0, 0))
        elif Jank == False:
            screen.blit(background_fire.image, (0, 0))
        else:
            screen.blit(background_jank.image, (0,0))
        screen.blit(player.image, (player.x, player.y))
        screen.blit(banana.image,(banana.x, banana.y))
        if Jank == True:
            screen.blit(banana.image, (Jank_x, Jank_y))
        if boolmissile == True:
            missile.y -= 1 + time/speed
            screen.blit(missile.image, (missile.x, missile.y))
        screen.blit(font.render("Score: " + str(score), False, (255, 255, 255)),(360, 50))
        screen.blit(font.render("Speed: " + str(format((1000/speed + 1 + time/speed),".2f")), False, (255, 255, 255)),(360, 80))
        screen.blit(font.render("FPS" + str(int(clock.get_fps())), False, (255, 255, 255)), (360, 110))
        pygame.display.flip()

        #movement
        if clock.get_fps() > 10:
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                player.y -= (1000/speed + 1 + time/speed) * 110/clock.get_fps()
            if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
                player.y += (1000/speed + 1 + time/speed)  * 110/clock.get_fps()
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                player.x -= (1000/speed + 1 + time/speed)  * 110/clock.get_fps()
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                player.x += (1000/speed + 1 + time/speed)  * 110/clock.get_fps()    
        #pause function
        esc = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            esc = True
            break

        #banana hit detection
        if ((player.x > banana.x-40) and (player.x < banana.x+10) and (player.y > banana.y-30) and (player.y < banana.y+20) and Jank == False) or ((player.x > banana.x-10) and (player.x < banana.x+10) and (player.y > banana.y-10) and (player.y < banana.y+10) and Jank == True): 
            score += 1
            pygame.mixer.Sound.play(banan_sound)
            banana.x = random.randint(50, 450)
            banana.y = random.randint(50, 350)
            Jank_x = random.randint(50, 450)
            Jank_y = random.randint(50, 350)

        #boundary detection
        if (player.x > 470 or player.x < -40 or player.y > 380 or player.y < -20) and Invincibility == False:
            died_wall = True
            break
        if (player.x > 470 or player.x < -40 or player.y > 380 or player.y < -20) and Invincibility == True:
            if player.x > 470:
                player.x = -40
            if player.x < -40:
                player.x = 470
            if player.y > 380:
                player.y = -20
            if player.y < -20:
                player.y = 380

        #random missile location
        if (random.randint(1, 300) == 1 or Godmode == True) and boolmissile == False:
            missile.x = random.randint(50,400)
            boolmissile = True

        #missile boundary detection
        if (missile.y < -100):
            missile.y = 500
            boolmissile = False
            
        #missile hit detection
        if ((player.x > missile.x+20) and (player.x < missile.x+70) and (player.y > missile.y) and (player.y < missile.y+100) and Jank == False and Invincibility == False) or ((player.x > missile.x-20) and (player.x < missile.x+150) and (player.y > missile.y-50) and (player.y < missile.y+15) and Jank == True and Invincibility == False):
            died_bang = True
            break
        
        #time add
        if time/speed < 4 and Godmode == False:
            time += 1
        elif time/speed < 9 and Godmode == True:
            time += 1.2

        #some jank
        if Jank == True:
            fate = random.randint(1, 3000)
            if fate == 1:
                died_attack = True
                break

    #death screen
    pygame.mixer.Sound.play(boom_sound)
    pygame.display.set_caption('Monkey Game')
    screen.blit(bigfont.render("GAME OVER", False, (255, 255, 255)),(170, 200))
    if died_wall == True:
        screen.blit(bigfont.render("Bumped into a wall", False, (255, 255, 255)),(125, 150))
    if died_attack == True:
        screen.blit(bigfont.render("Had a heart attack", False, (255, 255, 255)),(125, 150))
    if died_bang == True:
        screen.blit(bigfont.render("Went BANG!", False, (255, 255, 255)),(170, 150))
    screen.blit(font.render("Press Enter to Continue", False, (255, 255, 255)), (130, 240))
    pygame.display.flip()


    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True 

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            goback = True
            break

        if pygame.key.get_pressed()[K_ESCAPE] and esc == False:
            goback = False
            break
        if not pygame.key.get_pressed()[K_ESCAPE]:
            esc = False
    #return
    if goback == True:
        continue
    else:
        break


# quit
pygame.quit()
quit()