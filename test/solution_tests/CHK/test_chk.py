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


def test_chk_multiple_offer():
    assert checkout_solution.checkout("AAAAAABC") == 300


def test_chk_get_free():
    assert checkout_solution.checkout("EEEBC") == 140


def test_chk_get_same_free():
    assert checkout_solution.checkout("FFFBC") == 70


def test_chk_get_same_free_and_more():
    assert checkout_solution.checkout("FFFF") == 30


def test_chk_get_same_free_not_enough():
    assert checkout_solution.checkout("FF") == 20


def test_chk_mixed_offer():
    assert checkout_solution.checkout("STX") == 45
