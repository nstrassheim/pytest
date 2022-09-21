import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0.1, 0.2, 0.3)
    ])
def test_sum(a, b, expected):
    from subtraction import sum
    answer = sum(a, b)
    assert answer == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (0.1, 0.2, -0.1)
    ])
def test_sub(a, b, expected):
    from subtraction import sub
    answer = sub(a, b)
    assert answer == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (2, 3, 6)
    ])
def test_mul(a, b, expected):
    from subtraction import mul
    answer = mul(a, b)
    assert answer == pytest.approx(expected)

