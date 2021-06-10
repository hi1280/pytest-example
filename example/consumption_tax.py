class ConsumptionTax:
  def __init__(self, tax_rate):
    self.tax_rate = tax_rate
  def apply(self, price):
    return int((price * self.tax_rate) / 100) + price