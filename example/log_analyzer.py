class LogAnalyzer:
  def __init__(self, loader):
    self.loader = loader

  def analyze(self, file):
    data = self.loader.load(file)
    return self.do_analyze(data)

  def do_analyze(self):
    return {}

class LogLoader:
  def load(self):
    return {}