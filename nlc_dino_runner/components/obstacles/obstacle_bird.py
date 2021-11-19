from nlc_dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite
import random
from nlc_dino_runner.utils.constants import SCREEN_HEIGHT


class ObstacleBird(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        #self.rect.x = SCREEN_WIDTH
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed * 1.3
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

