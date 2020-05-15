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
        self.score = 0
        self.done = False
        self.clock = pygame.time.Clock()
    
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
        self.render_init()
    
    def render_init(self):
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("snek")
        pygame.font.init()
        self.myfont = pygame.font.SysFont('comicsansmc',35)
        self.render()
    
    def render(self):
        self.screen.fill(self.white)
        for i,point in enumerate(self.snek):
            if i == 0:
                pygame.draw.rect(self.screen,self.red,[point[0],point[1],10,10])
            else:
                pygame.draw.rect(self.screen,self.yellow,[point[0],point[1],10,10])

        if self.food is not None:
            pygame.draw.rect(self.screen,self.green,[self.food[0],self.food[1],10,10])
        
        curr_score = "Score " + str(self.score)

        self.textSurf = self.myfont.render(curr_score,False,(0,0,0))
        self.screen.blit(self.textSurf,(1,0))
        pygame.display.update()
        self.clock.tick(20)

    def create_new_point(self,key):
        new_point = [self.snek[0][0],self.snek[0][1]]
        if key == 0:
            new_point[1] -= 10
        elif key == 1:
            new_point[1] += 10
        elif key == 2:
            new_point[0] -= 10
        elif key == 3:
            new_point[0] += 10
        self.snek.insert(0,new_point)

    def remove_last_point(self):
        self.snek.pop()        

    def step(self,key):
        """
            CONTROLS :
            0 - UP
            1 - DOWN
            2 - LEFT
            3 - RIGHT
        """
        self.create_new_point(key)
        if self.done == True:
            self.end_game()

        if self.food_eaten():
            self.score += 1
            self.generate_food()
        else:
            self.remove_last_point()
        
        self.check_collisions()
        self.render()
        return self.generate_observations()

    def food_eaten(self):
        return self.snek[0] == self.food

    def check_collisions(self):
        if(self.snek[0][0] <= 5 or 
            self.snek[0][0] >= self.width - 5 or
            self.snek[0][1] <= 5 or
            self.snek[0][1] >= self.height - 5 or
            self.snek[0] in self.snek[1:-1]):
            self.done = True

    def generate_observations(self):
        return self.done, self.score, self.snek, self.food

    def end_game(self):
        pygame.quit()

if __name__ == "__main__":
    game = SnekGaem()
    game.start()
    print("Gaem Start")
    while(True):
        print(game.step(randint(0,3)))