import random


TASK: str = 'What is the result of the expression?'
NUMBER_RANGE: tuple[int, int] = (0, 999)


def generate_question_and_answer() -> tuple[str, str]:
    calculation_modes: tuple = (
        'addition',
        'subtraction',
        'multiplication'
    )
    current_mode: str = random.choice(calculation_modes)
    first_number: int = random.randint(*NUMBER_RANGE)
    second_number: int = random.randint(*NUMBER_RANGE)
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
