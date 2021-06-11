class Authentication:
  def get_dao(self):
    return self.dao
  def set_dao(self, val):
    self.dao = val
  def authenticate(self, user_id, password):
    account = self.dao.find_or_null(user_id)
    if account == None:
      return None
    return account if account.password == password else None