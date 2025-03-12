def add(a, b):
  return a + b

def curry_add(a):
  def inner(b):
    return add(a, b)
  return inner

add_two = curry_add(int(input("ENTER A NUMBER: ")))

print(add_two(int(input("ENTER ANOTHER NUMBER: "))))