
import re

def generator_floats(text: str):
    pattern = re.compile(r'\b\d+\.\d+\b') # pattern for floats
    floats = pattern.findall(text) # find all floats in text
    for float_digit in floats: # make generator for floats
        yield float(float_digit)
        