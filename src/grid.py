class Grid:
    def __init__(self, width, height, cell_size):
        self.size = cell_size
        self.width = width
        self.height = height
        self.grid = [[None for y in range(self.height)] for x in range(width)]

    def get_coordinate(self, value):
        return value * self.size

    def lock_shape(self):
        pass

    def can_move(self, shape, x_offset, y_offset):
        pass


