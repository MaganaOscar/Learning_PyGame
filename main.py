import pygame, sys, random
from pygame.locals import *

pygame.init()

#assign fps a value
FPS = 60
FramePerSec = pygame.time.Clock()

#setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#set up a 300x300 pixel display with caption
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Creating lines and shapes
# pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
# pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
# pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
# pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
# pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
# pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
# pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Materials/Enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40,360), 0))
    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30,370), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Materials/Player.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect()

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()
#game loop 
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()

    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
