x = ("My name is Bernardo")

def func(x):
  y = x.split()
  return " ".join(y[::-1])

print(func(x))