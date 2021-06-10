from datetime import date
from example.monthly_calendar import MonthlyCalendar

class TestMonthlyCalendar:
  def test_monthly_calendar_2012_1_31_is_0(self):
    sut = MonthlyCalendar(date(2012, 1, 31))
    assert sut.get_remaining_days() == 0
  def test_monthly_calendar_2012_1_30_is_1(self):
    sut = MonthlyCalendar(date(2012, 1, 30))
    assert sut.get_remaining_days() == 1
  def test_monthly_calendar_2012_2_1_is_29(self):
    sut = MonthlyCalendar(date(2012, 2, 1))
    assert sut.get_remaining_days() == 28