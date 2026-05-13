# t=(1,4,1,5,9,3,5,2,0,)
# print(t)
# print(type(t))
# print(t.count(5))
# print(t[-1])
# print(t.index(9))
# x,y,*z=t
# print(x)
# print(y)
# print(z)
from networkx.drawing.nx_agraph import to_agraph

# x,*y,z=t
# print(x)
# print(y)
# print(z)

# x,*y,*z=t #错误，只允许有一个*
# print(x)
# print(y)
# print(z)

score=[["S001","王林",85,92,78],["S002","利姆湾",92,88,95],["S003","十三",78,85,82]]
Chinese=[]
math=[]
English=[]
for i in score:
    total=i[2]+i[3]+i[4]
    avg=total/3
    Chinese.append(i[2])
    math.append(i[3])
    English.append(i[4])
    print(f"{i[1]}同学总分为{total},平均分为{avg:.1f}")

print(f"语文最高分为{max(Chinese)},最低分为{min(Chinese)}")
print(f"数学最高分为{max(math)},最低分为{min(math)}")
print(f"英语最高分为{max(English)},最低分为{min(English)}")










