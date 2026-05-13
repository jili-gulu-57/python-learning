# def Print():
#     print("Hello world")
#     print("Hello Python")

# def Print(s):
#     print(s)
#
# # Print()
# Print("你好")

# def circlr(r):
#     return 3.14 * r * r,2*3.14 * r
#
# print(type(circlr(2)))

# def fun1(a,h):
#     """
#     a：底
#     h：高
#     return:三角形面积
#     """
#     return a*h/2
#
# def fun2(s):
#     """
#     :param s: 源字符串
#     :return: 字符串中元音字母个数
#     """
#     count=0
#     for i in s:
#         if i in ['a','e','i','o','u','A','E','I','O','U']:
#             count+=1
#         continue
#     return count
#
# def fun3(l):
#     avg=sum(l)/len(l)
#
# print(fun1(30,20))
# print(fun2("naihdbdebjzasj"))

# num=100
# def fun4():
#     global num
#     num=10
#     print(num)
#
# fun4()
# print(num)

# def fun5(a):
#     print(a+10)

# fun5(5)
# fun5("hello")

# def fun6(*nums):
#     print(max(nums))
#     print(min(nums))
#     print(sum(nums)/len(nums))
#
# fun6(1,2,3,4,5,6,7,8,9)

# def fun6(**args):
#     print(args)
#
# fun6(zs=18,ls=20)

#加法
# def add(x,y):
#     return x+y
#
# #减法
# def sub(x,y):
#     return x-y
#
# #乘法
# def mul(x,y):
#     return x*y
#
# #除法
# def div(x,y):
#     return x/y
#
# #回调函数
# def calc(x,y,oper):
#     return oper(x,y)
#
# print(calc(2,3,mul))

a: int =3
print(a)
c=a+1.2
print(c)

scores:list[int]=[13,42,57]
print(scores)
scores.append(100)
print(scores)
scores.append("A")  #有提醒但不报错
print(scores)