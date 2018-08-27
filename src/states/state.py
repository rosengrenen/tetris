class State:
    def input(self, engine, events):
        raise NotImplementedError("Method input is not implemented")

    def update(self, engine, delta_time):
        raise NotImplementedError("Method update is not implemented")

    def render(self, engine, surface):
        raise NotImplementedError("Method render is not implemented")
