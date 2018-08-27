class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for y in range(height)] for x in range(width)]

    def __getitem__(self, item):
        return self.grid[item]

    def can_move(self, shape, x_offset, y_offset):
        for node in shape.nodes:
            if shape.position.x + node.x + x_offset < 0:
                return False
            if shape.position.x + node.x + x_offset >= self.width:
                return False
            if shape.position.y + node.y + y_offset < 0:
                return False
            if shape.position.y + node.y + y_offset >= self.height:
                return False
            if self[shape.position.x + node.x + x_offset][shape.position.y + node.y + y_offset]:
                return False
        return True

    def add_shape(self, shape):
        for node in shape.nodes:
            self[shape.position.x + node.x][shape.position.y + node.y] = shape.colour

    def clear_rows(self):
        cleared_rows = 0
        for y in range(self.height):
            flag = True
            for x in range(self.width):
                if not self[x][y]:
                    flag = False
            if flag:
                cleared_rows += 1
                for i in range(self.width):
                    for j in range(y, 0, -1):
                        self[i][j] = self[i][j - 1]
                    self[i][0] = None

        return cleared_rows
