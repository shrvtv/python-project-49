#!/usr/bin/env python3
import brain_games.games.brain_prime
import brain_games.game_engine


def main():
    brain_games.game_engine.engine(
        brain_games.games.brain_prime.task,
        brain_games.games.brain_prime.generate_question_and_answer
    )


if __name__ == "__main__":
    main()
