import random

from nlc_dino_runner.components.obstacles.obstacle_large_cactus import ObstacleLargeCactus


class LargeCactus(ObstacleLargeCactus):
    def __init__(self, image):
        self.index = random.randint(0, 2)
        super().__init__(image, self.index)
        self.rect.y = 310
