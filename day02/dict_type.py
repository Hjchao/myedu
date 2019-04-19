# dict  字典
import json

adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}
cdict_str = '{"username":"yansl","password":"123456"}'

def dict_sel():
    print(adict['username'])
    print(bdict[5])
    print(bdict['password'])
    b = adict['password']
    print(b)

# 删除字典的元素
def dict_del():
    adict.pop('password')
    print(adict)

def dict_update():
    adict['username']='胡金超'
    print(adict)

def dict_add():
    adict.update(bdict)
    print(adict)

    cdict = dict(bdict,** adict)
    print(cdict)

def dict_add1():
    adict['sex']='男'
    print(adict)

# 字典转字符串
def dic2str():
    print(type(adict))
    adict_str=json.dumps(adict)
    print(adict_str)
    print(type(adict_str))

#字符串转字典
def str2dict():
    print(type(cdict_str))
    astr_dict =json.loads(cdict_str)
    print(astr_dict)
    print(type(cdict_str))








if __name__ == '__main__':
    # dict_sel()
    # dict_del()
    # dict_update()
    # dict_add()
    # dict_add1()
    # dic2str()
    str2dict()

