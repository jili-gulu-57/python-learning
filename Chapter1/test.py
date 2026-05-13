# 字面量
# print(1+2)
# print(13.14)
# print(True)
# print("hello world")
# print("hello  python")
# print(None)
# print(True+1)
# print(False+1)
# num=1.1
# _num=2.2
# num1=3.3
# print(num+False)

# 交换数据
# num1=10
# num2=20
# num3=30
# print(num1)
# print(num2)
# print(num3)
#
# num1,num2,num3=num3,num1,num2
# print(num1)
# print(num2)
# print(num3)

#打印类型
# print(type(num1))
# print(type(3.14))

# 字符串拼接
# s="hello" ' python'
# print(s)
# print("hello"+" world")
# print(type("num1")) 

# 占位符
# s="大家好，我是XX，今年"
# num=18
# print("%s %s岁 %s"%(s,num,False))
# print(f"大家好,我是XX今年{num}岁")

# account=10000
# withdraw=input("请输入取款金额：")
# money=account-float(withdraw)
# print(f"账户余额为：{money}")


# num1=input("请输入第一个数字：")
# num2=input("请输入第二个数字：")
# print(f"总和为：{int(num1)+float(num2)}")

# print(10+4)
# print(10-4)
# print(10*4)
# print(10/4)
# print(10//4)
# print(10%3)   #取余操作
# print(10**4)
# print(10**-4)

# num=input("enter any number:")
# if float(num) >=10 and float(num) <=100:
#     print(f"{num}在10-100区间")
# else:
#     print(f"{num}不在10-100区间")

# account=input("请输入账号：")
# password=input("请输入密码：")
#
# if(account!="aaa" or int(password)!=1234):
#     print("账号密码错误")
# else:
#     print("成功登录")

# year=input("请输入年份：")
# year=int(year)
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# num=input("请输入一个数：")
# num=float(num)
# if num>0:
#     print(f"{num}是正数")
# elif num<0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}是0")

# num=input("请输入一个数：")
# num=int(num)
# print(num)

# day=input("请输入一个日期：")
# match day:
#     case '1':
#         print("周一")
#         print("--------------")
#     case '2':
#         print("周二")
#     case '6'|'7':
#         print("周末")
#     case _: #其他情况
#         print("其他情况")

# num=0
# sum=0
# while num<=100:
#     num+=2
#     sum+=num
# print(sum)

# msg="hello world"
# for i in msg:
#     print(i)

# for i in range(6):
#     for j in range(4):
#         print("* ", end="")
#     print()

#打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j} ",end=" ")
#     print()

# true_name="aaa"
# true_passwd="1234"


# count=3
# while count>0:
#     name = input("请输入账号:")
#     passwd = input("请输入密码:")
#     if name==true_name and passwd==true_passwd:
#         print("登录成功！")
#         break
#     else:
#         count-=1
#         print("账号密码错误，请重新输入")
#
# if count<0:
#     print("错误超过三次，账号已被锁定")


# def Add(l):
#     return sum(l)
#
# l=[14,7,13,16,17,12,15,10,18,18,13,8,13,20,12,13,16,19,7,8,17,16,12,15,17,20,27,6,14,14,15,18,20,22,13,3,18,14,15,12,18,15,32,20,44,23,45,44,30,60,18,24,37,23,18,25,30,25,26,25,11,29,13,61,28,46]
# print(Add(l)/60)

from datetime import datetime

print(datetime.now().strftime("%Y/%m/%d %H:%M"))