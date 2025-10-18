from brain_games.games.brain_gcd import generate_round
from brain_games.scripts.start_engine import start_engine

DESCRIPTION: str = 'Find the greatest common divisor of given numbers.'


def main():
    start_engine(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()
