from example.authentication import Authentication
from example.account_dao import AccountDao
from example.account import Account

account = Account("user001", "pw123")

def mock_response_none(self):
  return None

def mock_response_1(self):
  return account

def mock_response_2(self):
  return Account("user001", "pw999")

class TestAuthentication:
  def test_not_exist_account(self, monkeypatch):
    sut = Authentication()
    dao = AccountDao()
    monkeypatch.setattr(dao, "find_or_null", mock_response_none)
    sut.set_dao(dao)
    assert sut.authenticate("user001", "pw123") == None
  def test_exist_account_and_equal_password(self, monkeypatch):
    sut = Authentication()
    dao = AccountDao()
    monkeypatch.setattr(dao, "find_or_null", mock_response_1)
    sut.set_dao(dao)
    assert sut.authenticate("user001", "pw123") == account
  def test_exist_account_and_not_equal_password(self, monkeypatch):
    sut = Authentication()
    dao = AccountDao()
    monkeypatch.setattr(dao, "find_or_null", mock_response_2)
    sut.set_dao(dao)
    assert sut.authenticate("user001", "pw123") == None