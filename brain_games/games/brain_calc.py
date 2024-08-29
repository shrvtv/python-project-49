import random


task: str = 'What is the result of the expression?'


def generate_question_and_answer() -> tuple[str, str]:
    calculation_modes: tuple = (
        'addition',
        'subtraction',
        'multiplication'
    )
    current_mode: str = random.choice(calculation_modes)
    range_min: int = 0
    range_max: int = 999
    first_number: int = random.randint(range_min, range_max)
    second_number: int = random.randint(range_min, range_max)
    expression_sign: str = ''
    answer: int = 0
    match current_mode:
        case 'addition':
            expression_sign = '+'
            answer = first_number + second_number
        case 'subtraction':
            expression_sign = '-'
            answer = first_number - second_number
        case 'multiplication':
            expression_sign = '*'
            answer = first_number * second_number
    question: str = f'{first_number} {expression_sign} {second_number}'
    return question, str(answer)
