import math
import pygame 
from pygame import mixer
class player():
    x=None
    y=None
    img=None
    chan=None
    helth=None
    def __init__(self,x1,y1,img) :
        self.x=x1
        self.y=y1
        self.chan=0
        self.img= pygame.image.load(img)
        self.helth=5
    def dep (self):
        self.y+=self.chan
        if self.y <= 0:
            self.y = 0
        elif self.y >= 536:
            self.y = 536
class missile():
    x=None
    y=None
    img=None
    stat=None
    def __init__(self,x1,y1,img,stat1) :
        self.x=x1
        self.y=y1
        self.stat=stat1
        self.img= pygame.image.load(img)
    def fire (self,x1):
        if self.stat==False:
            self.x+=x1
        if self.x <= -30 or self.x>820 :
            self.stat=True
def aff_player(img,x,y):
    screen.blit(img, (x, y))
def aff_missile(img,x,y,stat):
    if not stat:    
        screen.blit(img, (x, y))
def collision (x,y,x1,Y1,stat):
    if not stat:
        distance = math.sqrt(math.pow(x - x1, 2) + (math.pow(y - Y1, 2)))
        if distance < 27:
            return True
        else:
            return False      
def show_helth(font,helth,x, y,nom_player,color):
    score = font.render(nom_player + str(helth), True, (color))
    screen.blit(score, (x, y))
def game_over(message,color):
    over_text = over_font.render(message, True, (color))
    screen.blit(over_text, (180, 250))
def start_game():
    start_text = start_font.render('PRESS ANY BUTTON TO START', True, (255, 255, 255))
    screen.blit(start_text, (150, 250))

pygame.init()
screen = pygame.display.set_mode((800, 600))
back = pygame.image.load('back.png')
pygame.display.set_caption("Projet Semestriel")
log = pygame.image.load('icon.png')
pygame.display.set_icon(log)

p1=player(735,280,'red.png')
p2=player(0,280,'green.png')
m1=missile(735,280,'missile1.png',True)
m2=missile(0,280,'missile1.png',True)
font = pygame.font.Font('freesansbold.ttf', 32)
start_font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
green = (0, 255, 0)
red = (255, 0, 0)

mixer.music.load("background.wav")
mixer.music.play(-1)
run=True
while run :
    message=''
    in_game=False
    end_game=False
    screen.fill((0, 0, 0))
    screen.blit(back, (0, 0))
    start_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            in_game=True
    p1.__init__(735,280,'red.png')
    p2.__init__(0,280,'green.png')
    m1.__init__(735,280,'missile1.png',True)
    m2.__init__(0,280,'missile1.png',True)
    while in_game :
        screen.fill((0, 0, 0))
        screen.blit(back, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game=False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p1.chan=-1
                if event.key == pygame.K_DOWN:
                    p1.chan=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    p2.chan=-1
                if event.key == pygame.K_s:
                    p2.chan=1  
                if event.key == pygame.K_RCTRL:
                    if m1.stat:
                        m1.__init__(p1.x+10,p1.y+20,'missile1.png',False)
                        Sound = mixer.Sound("laser.wav")
                        Sound.play()
                if event.key == pygame.K_LCTRL:
                    if m2.stat:
                        m2.__init__(p2.x+10,p2.y+20,'missile2.png',False)
                        Sound = mixer.Sound("laser.wav")
                        Sound.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_z:
                    p1.chan = 0
                    p2.chan = 0 
        p1.dep()
        p2.dep() 
        m1.fire(-2)  
        m2.fire(2)  
        aff_player(p1.img,p1.x,p1.y)
        aff_player(p2.img,p2.x,p2.y)
        aff_missile(m1.img,m1.x,m1.y,m1.stat)
        aff_missile(m2.img,m2.x,m2.y,m2.stat)
        if collision(p1.x,p1.y,m2.x,m2.y,m2.stat):
            bulletSound = mixer.Sound("explosion.wav")
            bulletSound.play()
            p1.helth=p1.helth-1
            m2.stat=True
        if collision(p2.x,p2.y,m1.x,m1.y,m1.stat):
            bulletSound = mixer.Sound("explosion.wav")
            bulletSound.play()
            p2.helth=p2.helth-1
            m1.stat=True
        if p1.helth <= 0:
            message='PLAYER 2 WIN'
            color=green
            in_game=False
            end_game=True
            break
        if p2.helth <= 0:
            message='PLAYER 1 WIN'
            in_game=False
            end_game=True
            color=red
            break
        show_helth(font,p1.helth,600,20,'player 1: ',red)
        show_helth(font,p2.helth,20,20, 'player 2: ',green)
        pygame.display.update()
    
    while end_game :
        screen.fill((0, 0, 0))
        screen.blit(back, (0, 0))
        game_over(message,color)
        start_text = start_font.render('PRESS ANY BUTTON TO RSTART', True, (255, 255, 255))
        screen.blit(start_text, (150, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game=False
                run = False
                end_game=False
            if event.type == pygame.KEYDOWN:
                in_game=True
                end_game=False
        pygame.display.update()
    pygame.display.update()
    