# #导入整个模块
# # import random
# import random as rnd
# for i in range(10):
#     print(rnd.randint(1,100))

#导入部分功能
# from random import randint
# for i in range(10):
#     print(randint(1,50))

#导入全部功能，不需要写模块
# from random import *
#
# for i in range(10):
#     print(randint(1,200))

def print1():
    print("#"*20)

def print2():
    print("*"*20)

def print3():
    print("-"*20)

if __name__ == '__main__': #当前程序为主程序时，才执行后续代码
    print1()
    print2()
    print3()
print(__name__)