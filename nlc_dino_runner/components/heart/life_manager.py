from nlc_dino_runner.utils.constants import numbers_life
from nlc_dino_runner.components.heart.life import Life


class LifeManager:
    def __init__(self):
        self.life = numbers_life

    def update(self, game):
        if self.life > 0:
            self.life -= 1

        else:
            game.playing = False

    def draw(self, screen):
        self.screen = screen

        #for life in range(0, self.life):

            #life = Life()

    def reset_obstacles(self):
        self.life
