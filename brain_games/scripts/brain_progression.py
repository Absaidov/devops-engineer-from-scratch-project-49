from brain_games.games.brain_progression import generate_round
from brain_games.scripts.start_engine import start_engine

DESCRIPTION: str = 'What number is missing in the progression?'


def main():
    start_engine(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()
