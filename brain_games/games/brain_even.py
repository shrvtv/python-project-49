import random


TASK: str = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_RANGE: tuple[int, int] = (-999, 999)


def generate_question_and_answer() -> tuple[str, str]:
    number: int = random.randint(*NUMBER_RANGE)
    correct_answer: str = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
