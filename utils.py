import random

async def get_roll(dice = 6):
    return random.randint(1, dice)

def are_numbers(first_number, second_number):
    return first_number.isnumeric() or not second_number.isnumeric()

def add_two_numbers(first_number, second_number):
    return int(first_number) + int(second_number)

unicode_emojis = ['😄', '😃', '😀', '😊', '😉', '🙃', '🤣', '😍', '😘', '😋']

def get_random_emoji():
    return None