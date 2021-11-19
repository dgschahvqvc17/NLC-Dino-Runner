import pygame

from nlc_dino_runner.components import dinosaur

from nlc_dino_runner.components.heart.life import Life
from nlc_dino_runner.components.heart.life_manager import LifeManager
from nlc_dino_runner.components.obstacles.obstacle_large_cactus_manager import LargeObstacleManager
from nlc_dino_runner.components.ornaments.cloud import Cloud
from nlc_dino_runner.components.power_ups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from nlc_dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITTLE, FPS, numbers_life
from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.components.power_ups.hammer.hammer import Hammer
from nlc_dino_runner.components.power_ups.hammer.hammer_manager import HammerManager
from nlc_dino_runner.components.obstacles.obstacle_bird_manager import ObstacleBirdManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.cloud = Cloud()
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.obstacle_bird_manager = ObstacleBirdManager()
        self.obstacle_large_cactus_manager = LargeObstacleManager()
        self.hammer = Hammer()
        self.hammer_manager = HammerManager()
        #self.dino_bird_manager = DinoBirdManager()
        self.life = Life()
        self.life_manager = LifeManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.lifes = numbers_life

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rec = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rec)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        half_width = SCREEN_WIDTH // 2
        half_height = SCREEN_HEIGHT // 2
        if self.death_count == 0:
            text_element, text_element_rec = text_utils.get_centered_message("Press any key to Start ")
            self.screen.blit(text_element, text_element_rec)
            text_element, text_element_rec = text_utils.get_centered_message("Your Score :  " + str(self.points), height=half_height + 40)
            self.screen.blit(text_element, text_element_rec)

        elif self.death_count > 0:
            text_element, text_element_rec = text_utils.get_centered_message("Press any key to Restart ")
            self.screen.blit(text_element, text_element_rec)
            text_element, text_element_rec = text_utils.get_centered_message("Your Score :  " + str(self.points), height = half_height + 40)
            self.screen.blit(text_element, text_element_rec)
            text_element, text_element_rec = text_utils.get_centered_message("Death Count :  " + str(self.death_count), height = half_height + 80)
            self.screen.blit(text_element, text_element_rec)
        self.screen.blit(ICON, (half_width - 40, half_height - 150))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.points = 0
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                self.lifes = numbers_life

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.hammer_manager.update(self.points, self.game_speed, self.player)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.obstacle_bird_manager.update(self)
        self.obstacle_large_cactus_manager.update(self)
        self.cloud.update(self. game_speed)
        for x in range(0, self.lifes):
            self.life.draw(self.screen)
            self.life.coordinates(self.lifes)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.hammer_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.obstacle_bird_manager.draw(self.screen)
        self.obstacle_large_cactus_manager.draw(self.screen)
        self.life.draw(self.screen)
        self.cloud.draw(self.screen)

    def draw_background(self):
        image_with = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_with:
            self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

