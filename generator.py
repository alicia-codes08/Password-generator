import random
from pathlib import Path

path = Path("password_elements.txt")
elements_list = path.read_text().splitlines()


# Generate a Password to use
def using_password_gen(password_list):
    """Generate a password to use:"""
    while len(password_list) < 8:
        element = random.choice(elements_list)
        if element=="A" and "-" in use_password:
            continue
        if element=="-" and "A" in use_password:
            continue
        password_list.append(element)
    
use_password = []
using_password_gen(use_password)
while len(use_password) < 8: 
    using_password_gen()


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
    lowest_index = 49
    for element_up in use_password:
        index = elements_list.index(element_up)
        if index < lowest_index:
            lowest_index = int(index)
    
    return lowest_index
        
# get the highest and lowest index in your using-password 
h_index = highest_index()
l_index = lowest_index()

# getting range 
right_max = 49 - h_index 
left_max = l_index*-1

# number of moved place for keeping-password 
while True:
    choose_num = random.randint(left_max, right_max) 
    if choose_num != 0:
        break

# getting keeping-password
keep_password = [] 
for element in use_password:
    index = elements_list.index(element)
    new_index = index + choose_num 
    new_element = elements_list[new_index]
    keep_password.append(new_element) 