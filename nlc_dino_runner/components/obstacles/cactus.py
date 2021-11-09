from nlc_dino_runner.utils.constants import SMALL_CACTUS[0]
from nlc_dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):

    def __init__(self, image):
        self.image_cactus = SMALL_CACTUS[0]
        super().__init__(self.image_cactus)
        self.rect.y = 250