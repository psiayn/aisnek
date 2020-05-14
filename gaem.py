import pygame 
from random import randint

class SnekGaem:
    def __init__(self, board_width = 400, board_height = 400):
        self.width = board_width
        self.height = board_height
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 102)
        self.black = (0, 0, 0)
        self.red = (215, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("SnekAI")
    
    def snake_init(self):
        x = randint(5, self.width - 5)
        y = randint(5, self.height - 5)
        self.snek = []
        vertical = randint(0,1) == 0 
        for i in range(3):
            point = [x + i, y] if vertical else [x, y + i]
            self.snek.insert(0, point)
    
    def generate_food(self):
        food = []
        while food == []:
            food = [randint(1, self.width), randint(1, self.height)]
            if food in self.snek:
                food = []
        
        self.food = food
    
    def start(self):
        self.snake_init()
        self.generate_food()
        