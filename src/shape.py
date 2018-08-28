import random


class Shape:
    last_shape = -1

    def __init__(self, grid):
        self.x = 5
        self.y = 0
        self.color = (255, 0, 0)
        self.grid = grid

        self.nodes = self.load_shape()

    def move(self, x_move, y_move):
        if self.grid.can_move(self, x_move, 0):
            self.x += x_move
        if self.grid.can_move(self, 0, y_move):
            self.y += y_move

    @staticmethod
    def load_shape():
        while True:
            random_shape = random.randint(0, len(ShapeDefinitions.Shapes))
            if random_shape == Shape.last_shape:
                continue
            Shape.last_shape = random_shape
            return ShapeDefinitions.Shapes[random_shape]


class ShapeDefinitions:
    Shapes = [
        ((255, 0, 0), [(1, 0), (1, 1), (1, 2), (1, 3)]),
        ((0, 255, 0), [(1, 0), (0, 1), (1, 1), (2, 1)])
    ]

