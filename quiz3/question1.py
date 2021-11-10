def foo1(L):
  n = len(L)
  result = 0
  index = 0
  while index < n:
    result = result + 2*L[index]
    index = index + 1
  return result, index

def foo2(L):
    n = len(L)
    result = 0
    index = 0
    while index < n:
        if index in L:
           result = result + index
        else:
           result = result + 2*L[index]
        index = index + 1
    return result, index

print(foo2(list(range(60))))