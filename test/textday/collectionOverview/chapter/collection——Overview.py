#coding = utf-8
__author__ = "keynote"

from collections import *
from collections import namedtuple
#抽象基类 interface


name_tuple = ("keynote1",29, 123)
name, age, height = name_tuple
name1, *other = name_tuple

User = namedtuple("User", ["name", "age", "height"])
user = User(name="keynote", age=18, height=60)
print(user.age, user.name, user.height)

#函数参数
#def ask(*args, **kwargs)