# d={"zs":18,"ls":21,27:30}
# print(d)
# # print(d["zs"])
# # print(d['zs'])
# # print(d['''zs'''])
# # print(d['ls'])
# # print(d[27])
# d['ww']=51
# print(d)
# # print(type(d.items()))
# # print(d.keys())
# # print(d.values())
# d.pop(27)
# print(d)
from nltk.corpus.europarl_raw import english
from sympy.core.random import choice

# print("######## 购物车系统 ########")
# print("#        1.添加购物车      #")
# print("#        2.修改购物车      #")
# print("#        3.删除购物车      #")
# print("#        4.查询购物车      #")
# print("#        5.退出购物车      #")
# print("###########################")
# num=input("请输入要执行的操作（1-5）：")
# shopping={}
# while True:
#     match num:
#         case "1":
#             k,v1,v2=input("请输入商品名称,价格和数量：").split(" ")
#             shopping[k]=[v1,v2]
#         case "2":
#             k,v1,v2=input("请输入要修改的商品名称和价格：").split(" ")
#             shopping[k]=[v1,v2]
#         case "3":
#             k=input("请输入要删除的商品名称：")
#             if k not in shopping.keys():
#                 print("商品不存在")
#             else:
#                 shopping.pop(k)
#         case "4":
#             print("------- 购物车 -------")
#             for k,(v1,v2) in shopping.items():
#                 print(f"商品:{k} 价格:{v1}元 数量:{v2}")
#             print("---------------------")
#             print()
#         case "5":
#             break
#         case _:
#             print("输入错误，请重新输入：")
#     print("######## 购物车系统 ########")
#     print("#        1.添加购物车      #")
#     print("#        2.修改购物车      #")
#     print("#        3.删除购物车      #")
#     print("#        4.查询购物车      #")
#     print("#        5.退出购物车      #")
#     print("###########################")
#     num=input("请输入要执行的操作（1-5）：")

students={}

menu="""
+------------------------------------- 学生管理系统 --------------------------------------------+
|        1.添加    2.修改    3.删除    4.查询    5.显示全部    6.统计    7.退出                    |    
+----------------------------------------------------------------------------------------------+ 
"""
print(menu)
while True:
    choice=input("请输入操作选项：")
    match choice:
        case "1":
            name=input("请输入学生姓名：")
            scores=input("请输入学生成绩(语/数/英)：").split()
            students[name] = scores
            print(f"{name}添加成功")
        case "2":
            name = input("请输入要修改的学生姓名：")
            if name not in students:
                print("学生不存在，请重新选择操作")
            else:
                scores = input("请输入学生成绩(语/数/英)：").split()
                students[name] = scores
                print(f"{name}成绩修改成功")
        case "3":
            name = input("请输入要删除的学生姓名：")
            if name not in students:
                print(f"{name}不存在，请重新选择操作")
            else:
                students.pop(name)
                print(f"{name}删除成功")
        case "4":
            name=input("请输入要查询的学生姓名：")
            if name not in students:
                print(f"{name}学生不存在，请重新操作")
            else:
                print(f"{name}：语文：{students[name][0]} 数学{students[name][1]} 英语{students[name][2]}")
        case "5":
            print("---------- 学生成绩信息 ------------")
            for name, scores in students.items():
                print(f"{name}：语文{scores[0]} 数学{scores[1]} 英语{scores[2]}")
            print("----------------------------------")

        #成绩统计
        case "6":
            chinese=[int(v[0]) for v in students.values()]
            math=[int(v[1]) for v in students.values()]
            english=[int(v[2]) for v in students.values()]
            avg_chinese=sum(chinese)/len(chinese)
            avg_math=sum(math)/len(math)
            avg_english=sum(english)/len(english)
            #for debug
            # for i in chinese:
            #     print(f"chinese:{i}",end=" ")
            # for i in math:
            #     print(f"math:{i}",end=" ")
            # for i in english:
            #     print(f"english:{i}",end=" ")
            #
            #打印各科高分，最低分，平均分及对应学生
            for name,(ch_score,ma_score,en_score) in students.items():
                if int(ch_score)==max(chinese):
                    ch_top_name = name
                if int(ch_score)==min(chinese):
                    ch_low_name = name
                if int(ma_score)==max(math):
                    ma_top_name = name
                if  int(ma_score)==min(math):
                    ma_low_name = name
                if int(en_score)==max(english):
                    en_top_name = name
                if int(en_score)==min(english):
                    en_low_name = name
            print("---------- 成绩统计 ----------")
            print(f"语文最高分：{ch_top_name}:{max(chinese)} 最低分：{ch_low_name}:{min(chinese)} 平均分：{avg_chinese}")
            print(f"数学最高分：{ma_top_name}:{max(math)} 最低分：{ma_low_name}:{min(math)} 平均分：{avg_math}")
            print(f"英语最高分：{en_top_name}:{max(english)} 最低分：{en_low_name}:{min(english)} 平均分：{avg_english}")
            print("------------------------------")

        case "7":
            break
        case _:
            print("请求错误，请重新输入")
            print(menu)