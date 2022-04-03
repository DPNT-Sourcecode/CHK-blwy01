from solutions.HLO import hello_solution


def test_hlo():
    assert hello_solution.hello("John") == "Hello, John!"
