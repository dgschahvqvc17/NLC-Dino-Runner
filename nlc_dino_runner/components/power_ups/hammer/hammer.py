import random

from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HAMMER, SCREEN_HEIGHT, HAMMER_TYPE


class Hammer(Sprite):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)

    def update(self, game_speed, hammer):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            hammer.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
