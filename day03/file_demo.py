

if __name__ == '__main__':
    # w+:覆盖内容
    text_io = open('test.text', 'w+')
    text_io.write('你好')
# a+:追加内容
    text_io=open('test.text','a+')
    text_io.write('世界')
# r只能读取，不能写入
    text_io=open('test.text','r')
    #readline（）读写一行



