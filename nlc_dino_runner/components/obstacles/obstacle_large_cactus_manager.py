import pygame.time

from nlc_dino_runner.components.obstacles.large_cactus import LargeCactus
from nlc_dino_runner.utils.constants import LARGE_CACTUS, numbers_life


class LargeObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(LargeCactus(LARGE_CACTUS))

        for obstacle_large_cactus in self.obstacles:
            obstacle_large_cactus.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle_large_cactus.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle_large_cactus)
                elif game.lifes > 0:
                    self.obstacles.remove(obstacle_large_cactus)
                    game.lifes -= 1
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break

    def draw(self, screen):
        for obstacle_large_cactus in self.obstacles:
            obstacle_large_cactus.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
