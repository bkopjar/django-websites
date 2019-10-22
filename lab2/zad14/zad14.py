x = [1,1,3,5,23,45,34,20,5,11,17,28,17]

def func(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y