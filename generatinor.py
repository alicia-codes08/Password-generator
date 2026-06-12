import random
from pathlib import Path

path = Path("password_elements.txt")
elements_list = path.read_text().splitlines()

# Generate a password
use_password = []
while len(use_password) < 8:
    element = random.choice(elements_list)
    if "A" in use_password or "-" in use_password:
        continue
    use_password.append(element)


for element in use_password[5:-1]:
    if elements_list.index(element) > 20:
        new_element = random.choice(elements_list[43:-1])
        if new_element in use_password:
            continue
        index_element = use_password.index(element)
        use_password[index_element] = new_element

print(use_password) 