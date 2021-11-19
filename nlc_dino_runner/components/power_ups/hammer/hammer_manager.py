import random
import pygame

from nlc_dino_runner.components.power_ups.hammer.army import Hammer


class HammerManager:
    def __init__(self):
        self.hammer = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))

    def reset_power_ups(self, points):
        self.hammer = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.hammer) == 0:
            if self.when_appears == self.points:
                print("generating hammer")
                self.when_appears = random.randint(self.when_appears + 200, 300 + self.when_appears)
                self.hammer.append(Hammer())
        return self.hammer

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for hammer in self.hammer:
            hammer.update(game_speed, self.hammer)
            if player.dino_rect.colliderect(hammer.rect):
                hammer.start_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = hammer.type
                hammer.start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.hammer_time_up = hammer.start_time + (time_random * 1000)
                self.hammer.remove(hammer)

    def draw(self, screen):
        for hammer in self.hammer:
            hammer.draw(screen)


