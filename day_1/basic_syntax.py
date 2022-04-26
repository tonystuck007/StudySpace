#!-*-coding:utf-8

from sys import stdin, stdout

word = "friends"
print(word[-3:-1])
print(word[2:4])
phone_number = '1388-666-0006'
hiding_number = phone_number.replace(phone_number[:9], "*" * 9)
print(hiding_number)
search = "168"
num_a = "1355-168-0146"
num_b = "1680-133-1688"
print(f"168 is at {num_a.find(search)} to {num_a.find(search) + len(search)} of num_a")
print(f"168 is at {num_b.find(search)} to {num_b.find(search) + len(search)} of num_b")

# str.find(a)，获取a在字符串str中的位置，只返回找到的第一个
# 字符串中需要插入多个值的时候，可以用.format处理
print("168 is at {} to {} of num_b".format(num_b.find(search), num_b.find(search) + len(search)))

# 'b'、'r'、'u'、'f'在字符串前面的作用各不相同，分别表示如下：
# b：bytes，r：表示忽略转义符'\',u：表示使用unicode编码模式，常见于中文前面，f：在字符串内部加{}配合使用，可以放入表达式

x = 0b11000
b = 0b10111
c = 0b10000
x &= b
c &= x
print(bin(x), bin(c))
print(0 & 1)
print(2 | 1)


# &和|表示位运算，按位求交集或者并集，
# 1&2 =0，表示求1和2的交集，|表示或运算，1|2 = 3
# and 不一样，返回的是布尔值，and有0返回0，没有0，返回后一个值，如 2and3 = 3
# or 运算时，返回第一个非0值


def counter(input_num: int):
    # x = bin(input())
    # input_num = bin(input_num)
    count = 0
    while input_num > 0:
        count += 1
        input_num &= (input_num - 1)
    return count


counter(0b11011)
counter(1234)
# 将一个数转换成二进制，bin()
# 常用input()方法获取到的输入都会转化成字符串，还有sys.stdin.reading()都是获取成字符串，需要转换
# 二进制转化成10进制，int(bin_number,2)

# map函数映射，将list中的int全部转换成字符串
list_1 = [1, 2, 3, 4, ]
list_str = map(str, list_1)
print(tuple(list_str))

import math

print(list(map(math.sqrt, list_1)))

# lambda的使用：
# test = lambda x: x**2
# print(test(int(input())))

bar = lambda x, y: x if x > y else y
print(bar(1, 3))


def f(x, y): return x if x > y else y


print(f(10, 9))


def foo(list_1: list):
    a = []
    b = []
    _test = map(lambda x: a.append(x) if x % 2 == 0 else b.append(x), list_1)
    a.sort()
    b.sort()
    print(a + b)


foo([1, 6, 5, 4, 8, 9, 2])

def foo(income):
    return ("income" + str(income))


r = map(foo, ["A", "B", "C"])
print(r)
r1 = list(map(foo, ["A", "B", "C"]))
print(r1)
r2 = tuple(map(foo, ["A", "B", "C"]))
print(r2)
