# def hoge(itaru,*args):
#     print(args,itaru)
#
# hoge(123,1,1,3)
#
# def hoge(arg, *tpargs,**kwargs):
#     print(arg)
#     print(tpargs)
#     for i in range(len(kwargs)):
#         print(list(kwargs.items())[i])
#
# hoge("furukawa",1,2,3,a="itaru",b="satomi",c="sora",d="kokoro")
#
# def single(arg1,*,arg2):
#     print(arg1+" and "+arg2)
#
# single(arg1="a",arg2="b")
# a =1
# b ="itaru"
# try:
#     print(a*b)
#
# except(ZeroDivisionError):
#     print("0で除算は出来ないよ")
#
# except(ValueError):
#     print("バリュ-エラ-でござる")
#
# except:
#     print("他のエラ-じゃよ")
#
# else:
#     print("そのほか（エラーが出なければここを経由）")
#
# finally:
#     print("最後はいつでも")
#
# class itaru(Exception):
#     pass
#
# def func(name:int):
#     try:
#         if name !=0:
#             raise_origin(name)
#         else:
#             print("seikourei")
#     except itaru:
#         print("test")
# def raise_origin(arg):
#     print(f"{arg}オリジナルエラーを作ったよ")
#     raise itaru
#
# print(type(raise_origin))
#
# import sys
# print(sys.argv)

# def scope_test():
#     def do_local():
#         purin = 'local purin'
#         print(purin)
#
#
#     def do_nonlocal():
#         nonlocal purin
#         purin = 'nonlocal purin'
#         print(purin)
#
#     def do_grobal():
#         global purin
#         purin = 'grobal purin'
#         print(purin)
#
#     purin = 'test purin'
#     do_grobal()
#     print(purin)
#
# scope_test()
#
# print(purin)

# class Fish:#親クラス
#     value = "クラス変数のテストだよ"
#     def __init__(self,name,build="hone",eyelids=False):
#         self.name =name
#         self.build = build
#         self.eyelids =eyelids
#
#     def swim(self):
#         print("こちらの魚は泳ぎます")
#         self.swim_back()
#
#     def swim_back(self):
#         print("こちらの魚は後ろ向きにも泳ぎます")
#
# class Medaka(Fish):#子クラス
#     def swim(self):
#         print("こちらの魚は動きません！！上書きされたからね")
#     pass
#
# sakana1 = Fish("マグロ（親クラス）","ほねほね","ぱっちり")
# print("名前",sakana1.name)
# print("骨格",sakana1.build)
# print("まぶた",sakana1.eyelids)
# sakana1.swim()



# sakana2 = Medaka("メダカ（子クラス）","骨なし","一重")
# print("名前",sakana2.name)
# print("骨格",sakana2.build)
# print("まぶた",sakana2.eyelids)
# sakana2.swim()
# sakana2.swim_back()
# print(Fish.value)

# class Sample:
#
#   c_list = []
#
#   def add_c_list(self,data):
#     self.c_list.append(data)
#
# print("出力結果:", end=" ")
# sample1 = Sample()
# sample1.add_c_list("データ1")
#
# sample2 = Sample()
# sample2.add_c_list("データ2")
#
# for item_data in sample1.c_list:
#   print(item_data, end=" ")

list = [1,"test",[1,2,3,'itaru']]
import json
print(json.dumps(list))

