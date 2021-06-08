from example import string_utils

class TestStringUtils:
  def test_echo(self):
    assert string_utils.echo("abc") == "abc"
  def test_snake_case_aaa_is_aaa(self):
    assert string_utils.to_snake_case("abc") == "abc"
  def test_snake_case_HelloWorld_is_hello_world(self):
    assert string_utils.to_snake_case("HelloWorld") == "hello_world"
  def test_snake_case_practiceJunit_is_practice_junit(self):
    assert string_utils.to_snake_case("practiceJunit") == "practice_junit"