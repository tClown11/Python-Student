#泛函数：根据第一个参数的类型，以不同的方式执行相同操作的一组函数
from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch     #@sinfledispatch标记处理object类型的基函数
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{0}</pre>'.format(content)

@htmlize.register(str)    #各个专门函数使用@《base_function》.register(《type》)装饰
def _(text):     #专门函数的名称无关紧要；_是个不错的选择，简单明了
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)     #为每个需要特殊处理的类型注册一个函数。numbers.Integral是int的虚拟超类
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)     #   可以叠放多个register装饰器，让同一个函数支持不同的类型
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'