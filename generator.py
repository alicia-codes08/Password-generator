import random
from pathlib import Path


class Generator():
    """Class to manage the generator."""

    def __init__(self):
        """Initialize attributes and path."""
        self.path = Path("password_elements.txt")
        self.elements_list = self.path.read_text().splitlines()

        self.highest_index = 0
        self.lowest_index = 49

        self.use_password = []
        self.keep_password = []
        self.moved_place_num = 0


    def using_password_gen(self):
        """Generate a password to use:"""
        while len(self.use_password) < 8:
            element = random.choice(self.elements_list)
            if element=="A" and "-" in self.use_password:
                continue
            if element=="-" and "A" in self.use_password:
                continue
            self.use_password.append(element)


    # Generate password to keep
    def highest_lowest_index(self):
        """Find out the highest index of the using-password."""
        highest_index = self.highest_index
        for element_up in self.use_password:
            index = self.elements_list.index(element_up)
            if index > highest_index:
                highest_index = int(index)
        
        lowest_index = self.lowest_index
        for element_up in self.use_password:
            index = self.elements_list.index(element_up)
            if index < lowest_index:
                lowest_index = int(index)

        self.highest_index = highest_index
        self.lowest_index = lowest_index


    def moved_place(self):
        """Getting number of moved place:"""
        # get the highest and lowest index in your using-password 
        h_index = self.highest_index
        l_index = self.lowest_index 

        # getting range 
        right_max = 49 - h_index 
        left_max = l_index*-1
        # number of moved place for keeping-password 
        while True:
            choose_num = random.randint(left_max, right_max) 
            if choose_num != 0:
                break

        self.moved_place_num = choose_num

    def getting_keeping_password(self):
        """Getting keeping password."""
        # getting keeping-password
        for element in self.use_password:
            index = self.elements_list.index(element)
            new_index = index + self.moved_place_num
            new_element = self.elements_list[new_index]
            self.keep_password.append(new_element) 