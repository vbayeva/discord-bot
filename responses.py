import random

async def get_roll(dice = 6):
    return random.randint(1, dice)