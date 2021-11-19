import pygame.time

from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.utils.constants import BIRD, numbers_life


class ObstacleBirdManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Bird(BIRD))

        for obstacle_bird in self.obstacles:
            obstacle_bird.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle_bird.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle_bird)
                elif game.lifes > 0:
                    self.obstacles.remove(obstacle_bird)
                    game.lifes -= 1
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break

    def draw(self, screen):
        for obstacle_bird in self.obstacles:
            obstacle_bird.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
