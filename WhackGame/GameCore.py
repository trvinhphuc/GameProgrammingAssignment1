import pygame
import random
import Resource.AnimationCreator as ANIM

###### TYPES ##################

#struct Enemy{
# posX, posY
# animation (start | mid | end)
# timing [ ENTRANCE | END ] -> state length
# start_time_tamp
# current_state : 0 start | 1 mid | 2 end | 3 die | 4: DELETED
#}
#Enemy = namedtuple("Enemy", "positionX positionY animation timing start_time current_state")

class Enemy:
    def __init__(self, ppositionX, ppositionY, panimation, ptiming, pstart_time, pcurrent_state):
        self.positionX = ppositionX
        self.positionY = ppositionY
        self.animation = panimation
        self.timing = ptiming
        self.start_time = pstart_time
        self.current_state = pcurrent_state
        
    positionX = 0
    positionY = 0 
    animation = 0
    timing = 0
    start_time = 0
    current_state = 0

m_enemy_list = []

###### CONSTANT ##############

SPAWN_RATE = 0.1 # spawn per second

# EX: SPAWN_RATE = 0.2
# CALCULATE : 0.2 (20%) for each second -> 5s == 100 percent spawn
# RATE = ElapseTime (ms) * SPAWN_RATE / 1000 x 100 (%)
#

base_time_stamp = 0

###### VARIABLES ##############
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480



size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

def initGame():
    
    
    pygame.display.set_caption("My gamme")

def testfunc():
    print "hehhehe"
    
def render():
    
    screen.fill((0x00, 0x00, 0x00))
    pygame.draw.rect(screen, (0x00, 0xFF, 0x00), [55, 50, 20, 25])
    
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("My text",True,(0xFF, 0xFF, 0xFF))

    screen.blit(text, [250, 250])
    
    schedule()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
def schedule():
    ################ DEFINITIONS
    
    global base_time_stamp
    
    ################ SPAWN CALCULATION
    
    elapse_time_from_last_spawn = pygame.time.get_ticks() - base_time_stamp
    spawn_rate = SPAWN_RATE * elapse_time_from_last_spawn / 10.0
    rate = random.randint(0, 100)
    
    if rate <= spawn_rate:
        spawnMonster(0)
        base_time_stamp = pygame.time.get_ticks()
    
    ################ HANDLE
    for enemy in m_enemy_list:
        if enemy.current_state == 0: ### SPAWN
            enemy.animation[0].blit(screen, (enemy.positionX, enemy.positionY))
            if enemy.timing[0] < (pygame.time.get_ticks() - enemy.start_time):
                enemy.current_state = 1
                enemy.animation[0].stop()
                enemy.animation[1].play()
                enemy.start_time = pygame.time.get_ticks()
        if enemy.current_state == 1: ### WAIT
            enemy.animation[1].blit(screen, (enemy.positionX, enemy.positionY))    
            if enemy.timing[1] < (pygame.time.get_ticks() - enemy.start_time): #### TIME OUT ####
                enemy.current_state = 2
                enemy.animation[1].stop()
                enemy.animation[2].play()
                enemy.start_time = pygame.time.get_ticks()
        if enemy.current_state == 2: ### ESCAPE 
            enemy.animation[2].blit(screen, (enemy.positionX, enemy.positionY))    
            if enemy.timing[2] < (pygame.time.get_ticks() - enemy.start_time): #### TIME OUT ####
                enemy.current_state = 4
                enemy.animation[2].stop()
                m_enemy_list.remove(enemy)
    
def spawnMonster(code):
    if code == 0:
        posX = random.randint(0, SCREEN_WIDTH)
        posY = random.randint(0, SCREEN_HEIGHT)

        
        new_enemy = Enemy(
                          posX, 
                          posY, 
                          (ANIM.getBoltanim(), ANIM.getFlameanim(), ANIM.getSmokeanim()),
                          (900, 2000, 900),
                          pygame.time.get_ticks(),
                          0 )
        new_enemy.animation[0].play()
        m_enemy_list.append(new_enemy)
    