# _*_ coding: utf-8 _*_
class Earth(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            # 调用父类object的new方法去返回一个实例，传给_instance变量
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        print("PASS")


a = Earth()
# 创建实例后的instance值
print("创建实例后的instance值为：{}".format(Earth._instance))

print(id(a))

b = Earth()
print(id(b))




