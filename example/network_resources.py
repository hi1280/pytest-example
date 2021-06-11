class NetworkResources:
  def __init__(self, loader):
    self.loader = loader
  def load(self):
    reader = self.loader.get_input()
    str = reader.read()
    return str

class NetworkLoader:
  def get_input(self):
    return None