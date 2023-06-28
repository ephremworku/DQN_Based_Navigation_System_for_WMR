import gym
from gym import spaces
import numpy as np
from gym_game.envs.Environment import Environ


class CustomEnv(gym.Env):
    # metadata = {'render.modes' : ['human']}
    def __init__(self):
        self.pygame = Environ()
        self.action_space = spaces.Discrete(3)
        low = np.zeros(30)  # Lower bound of 0 for each element
        high = np.ones(30) * 100  # Upper bound of 100 for each element

        # Create the observation space
        self.observation_space = spaces.Box(low, high, dtype=np.int)

        # self.observation_space = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([10, 10, 10, 10, 10]), dtype=np.int)

    def reset(self):
        del self.pygame
        self.pygame = Environ()
        # obstacles = environment.sense_obstacles()
        self.pygame.screen.fill((255, 255, 255))
        self.pygame.obstacles()
        self.pygame.sense_obstacles()
        # using circles detect the collision
        self.pygame.collisionDetectorCircles()
        self.pygame.movement()
        # sensing the obstacle
        self.pygame.action(0)
        obs = self.pygame.observe()
        return obs

    def step(self, action):
        self.pygame.is_alive = True
        # obstacles = environment.sense_obstacles()
        self.pygame.screen.fill((255, 255, 255))
        self.pygame.obstacles()
        self.pygame.sense_obstacles()
        # using circles detect the collision
        self.pygame.collisionDetectorCircles()
        self.pygame.movement()
        # sensing the obstacle
        self.pygame.action(action)
        # using circles detect the collision
        # self.pygame.collisionDetectorCircles()
        obs = self.pygame.observe()
        reward = self.pygame.evaluate()
        done = self.pygame.is_done()
        return obs, reward, done, {}

    def render(self, mode="human", close=False):
        self.pygame.view()
