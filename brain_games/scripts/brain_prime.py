from brain_games.games.brain_prime import generate_round
from brain_games.scripts.start_engine import start_engine

DESCRIPTION: str = \
    'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    start_engine(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()
