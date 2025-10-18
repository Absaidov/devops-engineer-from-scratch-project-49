from brain_games.scripts.start_engine import start_engine
from brain_games.games.brain_even import DESCRIPTION, generate_round

def main():
    start_engine(DESCRIPTION, generate_round)

if __name__ == '__main__':
    main()