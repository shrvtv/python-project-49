import random


task: str = 'What number is missing in the progression?'


def generate_question_and_answer() -> tuple[str, str]:
    number_range: tuple[int, int] = (0, 100)
    number: int = random.randint(*number_range)
    step: int = random.randint(*number_range)
    progression_length_range: tuple[int, int] = (5, 10)
    progression_end_index: int = random.randint(*progression_length_range) - 1
    hidden_element_index: int = random.randint(0, progression_end_index)
    question: str = ''
    answer: str = ''
    index: int = 0
    while index <= progression_end_index:
        if index == hidden_element_index:
            answer = str(number)
            question += '..'
        else:
            question += str(number)
        number += step
        if index != progression_end_index:
            question += ' '
        index += 1
    return question, answer
