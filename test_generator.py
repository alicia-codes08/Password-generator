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
    """Checking lenghts of the both password."""
    lenght_use = generator.use_password
    lenght_keep = generator.keep_password

    assert len(lenght_use) == 8
    assert len(lenght_keep) == 8 