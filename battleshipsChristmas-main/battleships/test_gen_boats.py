import main

def test_gen_boats():
    result = main.gen_boats(5, 5)
    assert len(result) == 5