from example.range import Range

class TestRange:
  def test_range(self):
    sut = Range(0.0, 10.5)
    tests = [
      {"args": -0.1, "expected": False},
      {"args": 0.0, "expected": True},
      {"args": 10.5, "expected": True},
      {"args": 10.6, "expected": False},
    ]
    for t in tests:
      assert sut.contains(t["args"]) == t["expected"]
