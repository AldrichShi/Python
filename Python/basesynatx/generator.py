# -*- coding: utf-8 -*-
# generator.py
# @author King
# @description
# @created 2019-07-01T10:55:09.945Z+08:00
# @last-modified 2019-07-01T13:24:06.546Z+08:00
#

# 1 .迭代是python 最强大功能之一,是访问集合元素的一种方式
# 2 .迭代器可以记住遍历位置的对象
# 3 .迭代器从对象集合的第一个元素开始访问,一直到最后一个结束,只能向前不能向后
# 4 .迭代器基本方法iter() 和 next()
# 5 .str ,set, tuple 都可以用于创建迭代器


import sys


def fibonacci(n):  # 生成器函数斐波数列
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1


f = fibonacci(10)
while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
