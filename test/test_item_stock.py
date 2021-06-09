import pytest
from example.item_stock import ItemStock
from example.item import Item

@pytest.fixture
def item_stock():
  return ItemStock()

@pytest.fixture
def item():
  return Item("book", 3800)

@pytest.fixture
def add_item_stock(item_stock, item):
  item_stock.add(item)
  return item_stock

class TestItemStockAtInitial:
  def test_get_num_is_0_at_initial(self, item, item_stock):
    assert item_stock.get_num(item) == 0
  def test_get_num_is_1_after_add_item(self, item, item_stock):
    item_stock.add(item)
    assert item_stock.get_num(item) == 1
class TestItemStockAfterAddItem:
  def test_get_num_is_1_after_add_item(self, item, add_item_stock):
    assert add_item_stock.get_num(item) == 1
  def test_get_num_is_2_after_add_same_item(self, item, add_item_stock):
    add_item_stock.add(item)
    assert add_item_stock.get_num(item) == 2
  def test_get_num_is_1_after_add_different_item(self, item, add_item_stock):
    bike = Item("bike", 57000)
    add_item_stock.add(bike)
    assert add_item_stock.get_num(item) == 1
