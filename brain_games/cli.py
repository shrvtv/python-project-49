import prompt


def welcome_user() -> None:
    name: str = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
