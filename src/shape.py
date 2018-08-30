import random

from src.utils import Point


class Shape:
    Last_shape = -1

    def __init__(self, grid):
        self.x = 5
        self.y = 0
        self.color = (0, 0, 0)
        self.grid = grid
        loaded_shape = self.load_shape()

        self.color = loaded_shape[0]
        self.nodes = loaded_shape[1]

    def move_down(self):
        if self.grid.can_move(self, 0, 1):
            self.y += 1
         # else





    def move(self, x_move, y_move):
        if self.grid.can_move(self, x_move, 0):
            self.x += x_move
        if self.grid.can_move(self, 0, y_move):
            self.y += y_move

    def get_node_coordinate(self, point):
        return Point((self.x + point.x) * 20, (self.y + point.y) * 20)

    @staticmethod
    def load_shape():
        while True:
            random_shape = random.randint(0, len(ShapeDefinitions.Shapes) - 1)
            if random_shape == Shape.Last_shape:
                continue
            Shape.Last_shape = random_shape
            return ShapeDefinitions.Shapes[random_shape]


class ShapeDefinitions:
    Shapes = [
        ((255, 0, 0), (Point(1, 0), Point(1, 1), Point(1, 2), Point(1, 3))),
        ((0, 255, 0), (Point(1, 0), Point(0, 1), Point(1, 1), Point(2, 1))),
        ((0, 0, 255), (Point(1, 0), Point(0, 1)))
    ]

