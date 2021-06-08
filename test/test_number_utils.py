from example import number_utils

class TestNumberUtils:
  def test_is_even(self):
    assert number_utils.is_even(10) == True
  def test_is_not_even(self):
    assert number_utils.is_even(7) == False
