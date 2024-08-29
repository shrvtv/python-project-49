import random


task: str = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer() -> tuple[str, str]:
    range_min: int = -999
    range_max: int = 999
    number: int = random.randint(range_min, range_max)
    correct_answer: str = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
