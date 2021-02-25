def quickSort(group, left, right):

  if left >= right:
    return

  pivot = partition(group, left, right)
  
  quickSort(group, left, pivot - 1)
  quickSort(group, pivot + 1, right)


def partition(group, left, right):

  pivot = group[right]
  lessThan = left - 1

  for num in range(left, right):

    if group[num] <= pivot:

      lessThan += 1
      group[lessThan], group[num] = group[num], group[lessThan]

  group[right], group[lessThan + 1] = group[lessThan + 1], group[right]

  return lessThan + 1