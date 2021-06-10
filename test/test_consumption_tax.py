import pytest
from example.consumption_tax import ConsumptionTax

class TestConsumptionTax:
  @pytest.mark.parametrize("tax_rate,price,expected", [
    (5, 100, 105),
    (5, 3000, 3150),
    (10, 50, 55),
    (5, 50, 52),
    (3, 50, 51),
  ])
  def test_consumption_tax(self, tax_rate, price, expected):
    sut = ConsumptionTax(tax_rate)
    assert sut.apply(price) == expected