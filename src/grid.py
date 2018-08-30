class Grid:
    def __init__(self, width, height, cell_size):
        self.size = cell_size
        self.width = width
        self.height = height
        self.grid = [[None for y in range(self.height)] for x in range(width)]

    def get_coordinate(self, value):
        return value * self.size

    def lock_shape(self, shape):
        for node in shape.nodes:
            self.grid[shape.x + node.x][shape.y + node.y] = shape.color


    def can_move(self, shape, x_offset, y_offset):
        for node in shape.nodes:
            node_offset_x = shape.x + node.x + x_offset
            node_offset_y = shape.y + node.y + y_offset
            if node_offset_x > self.width or node_offset_x < 0:
                return False
            if node_offset_y > self.height:
                return False
            if self.grid[node_offset_x][node_offset_y]:
                return False

        return True;
