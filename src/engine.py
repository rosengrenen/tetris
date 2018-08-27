import pygame
import time


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

        time_since_last_render = 0
        frames_per_second = 60

        time_since_last_update = 0
        updates_per_second = 120

        current_time = int(round(time.time() * 1000))

        while self.running and len(self.states):
            last_time = current_time
            current_time = int(round(time.time() * 1000))
            delta_time = current_time - last_time
            time_since_last_update += delta_time
            time_since_last_render += delta_time

            if time_since_last_update > 1000 / updates_per_second:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        self.running = False
                self.states[-1].input(self, events)
                self.states[-1].update(self, 1000 / updates_per_second)
                time_since_last_update -= 1000 / updates_per_second

            if time_since_last_render > 1000 / frames_per_second:
                screen.fill((0, 0, 0))
                self.states[-1].render(self, screen)
                pygame.display.flip()
                time_since_last_render -= 1000 / frames_per_second

    def stop(self):
        self.running = False

    def push_state(self, state):
        self.states.append(state)

    def pop_state(self):
        self.states.pop()
