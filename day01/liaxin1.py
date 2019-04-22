#声明一个方法
def test1():
    print('test1')
def test2():
    print('test2')
def test3():
    print('test3')
def test4(a,b):
    print(a+b)
def first_demo():
    print('aaa')

# 字符串类型
def str_demo():
    astr='str'
    print(astr)
    print(type(astr))
# 数字型
def int_demo():
    aint=20
    print(aint)
    print(type(20))
# 小数型
def float_demo():
    afloat=2.25
    print(afloat)
    print(type(afloat))
# 数据类型的转换
def zhuanhuan_demo():
    a=10
    print(type(a))
    print(str(a))
    print(type(str(a)))


#字符串的拼接
#方法一
def join_demo():
    a=2.25
    b='chao'
    c=5
    print(str(a)+b+str(c))
#方法二
    print('a是%s b是%s c是%s'%(a,b,c))

# 调用另一个模块 from包名import模块名
from day01 import base_type





#调用方法
if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4(5,6)
    # first_demo()
    # str_demo()
    # int_demo()
    # float_demo()
    # zhuanhuan_demo()
    join_demo()








