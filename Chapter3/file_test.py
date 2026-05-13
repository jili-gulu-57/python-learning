# f=open("resources/test.txt","r",encoding="utf-8")
#
# # content=f.read()    #读取所有文件内容
#
# content=f.readlines()
# print(content)
#
# f.close()

# f=open("resources/test2.txt","w",encoding="utf-8")
#
# f.write("hello world\n")
# f.write("hello world\n")
#
# f.close()

# -------------------------------------------释放资源

# f=open("resources/test2.txt","w",encoding="utf-8")
#
# try:
#     f.write("hello world\n")
#     num=2/0
#     f.write("hello world\n")
# except ZeroDivisionError as e:
#     print("出现除零错误:",e)
#
# finally:
#     print("释放资源")
#     f.close()


# with open("resources/test2.txt","w",encoding="utf-8") as f:
#     f.write("hello python\n")
#     num=2/0
#     f.write("hello python\n")

# with open("C:\\Users\\22632\\PycharmProjects\\PythonProject1\\Chapter3\\resources\\test2.txt","r") as f:
#     print(f.read())

with open("C:/Users/22632/PycharmProjects/PythonProject1/Chapter3/resources/test2.txt", "r") as f:
    print(f.read())