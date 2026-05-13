# s="abc"
# print(s)
# print(s[0])
# s[0]='c'
# print(s)

# s="Hello World,Hello Python"
# print(s.count('H'))
# print(s.find('World'))
# print(s.upper())
# print(s.lower())
# print(s.replace('H','h'))
# print(s)
# l=s.split(',')
# print(l)

#邮箱格式检验
# s=input("请输入邮箱：")
# if s.count('@')!=1 or s.find('.')==-1:
#     print("格式错误")
# else:
#     print("格式正确")

# s1=input("请输入字符串1：")
# s2=input("请输入字符串2：")
# print(s1==s2)

s="黄山落叶松叶落山黄"
if s==s[::-1]:
    print("是回文串")
else:
    print("不是回文串")
