#!/usr/bin/env python3
import brain_games.brain_even
import brain_games.game_engine


def main():
    brain_games.game_engine.engine(
        brain_games.brain_even.task,
        brain_games.brain_even.generate_question_and_answer
    )


if __name__ == "__main__":
    main()
