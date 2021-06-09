from example import fizzbuzz

class TestFizzBuzz:
  def test_fizz_buzz(self):
    actual = fizzbuzz.create_fizz_buzz_list(16);
    assert len(actual) == 16
    assert actual[0] == "1"
    assert actual[1] == "2"
    assert actual[2] == "Fizz"
    assert actual[3] == "4"
    assert actual[4] == "Buzz"
    assert actual[5] == "Fizz"
    assert actual[6] == "7"
    assert actual[7] == "8"
    assert actual[8] == "Fizz"
    assert actual[9] == "Buzz"
    assert actual[10] == "11"
    assert actual[11] == "Fizz"
    assert actual[12] == "13"
    assert actual[13] == "14"
    assert actual[14] == "FizzBuzz"
    assert actual[15] == "16"
  def test_fizz_buzz_custom(self):
    expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz","16"]
    actual = fizzbuzz.create_fizz_buzz_list(16)
    assert len(actual) == 16
    assert actual == expected