def echo(a):
  return a
def to_snake_case(str):
  result = ""
  for i, s in enumerate(str):
    if s.isupper() and i >= 1:
      result += "_"
    result += s.lower()
  return result