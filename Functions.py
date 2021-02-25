def factorial(number):

  if number < 0 or number == float():
    raise Exception("Number given to the 'factorial' function must be a positive integer.")

  elif number == 0 or number == 1:
    return 1

  else:
    return number * factorial(number - 1)


def fibonacci(index):

  if type(index) == float or index < 0:
    raise Exception("Number given to the 'fibonacci' function must be a positive integer.")

  elif index == 0:
    return 0 

  elif index == 1 or index == 2:
    return 1

  else:
    return fibonacci(index - 1) + fibonacci(index - 2)


def binarySearch(group, value):
	
  group = group.sort()

  left = 0
  right = len(group) - 1

  while left <= right:

    mid = (left + right) // 2

    if group[mid] == value:
      return mid

    elif group[mid] < value:
      left = mid + 1

    elif group[mid] > value:
      right = mid - 1

  return -1