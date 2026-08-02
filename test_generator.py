import pytest
from generator import Generator 

@pytest.fixture 
def generator():
    """Make instance for tests."""
    gen_i = Generator()
    gen_i.using_password_gen()
    gen_i.highest_lowest_index()
    gen_i.moved_place()
    gen_i.getting_keeping_password() 
    
    return gen_i 


def test_checking_lenght(generator):
    """Checking lenghts of the both passwords."""
    lenght_use = generator.use_password
    lenght_keep = generator.keep_password

    assert len(lenght_use) == 8
    assert len(lenght_keep) == 8 

def test_moved_place(generator):
    """Checking keeping password is moved place away from the using one."""
    elements = generator.elements_list
    using = generator.use_password
    keeping = generator.keep_password
    moved_place = generator.moved_place_num 

    # testing each element of the keeping password
    using_new = []
    for element in keeping:
        index = elements.index(element)
        moved_index = index - moved_place
        using_element = elements[moved_index] 
        using_new.append(using_element)

    assert using_new == using 