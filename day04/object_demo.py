

class H (object):

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex


    def chifan(self):
        print('%s吃饭'%self.name)
    def shuijiao(self):
        print('%s睡觉'%self.name)
# 类的继承，H是被继承的父类名，T是类名（继承H类）
class T (H):
    def work(self):
        self.shuijiao()
        self.chifan()
        print('%s做测试'%self.name)


if __name__ == '__main__':
    # h是对象名，H调用类名（类的初始化参数）
    h=H('小明',20,'男')
    # h.chifan()
    # h.shuijiao()
    t = T('小明', 20, '男')
    # 对象可以调用类的方法和属性
    t.work()






