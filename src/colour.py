class Colour:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def darken(self, percentage):
        percentage /= 100
        r = self.r - self.r * percentage
        g = self.g - self.g * percentage
        b = self.b - self.b * percentage
        return max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0)

    def lighten(self, percentage):
        percentage /= 100
        r = self.r + (255 - self.r) * percentage
        g = self.g + (255 - self.g) * percentage
        b = self.b + (255 - self.b) * percentage
        return max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0)

    def get(self):
        return self.r, self.g, self.b
