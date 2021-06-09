from example import multi_line_string

class TestMultiLineString:
  def test_multi_line_string(self):
    expected = "Hello\nWorld\nHello\nWorld\nHello\nWorld\n"
    assert multi_line_string.join("Hello", "World", "Hello", "World", "Hello", "World") == expected