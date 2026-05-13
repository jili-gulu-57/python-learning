# list=[1,2,"hello world",True,3.14]
# print(type(list))
# for i in list:
#     print(i,end=" ")
# print(list[0])
# print(list[-1])
# del list[0]
# print(list)
# del list[0]
# print(list)

# l1=[2,1,3,54,9,0,35]
# l1.sort()   #0,1,2,3,35,54
# print(l1)
#
# l1.append(17)
# print(l1)
#
# l1.insert(1,8)
# print(l1)
#
# l1.remove(3)
# print(l1)
#
# l1.pop(-1)
# print(l1)
#
# l1.reverse()
# print(l1)

# l2=[3,"ehqiw",True]
# l2.sort()   #错误，同一类型才能排序
# l3=["wwd","efref","gert"]
# l3.sort()
# print(l3)

# l=[]
# total=0
# for i in range(10):
#     x=int(input("请输入一个数字："))
#     l.append(x)
#     total+=x
#
# l.sort()
# print(f"最小值为：{l[0]}")
# print(f"最大值为：{l[-1]}")
# avg=total/len(l)
# print(f"平均值为：{avg}")

#1
# l1=[]
# for i in range(1,21):
#     x=i**2
#     l1.append(x)
# print(l1)
#
# #2
# l2=[19,23,54,64,87,20,109,232,123,43,26,55,72]
# l3=[]
# for i in l2:
#     if i%2==0:
#         i**=2
#         l3.append(i)
# print(l3)

# l1=['M','A','C','E','F','G','H','L','N','I','J','K','O']
# l2=['X','Z','T','Y','D','E','F','G']
# l3=['W','A','S','D']
# # total_l=l1+l2+l3
# total_l=[*l1,*l2,*l3]
# l=[]
# for i in total_l:
#     if i not in l:
#         l.append(i)
# l.sort()
# print(l)

# l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# l=[i**2 for i in l1 if i%3==0 or i%5==0]
# print(l)

# l1=[11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
# l=[i for i in l1 if i>0]
# print(l)

l=[1,2,3,4]
print(l)
l[0]=9
l[-1]=7
print(l)