import os

if __name__ == '__main__':
    # os.getcwd 获取当前目录(os做目录或者文件相关的操作)
    pwd = os.getcwd()
    print(pwd)

# 返回上级目录的字符串
    b = os.path.abspath('..')
    print(b)

#返回上上级目录的字符串
    c = os.path.abspath('../..')
    print(c)
    