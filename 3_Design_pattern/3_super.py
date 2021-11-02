# _*_ coding: utf-8 _*_
class A(object):
    def __init__(self):
        self.nameaa = 'aa'
    def funca(self):
        print('function funca' )
class B(A):
    def __init__(self):
        self.namebb = 'bb'
    def funcb(self):
        # print('function funcb ' )
        pass
b = B() # 建立对象
print(b.funcb()) #调用子类的函数
# print(b.funca()) # 调用父类的函数
