import random


TASK: str = 'Find the greatest common divisor of given numbers.'
NUMBER_RANGE: tuple[int, int] = (0, 100)


def calculate_gcd(x: int, y: int) -> int:
    x, y = min(x, y), max(x, y)
    if x == 0:
        return y
    elif y % x == 0:
        return x
    else:
        divisor: int = x // 2
        while divisor >= 1:
            if x % divisor == 0 and y % divisor == 0:
                return divisor
            divisor -= 1


def generate_question_and_answer() -> tuple[str, str]:
    first_number: int = random.randint(*NUMBER_RANGE)
    second_number: int = random.randint(*NUMBER_RANGE)
    question: str = f'{first_number} {second_number}'
    answer: str = str(calculate_gcd(first_number, second_number))
    return question, answer

print(calculate_gcd(67, 0))