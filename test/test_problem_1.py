from src.problem_1 import divisible_by_3_or_5
from src.problem_1 import sum_of_multiples_of_3_and_5

def test_sum():
    assert sum_of_multiples_of_3_and_5(1000) == 233168

def test_divisor():
    assert divisible_by_3_or_5(5) is True
