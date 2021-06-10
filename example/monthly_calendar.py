from datetime import date
import calendar

class MonthlyCalendar:
  def __init__(self, date):
    self.date = date
  def get_remaining_days(self):
    return (self.date.replace(day=calendar.monthrange(self.date.year, self.date.month)[1]) - self.date).days