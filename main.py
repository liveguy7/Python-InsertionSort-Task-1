
def insertion_sort(lst):
  for index in range(1, len(lst)):
    value = lst[index]
    i = index - 1
    while(i >= 0):
      if(value < lst[i]):
        lst[i+1] = lst[i]
        lst[i] = value
        i = i - 1
      else:
        break
  return lst

lst = [5,4,3,99,90,1,6,2]
print(insertion_sort(lst))
