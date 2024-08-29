import random


TASK: str = 'What number is missing in the progression?'
NUMBER_RANGE: tuple[int, int] = (0, 100)
PROGRESSION_LENGTH_RANGE: tuple[int, int] = (5, 10)


def generate_question_and_answer() -> tuple[str, str]:
    number: int = random.randint(*NUMBER_RANGE)
    step: int = random.randint(*NUMBER_RANGE)
    last_element_index: int = random.randint(*PROGRESSION_LENGTH_RANGE) - 1
    hidden_element_index: int = random.randint(0, last_element_index)
    question: str = ''
    answer: str = ''
    index: int = 0
    while index <= last_element_index:
        if index == hidden_element_index:
            answer = str(number)
            question += '..'
        else:
            question += str(number)
        if index != last_element_index:
            question += ' '
        number += step
        index += 1
    return question, answer
