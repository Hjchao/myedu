
def if_demo():
    a = 1 > 2
#判断，
    if a:
        print('zhen')
    else:
        print('jia')

def ifel_demo():
    a=3
    if a ==1:
        print('a是1')
    elif a==2:
        print('a是2')
    elif a == 3:
        print('a是3')
    elif a == 5:
        print('a是5')
    elif a == 7:
        print('a是7')
    elif a == 8:
        print('a是8')
    elif a == 10:
        print('a是10')
    else:
        print ('a是%s'%a)
    print('if结束')



if __name__ == '__main__':
    ifel_demo()
