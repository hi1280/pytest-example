from example.network_resources import NetworkResources, NetworkLoader

class MockResponse:
    @staticmethod
    def read():
        return "Hello World"

def mock_get_input():
  return MockResponse()

class TestNetworkResources:
  def test_load_test(self, monkeypatch):
    loader = NetworkLoader()
    monkeypatch.setattr(loader, "get_input", mock_get_input)
    sut = NetworkResources(loader)
    assert sut.load() == "Hello World"