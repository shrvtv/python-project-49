import random


task: str = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(x: int, y: int) -> int:
    x, y = min(x, y), max(x, y)
    if y % x == 0:
        return x
    else:
        divisor: int = x // 2
        while divisor >= 1:
            if x % divisor == 0 and y % divisor == 0:
                return divisor
            divisor -= 1


def generate_question_and_answer() -> tuple[str, str]:
    range_min: int = 0
    range_max: int = 100
    first_number: int = random.randint(range_min, range_max)
    second_number: int = random.randint(range_min, range_max)
    question: str = f'{first_number} {second_number}'
    answer: str = str(calculate_gcd(first_number, second_number))
    return question, answer
