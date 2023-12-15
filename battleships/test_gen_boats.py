"""
pytest testing
"""
import main

def test_gen_boats():
    """
    testing of generating boats
    """
    result = main.gen_boats(5, 5)
    assert len(result) == 5
