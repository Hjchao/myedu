# # 九九乘法表
# def for_for():
#     for i in range(1,10):
#         x=i+1
#         for j in range(1,x):
#                 print('%s*%s=%s'%(j,i,i*j),end='  ')
#         print('')
#
#
# # 计算1到50之间的奇数和?
# def sum_demo():
#     b=0
#     for i in range(1,51):
#         if i % 2==1:
#             b=b+i
#     print(b)
#
# import json
#
#
# # 输入两个数求这两个数之间的偶数和?
# def fenli_demo():
#     a= [['admin', '123456', '成功', '登录成功'], ['admin1', '123456', '错误', '用户名错误'], ['admin', '123456a', '错误', '密码错误'],
#      ['admin', '123456', '成功', '登录成功1'], ['admin1', '123456', '错误', '用户名错误1'], ['admin', '123456a', '错误', '密码错误1']]
#     for i in a:
#         a.pop()
#         print(a)



def jiujiu():


    for i in range(1,10):
        x=i+1
        for j in range(1,x):
            print('%s*%s=%s'%(i,j,i*j),end='  ')
        print('')


def jiu():
    for i in range(1, 10):
        x=i+1
        for j in range(1,x):
             print('%s*%s=%s'% (j, i,i*j),end=',')
        print('')


if __name__ == '__main__':
    # for_for()
    # sum_demo()
    # fenli_demo()
    jiu()














