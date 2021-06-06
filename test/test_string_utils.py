from example import string_utils

class TestStringUtils:
  def test_echo(self):
    assert string_utils.echo() == "abc"
