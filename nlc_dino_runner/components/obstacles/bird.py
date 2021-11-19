from nlc_dino_runner.components.obstacles.obstacle_bird import ObstacleBird
import random


class Bird(ObstacleBird):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.index = random.randint(0, 2)
        self.rect.y = 230
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 7:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
