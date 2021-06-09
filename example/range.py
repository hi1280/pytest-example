class Range:
  def __init__(self, min, max):
    self.min = min
    self.max = max
  def contains(self, value):
    return self.min <= value and self.max >= value