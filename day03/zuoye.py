# 九九乘法表
def for_for():
    for i in range(1,10):
        x=i+1
        for j in range(1,x):
                print('%s*%s=%s'%(j,i,i*j),end='  ')
        print('')


# 计算1到50之间的奇数和?
def sum_demo():
    b=0
    for i in range(1,51):
        if i % 2==1:
            b=b+i
    print(b)

# 输入两个数求这两个数之间的偶数和?





if __name__ == '__main__':
    # for_for()
    sum_demo()









