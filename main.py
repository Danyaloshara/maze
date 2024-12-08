import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Лабіринт')

background = pygame.transform.scale(pygame.image.load('background.jpg'), (800,600))

running = True
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()

kick = pygame.mixer.Sound('kick.ogg')
money = pygame.mixer.Sound('money.ogg')

class GameStrite(pygame.sprite.Sprite):
    def __init__(self, image, x ,y , speed):
        self.image = pygame.transform.scale(pygame.image.load(), (64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = x
        self.speed = speed

    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

hero = GameStrite('hero.png', 100,100,5)
enemy = GameStrite('cyborg.png',200,200,10)
treasure = GameStrite('treasure.png',500,500,0)

while running:
    window.blit(background, (0,0))

    hero.render()
    enemy.render()
    treasure.render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()
    clock.tick(240)

pygame.quit()