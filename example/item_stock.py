class ItemStock:
  def __init__(self):
    self.values = {}
  def add(self, item):
    num = self.values.get(item.name)
    if num == None:
      num = 0
    num += 1
    self.values[item.name] = num
  def get_num(self, item):
    num = self.values.get(item.name)
    if num == None:
      return 0
    else:
      return num