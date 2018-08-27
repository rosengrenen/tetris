from src.engine import Engine
from src.states.play_state import PlayState


def main():
    game = Engine(PlayState())
    game.start()


if __name__ == "__main__":
    main()