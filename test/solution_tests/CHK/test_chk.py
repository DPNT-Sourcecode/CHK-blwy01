from solutions.CHK import checkout_solution


def test_chk_illegal():
    assert checkout_solution.checkout(5) == -1


def test_chk():
    assert checkout_solution.checkout("A B C") == 100


def test_chk_multiple():
    assert checkout_solution.checkout("A A B C C") == 170


def test_chk_offer():
    assert checkout_solution.checkout("A A A B B C") == 100
