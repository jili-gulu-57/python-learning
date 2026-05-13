# s1={1,5,2,8,0,4,3,2,1}
# print(s1)
# s=set()
# print(type(s))

# s1={1,2,3,4,5,6,7,8,9,10}
# print(s1)
# s2={2,1,5,3,6,7,9,4}
# print(s2)
#
# s2.add(0)
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.intersection(s2))
# print(s1.union(s2))

football={"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
basketball={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","李化元","厉飞雨","云露"}
french = {"许木", "王卓", "十三", "虎跑", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
art = {"通天", "天运子", "韩立", "虎跑", "姜老道", "紫灵"}

# print(french&art)
# print(football&basketball&french&art)
# print(football-basketball)

#统计每个人选了几节课
all=[*football,*basketball,*french,*art]
for item in all:
    print(all.count(item),end=' ')