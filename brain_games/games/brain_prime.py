import random


TASK: str = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number > 1:
        divisor: int = 2 # 2 is first prime number
        while divisor <= number // 2:
            if number % divisor == 0:
                return False
            divisor += 1
        return True
    return False


def generate_question_and_answer() -> tuple[str, str]:
    number_range: tuple[int, int] = (0, 999)
    number: int = random.randint(*number_range)
    question: str = str(number)
    answer: str = 'yes' if is_prime(number) else 'no'
    return question, answer
