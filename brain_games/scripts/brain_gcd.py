#!/usr/bin/env python3
import brain_games.games.brain_gcd
import brain_games.game_engine


def main():
    brain_games.game_engine.engine(
        brain_games.games.brain_gcd.task,
        brain_games.games.brain_gcd.generate_question_and_answer
    )


if __name__ == "__main__":
    main()
