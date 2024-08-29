import random


task: str = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer() -> tuple[str, str]:
    number_range: tuple[int, int] = (-999, 999)
    number: int = random.randint(*number_range)
    correct_answer: str = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
