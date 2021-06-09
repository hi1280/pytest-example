def create_fizz_buzz_list(num):
  list = []
  for i in range(1, num + 1):
    if i % 15 == 0:
      list.append("FizzBuzz")
    elif i % 5 == 0:
      list.append("Buzz")
    elif i % 3 == 0:
      list.append("Fizz")
    else:
      list.append(str(i))
  return list