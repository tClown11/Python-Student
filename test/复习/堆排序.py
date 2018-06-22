result = 0
def f1(x):
   global result
   result += x
   return result


print(f1(3))
print(f1(5))
print(f1(6))


origin = 0
def factory(pos):
    def go(star):
        nonlocal pos
        new_pos = pos + star
        pos = new_pos
        return new_pos
    return go

f1 = factory(origin)
print(f1(2))
print(f1(3))
print(f1(6))