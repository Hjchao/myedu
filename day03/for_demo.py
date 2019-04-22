
alist=[1,2,3,'a','b','c','d']


#for（关键字）；i（变量名，代表循环次数） in(关键字) range（迭代器函数）
def for_demo():
    for i in range(10):
        print(i)
        print('hello world')
# 两个参数时（类似于切片），从第一个开始，到第二个的前一位结束
def for_demo1():
    for i in range(4,8):
        print(i)
    for j in range(10,20):
        print(j)
#三个参数时，从第一个参数开始开始计数，到第二个参数前一位结束，
def for_demo2():
    for i in range(2,13,3):
        print(i)

def for_demo3():
    for j in range(11,2,-3):
        print(j)
# 遍历：将列表里的每个元素都做一次操作
def for_list():
    for i in alist:
        print(i)
# 第二种遍历方式
def for_list2():
# 通过长度设置循环次数
# 把i当做索引值来遍历元素
    a=len(alist)
    for i in range(a):
        print(alist[i])
def for_list3():
    a=len(alist)
    for i in range(a):
        print(alist[i])

#停止所有循环
def for_break():
    for i in range(5):
        print(i)
        if i==2:
            break

# continue：停止本次循环，直接开始下一个循环
def for_continue():
    for i in range(5):
        print(i)
        if i==2:
            continue
        print('第%s循环'%i)
        print('')







if __name__ == '__main__':
    # for_demo()
    # for_demo1()
    # for_demo2()
    # for_demo3()
    # for_list()
    # for_list2()
    # for_break()
    for_continue()

