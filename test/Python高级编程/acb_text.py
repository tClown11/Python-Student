#检查某个类是否有某种方法

class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(["Clown1", "Clown2"])
print(hasattr(com, "__len__"))
