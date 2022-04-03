from solutions.CHK import checkout_solution


def test_chk_illegal():
    assert checkout_solution.compute(5) == -1


def test_chk():
    assert checkout_solution.compute("A B C") == 100
