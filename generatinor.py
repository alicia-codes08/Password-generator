import random
from pathlib import Path

path = Path("password_elements.txt")
elements_list = path.read_text().splitlines()


# Generate a Password to use
def using_password_gen(password_list):
    """Generate a password to use:"""
    while len(password_list) < 8:
        element = random.choice(elements_list)
        password_list.append(element)

    
use_password = []
using_password_gen(use_password)
while len(use_password) < 8: 
    using_password_gen()
# print-Test
print(use_password)


# Generate password to keep
def highest_index():
    """Find out the highest index of the using-password."""
    highest_index = 0
    for element_up in use_password:
        index = elements_list.index(element_up)
        if index > highest_index:
            highest_index = int(index)
    
    return highest_index


def lowest_index():
    """Find out the lowest index of the using_password."""
    lowest_index = 50
    for element_up in use_password:
        index = elements_list.index(element_up)
        if index < lowest_index:
            lowest_index = int(index)
    
    return lowest_index
        

# get the highest and lowest index in your using-password 
h_index = highest_index()
l_index = lowest_index()
# print-test
print(h_index)
print(l_index)