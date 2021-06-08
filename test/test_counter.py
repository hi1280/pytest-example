from example.counter import Counter

class TestCounter:
  def test_increment_get_1_at_initial(self):
    sut = Counter()
    assert sut.increment() == 1
  def test_increment_get_2_at_run_increment_method(self):
    sut = Counter()
    sut.increment()
    assert sut.increment() == 2
  def test_increment_get_51_at_run_increment_method_50_times(self):
    sut = Counter()
    for _ in range(50):
      sut.increment()
    assert sut.increment() == 51