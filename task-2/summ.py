from typing import Callable

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text) # use generator for text processing
    total_income = sum(numbers_generator) # sum all floats from number generator
    return total_income