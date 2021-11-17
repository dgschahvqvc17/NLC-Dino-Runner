from nlc_dino_runner.components.obstacles.obstacle import Obstacle
import random

from nlc_dino_runner.utils.constants import BIRD


class DinoBird(Obstacle):
    def __init__(self, image):
        self.run_img = BIRD
        self.index = random.randint(0, 2)
        super().__init__(image, self.index)
        self.rect.y = 328