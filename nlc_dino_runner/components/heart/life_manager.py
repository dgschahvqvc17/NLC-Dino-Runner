class LifeManager:
    def __init__(self):
        self.life = 3

    def update(self, game):
        if self.life > 0:
            self.life -= 1

        else:
            game.playing = False

    def draw(self, screen):
        for life in range(0, self.life):
            
            life = Life()

    def reset_obstacles(self):
        self.life
