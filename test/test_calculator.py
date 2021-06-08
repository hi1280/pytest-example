import pytest
from example import calculator

class TestCalculator:
  def test_divide_0_is_exception(self):
    with pytest.raises(ZeroDivisionError):
      calculator.divide(1, 0)