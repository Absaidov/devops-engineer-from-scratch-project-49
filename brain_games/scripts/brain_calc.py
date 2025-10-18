from brain_games.games.brain_calc import generate_round
from brain_games.scripts.start_engine import start_engine

DESCRIPTION: str = 'What is the result of the expression?'

def main():
    start_engine(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()