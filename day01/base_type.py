def test1():
    print('test1')
def test2():
    print('test2')
def test3():
    print('test3')

def int_demo():
    aint =5
    print(aint)
    print(type(aint))

def str_demo():
    astr="5"
    print(astr)
    print(type(astr))

def float_demo():
    afloat=2.25
    print(afloat)
    print(type(afloat))

def add_demo(a,b):
    print(a+b)

def type_zhuanhuan():
    aint=7
    print(type(aint))
    print(type(str(aint)))
    print(type(int(aint)))
    print(int('18515451'))
# 字符串拼接
def str_join():
    a=123
    b='你好'
    c=2.25
    # 方式一
    print(str(a)+b+str(c))
    # 方式二 占位符 %s
    print('a是%s b是%s c是%s'%(a,b,c))

def jianfa_demo(a,b):
    c=a-b
    return c


if __name__ == '__main__':
    # test3()
    # test1()
    # test2()
    # int_demo()
    # str_demo()
    # float_demo()
    # add_demo(12,13)
    # add_demo('你好','世界')
    # type_zhuanhuan()
    str_join()
    c=add_demo(4,2)
    d=jianfa_demo(4,2)
    print(c)
    print(d)
