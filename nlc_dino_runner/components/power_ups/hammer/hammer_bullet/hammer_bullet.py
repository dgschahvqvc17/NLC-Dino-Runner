import pygame
from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import HAMMER_TYPE, HAMMER


class HammerBullet(Sprite):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)
        super().__init__()
