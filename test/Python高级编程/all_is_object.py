def ask(name="Clown"):
    print(name)

class Person:
    def __init__(self):
        print("Clown1")

def decorator_func(func):
    return ask
my_ask = decorator_func(ask)
my_ask('tj')

obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())