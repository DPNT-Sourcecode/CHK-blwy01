from solutions.CHK import checkout_solution


def test_chk_not_str():
    assert checkout_solution.checkout(5) == -1


def test_chk_not_exist():
    assert checkout_solution.checkout("ABCy") == -1


def test_chk():
    assert checkout_solution.checkout("ABC") == 100


def test_chk_multiple():
    assert checkout_solution.checkout("AABCC") == 170


def test_chk_offer():
    assert checkout_solution.checkout("AAABBC") == 195
