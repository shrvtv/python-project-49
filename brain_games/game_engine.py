import prompt
import typing


def engine(
    task: str,
    generate_question_and_answer: typing.Callable[[], tuple[str, str]]
) -> None:
    print("Welcome to the Brain Games!")
    name: str = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(task)
    successful_tries_left: int = 3
    while successful_tries_left:
        raw_question: str
        correct_answer: str
        raw_question, correct_answer = generate_question_and_answer()
        print(f'Question: {raw_question}')
        player_answer: str = prompt.string('Your answer: ')
        if player_answer == correct_answer:
            print('Correct!')
            successful_tries_left -= 1
            if successful_tries_left == 0:
                print(f'Congratulations, {name}!')
        else:
            print(
                f"'{player_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
