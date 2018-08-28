import pygame


class Engine:
    def __init__(self, state):
        self.running = False
        self.states = [state]
        pygame.init()

    def start(self):
        if self.running:
            return

        screen = pygame.display.set_mode((600, 800))
        self.running = True

        while self.running and len(self.states):
            events = pygame.event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            delta_time = 16
            self.states[-1].input(self, events)
            self.states[-1].update(self, delta_time)
            screen.fill((0, 0, 0))
            self.states[-1].render(self, screen)
            pygame.display.flip()

    def stop(self):
        self.running = False

    def push_state(self, state):
        self.states.append(state)

    def pop_state(self):
        self.states.pop()
