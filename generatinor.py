import random
from pathlib import Path

path = Path("password_elements.txt")
elements_list = path.read_text().splitlines()


def using_password_gen(password_list):
    """Generate a password to use:"""
    while len(password_list) < 8:
        element = random.choice(elements_list)
        password_list.append(element)

    
# Generate a Password to use
use_password = []
using_password_gen(use_password)
while len(use_password) < 8: 
    using_password_gen()


print(use_password)