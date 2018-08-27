class Shape:
    def __init__(self, position, colour, nodes):
        self.position = position
        self.colour = colour
        self.nodes = nodes

    def rotate_right(self):
        size = 0
        for node in self.nodes:
            if node.x > size:
                size = node.x
            elif node.y > size:
                size = node.y
        for node in self.nodes:
            tmp = node.y
            node.y = node.x
            node.x = size - tmp

    def rotate_left(self):
        size = 0
        for node in self.nodes:
            if node.x > size:
                size = node.x
            elif node.y > size:
                size = node.y
        for node in self.nodes:
            tmp = node.y
            node.y = size - node.x
            node.x = tmp
