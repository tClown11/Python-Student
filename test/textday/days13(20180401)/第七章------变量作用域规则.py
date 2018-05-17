#书P159----160

b = 6
def f1(a):
    global b
    print(a)
    print(b)
    b = 9

f1(3)
print(b)