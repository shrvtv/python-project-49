import random


task: str = 'What is the result of the expression?'


def generate_question_and_answer() -> tuple[str, str]:
    calculation_modes: tuple = (
        'addition',
        'subtraction',
        'multiplication'
    )
    current_mode: str = random.choice(calculation_modes)
    number_range: tuple[int, int] = (0, 999)
    first_number: int = random.randint(*number_range)
    second_number: int = random.randint(*number_range)
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
