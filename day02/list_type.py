
def list_sel(a):
    print(a[2])
    print(a[-3])
    # 切片取值 方法：第一个数字代表第几位（从0开始数），第二数字代表到位数的前一位（也是从0开始）
    print(a[:])




if __name__ == '__main__':
    alist = ['a',5,'haode','10',1,2,3,4,6,20,14,69,54,21,455]
    list_sel(alist)
    # print(alist)