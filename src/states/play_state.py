from src.states.state import State
import pygame


class PlayState(State):
    def __init__(self):
        self.right = False
        self.left = False
        self.down = False
        self.rotate_right = False
        self.rotate_left = False
        self.drop = False

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



    def render(self, engine, surface):
        pygame.draw.rect(surface, (255, 0, 0), (0, 0, 20, 20))
        for y in range(20):
            for x in range(10):
                if self.grid[x][y]:
                    pass
