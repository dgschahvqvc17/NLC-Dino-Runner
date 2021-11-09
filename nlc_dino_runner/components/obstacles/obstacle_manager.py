class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
