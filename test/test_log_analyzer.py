import pytest
from example.log_analyzer import LogAnalyzer, LogLoader

def load_exception(self):
  raise ValueError

class TestLogAnalyzer:
  def test_load_method_throw_exception(self, monkeypatch):
    loader = LogLoader()
    monkeypatch.setattr(loader, "load", load_exception)
    sut = LogAnalyzer(loader)
    with pytest.raises(ValueError):
      sut.analyze("test")