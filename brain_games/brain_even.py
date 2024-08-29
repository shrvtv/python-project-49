import random
import prompt


def game() -> None:
    print("Welcome to the Brain Games!")
    name: str = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    successful_tries_left: int = 3
    while successful_tries_left:
        number: int = random.randint(-999, 999)
        correct_answer: str = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
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
            print(f"Let's try again, {name}")
            break
