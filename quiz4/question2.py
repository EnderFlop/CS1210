def q2(x, y, z):
    if (x > y):
        if (y > z) and (z > 0):
            return True
    else:
        return False

def q2fix(x, y, z):
  return x > y and y > z and z > 0

print(q2fix(10, 9, 1))
