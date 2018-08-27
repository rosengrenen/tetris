import copy
import random
import pygame

from src.grid import Grid
from src.states.state import State
from src.shape import Shape
from src.point import Point
from src.colour import Colour


class PlayState(State):
    shape_variations = [
        (Colour(0, 240, 240), [Point(0, 1), Point(1, 1), Point(2, 1), Point(3, 1)]),  # I BLOCK
        (Colour(240, 0, 0), [Point(0, 1), Point(1, 1), Point(1, 2), Point(2, 2)]),  # Z BLOCK
        (Colour(0, 240, 0), [Point(0, 2), Point(1, 2), Point(1, 1), Point(2, 1)]),  # S BLOCK
        (Colour(0, 0, 240), [Point(0, 1), Point(1, 1), Point(2, 1), Point(2, 2)]),  # J BLOCK
        (Colour(240, 160, 0), [Point(0, 1), Point(1, 1), Point(2, 1), Point(2, 0)]),  # L BLOCK
        (Colour(160, 0, 240), [Point(0, 1), Point(1, 1), Point(2, 1), Point(1, 0)]),  # T BLOCK
        (Colour(240, 240, 0), [Point(1, 1), Point(1, 2), Point(2, 1), Point(2, 2)])  # O BLOCK
    ]

    def __generate_next_shapes(self):
        for index in range(len(self.next_shapes), 4):
            while True:
                number = random.randint(0, len(PlayState.shape_variations) - 1)
                if number not in self.next_shape_indices:
                    break
            self.next_shapes.append(Shape(Point(5, 0), PlayState.shape_variations[number][0],
                                          copy.deepcopy(PlayState.shape_variations[number][1])))
            self.next_shape_indices.append(number)
            for i in range(random.randint(0, 4)):
                self.next_shapes[index].rotate_right()

    def __init__(self):
        self.grid_size = 30
        self.grid = Grid(10, 20)
        self.time_since_last_drop = 0
        self.level = 0
        self.score = 0

        self.next_shapes = []
        self.next_shape_indices = []

        self.shape = None
        self.__generate_next_shapes()
        self.shape = self.next_shapes[0]
        del self.next_shapes[0]
        del self.next_shape_indices[0]
        self.__generate_next_shapes()

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
        if self.left:
            if self.grid.can_move(self.shape, -1, 0):
                self.shape.position.x -= 1
        if self.right:
            if self.grid.can_move(self.shape, 1, 0):
                self.shape.position.x += 1
        if self.rotate_right:
            self.shape.rotate_right()
            if self.grid.can_move(self.shape, 0, 0):
                pass
            elif self.grid.can_move(self.shape, 1, 0):
                self.shape.position.x += 1
            elif self.grid.can_move(self.shape, -1, 0):
                self.shape.position.x -= 1
            elif self.grid.can_move(self.shape, 2, 0):
                self.shape.position.x += 2
            elif self.grid.can_move(self.shape, -2, 0):
                self.shape.position.x -= 2
            else:
                self.shape.rotate_left()
        if self.rotate_left:
            self.shape.rotate_left()
            if self.grid.can_move(self.shape, 0, 0):
                pass
            elif self.grid.can_move(self.shape, 1, 0):
                self.shape.position.x += 1
            elif self.grid.can_move(self.shape, -1, 0):
                self.shape.position.x -= 1
            elif self.grid.can_move(self.shape, 2, 0):
                self.shape.position.x += 2
            elif self.grid.can_move(self.shape, -2, 0):
                self.shape.position.x -= 2
            else:
                self.shape.rotate_right()
        if self.drop:
            while self.grid.can_move(self.shape, 0, 1):
                self.shape.position.y += 1
                self.score += 1

        self.time_since_last_drop += delta_time
        drops_per_second = 4 + self.level
        drop_interval = 1000 / drops_per_second
        increased_drop_speed_multiplier = 6
        increased_drop_interval = drop_interval / increased_drop_speed_multiplier

        if self.time_since_last_drop > drop_interval or (
                self.time_since_last_drop > increased_drop_interval and self.down):
            if self.down:
                self.time_since_last_drop -= increased_drop_interval
            else:
                self.time_since_last_drop -= drop_interval

            if self.grid.can_move(self.shape, 0, 1):
                if self.down:
                    self.score += 1
                self.shape.position.y += 1
            else:
                self.grid.add_shape(self.shape)
                self.shape = self.next_shapes[0]
                del self.next_shapes[0]
                del self.next_shape_indices[0]
                self.__generate_next_shapes()

        cleared_rows = self.grid.clear_rows()

    def render(self, engine, surface):
        white = Colour(255, 255, 255)
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                if self.grid[x][y]:
                    pygame.draw.rect(surface, self.grid[x][y].darken(20),
                                     (x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size))
                    pygame.draw.rect(surface, self.grid[x][y].get(),
                                     (x * self.grid_size + 1, y * self.grid_size + 1, self.grid_size - 2,
                                      self.grid_size - 2))
                else:
                    pygame.draw.rect(surface, white.darken(10),
                                     (x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size))
                    pygame.draw.rect(surface, white.get(),
                                     (x * self.grid_size + 1, y * self.grid_size + 1, self.grid_size - 2,
                                      self.grid_size - 2))

        for node in self.shape.nodes:
            pygame.draw.rect(surface, self.shape.colour.darken(20), (
                (self.shape.position.x + node.x) * self.grid_size, (self.shape.position.y + node.y) * self.grid_size,
                self.grid_size, self.grid_size))
            pygame.draw.rect(surface, self.shape.colour.get(), (
                (self.shape.position.x + node.x) * self.grid_size + 1,
                (self.shape.position.y + node.y) * self.grid_size + 1,
                self.grid_size - 2, self.grid_size - 2))

        y_offset = 0
        while self.grid.can_move(self.shape, 0, y_offset + 1):
            y_offset += 1

        for node in self.shape.nodes:
            pygame.draw.rect(surface, self.shape.colour.get(), (
                (self.shape.position.x + node.x) * self.grid_size,
                (self.shape.position.y + node.y + y_offset) * self.grid_size,
                self.grid_size, self.grid_size))
            pygame.draw.rect(surface, self.shape.colour.lighten(50), (
                (self.shape.position.x + node.x) * self.grid_size + 1,
                (self.shape.position.y + node.y + y_offset) * self.grid_size + 1,
                self.grid_size - 2, self.grid_size - 2))

        offset = 1
        for shape in self.next_shapes:
            x_min = 100
            x_max = 0
            y_min = 100
            y_max = 0
            for node in shape.nodes:
                if node.x > x_max:
                    x_max = node.x
                if node.x < x_min:
                    x_min = node.x
                if node.y > y_max:
                    y_max = node.y
                if node.y < y_min:
                    y_min = node.y
            height = y_max - y_min
            for node in shape.nodes:
                pygame.draw.rect(surface, shape.colour.darken(20), (
                    (self.grid.width + node.x - x_min + 1) * self.grid_size,
                    (node.y + offset - y_min) * self.grid_size,
                    self.grid_size, self.grid_size))
                pygame.draw.rect(surface, shape.colour.get(), (
                    (self.grid.width + node.x - x_min + 1) * self.grid_size + 1,
                    (node.y + offset - y_min) * self.grid_size + 1,
                    self.grid_size - 2, self.grid_size - 2))
            offset += height + 2
