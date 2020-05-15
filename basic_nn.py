from gaem import SnekGaem
from random import randint 
import numpy as np 
import torch 
import math 
from statistics import mean 
from collections import Counter

class SnekNN:
    def __init__(self, inital_games = 100, test_games = 100, goal_steps = 100, lr = 1e-2, filename="snek_nn.pt"):
        self.intial_games = inital_games
        self.test_games = test_games
        self.goal_steps = goal_steps
        self.lr = lr 
        self.filename = filename
        self.vectors_and_keys = [
            [[-10, 0], 0],
            [[10, 0], 1],
            [[0, -10], 2],
            [[0, 10], 3]
        ]
    
    def initial_population(self):
        training_data = [] 
        for _ in range(self.intial_games):
            game = SnekGaem()
            _, _, snek, _ = game.start()
            prev_observation = self.generate_observation(snek,game)
            for _ in range(self.goal_steps):
                action, game_action = self.generate_action(snek)
    
    def generate_action(self, snek):
        action = randint(0, 2) - 1
        return action, self.get_game_action(snek, action)
    
    def generate_observation(self, snek, game):
        return np.array([int(i) for i in game.detect_obstacles()])

    
    def get_snek_direction_vector(self, snek):
        return np.array(snek[0]) - np.array(snek[1])

    def get_game_action(self, snek, action):
        snek_direction = self.get_snek_direction_vector(snek)
        new_direction = snek_direction
        if action == -1:
            new_direction 
    
    def turn_vector_to_the_left(self, snek_direction):
        return 