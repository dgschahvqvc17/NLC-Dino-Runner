from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART


class Life(Sprite):
    def __init__(self):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 10

    #def update(self, game_speed,):
        #self.rect.x = game_speed

        #if self.rect.x < -self.rect.width:
            #powerups.pop()
    def coordinates(self, lives):
        self.rect.x += 25
        if self.rect.x == 25+25*lives:
            self.rect.x = 25

    def draw(self, screen):
        screen.blit(self.image, self.rect)
