from src.grid import Grid
from src.shape import Shape
from src.states.state import State
import pygame

from src.utils import Point


class PlayState(State):
    def __init__(self):
        self.right = False
        self.left = False
        self.down = False
        self.rotate_right = False
        self.rotate_left = False
        self.drop = False

        self.grid = Grid(10, 20, 20)
        self.shape = Shape(self.grid)

    def reset_input(self):
        self.right = False
        self.left = False
        self.down = False
        self.rotate_right = False
        self.rotate_left = False
        self.drop = False

    def input(self, engine, events):
        self.reset_input()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.left = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.right = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.down = True
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_x:
                    self.rotate_right = True
                if event.key == pygame.K_z:
                    self.rotate_left = True
                if event.key == pygame.K_SPACE:
                    self.drop = True

    def update(self, engine, delta_time):
        if self.drop:
            self.shape.color = self.shape.load_shape()[0]
            self.shape.nodes = self.shape.load_shape()[1]
            self.drop = False

    def render(self, engine, surface):
        # for y in range(20):
        #     for x in range(10):
        #         if self.grid[x][y]:
        #             pass

        for cell in self.shape.nodes:
            pygame.draw.rect(
                surface,
                self.shape.color,
                (
                    self.shape.get_node_coordinate(cell).x,
                    self.shape.get_node_coordinate(cell).y,
                    20,
                    20
                ),
                0)

