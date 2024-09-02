import random


TASK: str = 'What number is missing in the progression?'
NUMBER_RANGE: tuple[int, int] = (0, 100)
PROGRESSION_LENGTH_RANGE: tuple[int, int] = (5, 10)


def generate_question_and_answer() -> tuple[str, str]:
    number: int = random.randint(*NUMBER_RANGE)
    step: int = random.randint(*NUMBER_RANGE)
    length: int = random.randint(*PROGRESSION_LENGTH_RANGE)
    elements: list[str] = []
    for _ in range(length):
        elements.append(str(number))
        number += step
    hidden_element_index: int = random.randint(0, length - 1)
    answer: str = elements[hidden_element_index]
    elements[hidden_element_index] = '..'
    question: str = ' '.join(elements)
    return question, answer
