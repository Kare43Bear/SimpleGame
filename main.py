# This game demonstrates objects, pygame and key input
import pygame
import sys


# Player class for the players
class Player:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.speed = 1
        self.size = (50, 100)
        self.image = pygame.image.load("pez.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)

    def moveLeft(self):
        self.x = self.x - self.speed
        self.rect.update(self.x, self.y, self.size[0], self.size[1])

    def moveRight(self):
        self.x = self.x + self.speed
        self.rect.update(self.x, self.y, self.size[0], self.size[1])

    def moveUp(self):
        self.y = self.y - self.speed
        self.rect.update(self.x, self.y, self.size[0], self.size[1])

    def moveDown(self):
        self.y = self.y + self.speed
        self.rect.update(self.x, self.y, self.size[0], self.size[1])


# Candy class for the candy (coins, rewards, food)
class Candy:
    def __init__(self):
        self.x = 300
        self.y = 50
        self.size = (50, 50)
        self.image = pygame.image.load("candy.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)

    def checkCollision(self, sprite1):
        col = self.rect.colliderect(sprite1.rect)
        if col == True:
            self.rect = self.rect.move(1000, 1000)


# main
clock = pygame.time.Clock()
p1 = Player()
candy1 = Candy()
pygame.init()
win = pygame.display.set_mode((500, 500))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p1.moveLeft()
    if keys[pygame.K_RIGHT]:
        p1.moveRight()
    if keys[pygame.K_UP]:
        p1.moveUp()
    if keys[pygame.K_DOWN]:
        p1.moveDown()

    # check collision
    candy1.checkCollision(p1)

    win.fill((255, 255, 255))
    win.blit(p1.image, p1.rect)
    win.blit(candy1.image, candy1.rect)
    pygame.display.update()