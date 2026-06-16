import random
from pathlib import Path

path = Path("password_elements.txt")
elements_list = path.read_text().splitlines()


def using_password_gen(password_list):
    """Generate a password to use:"""
    while len(password_list) < 8:
        element = random.choice(elements_list)
        password_list.append(element)


# Baustelle 
def highest_element():
    """Get the highest element."""
    last_element = 0
    for element in elements_list:
        if element in use_password:
            if elements_list.index(element) > last_element:
                last_element = elements_list.index(element)
    return last_element

def lowest_element():
    """Get the lowest element."""
    first_element = 51
    for element in elements_list:
        if elements_list.index(element) < last_element:
            first_element = elements_list.index(element)
    return first_element

     
# Generate a Password to use
use_password = []
using_password_gen(use_password)
while len(use_password) < 8: 
    using_password_gen()


print(use_password)