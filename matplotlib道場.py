import matplotlib.pyplot as plt
import numpy as np


# fig, ax = plt.subplots()
# ax.plot([1,2,3,4],[1,4,2,3])#ジグザググラフになる

# plt.plot([1,2,3,4])#これだけ入れたら勝手にy軸と判断し、同じｘ軸を作成
# plt.ylabel("same numbers")#ラベルを付与

# plt.plot([1,2,3,4],[1,4,9,16],"g-")#ro=赤点 r-=赤線
# plt.axis([0,6,0,20])#0-6（ｘ）,0-20（ｙ）

# t = np.arange(0,5,0.2)#0-5までの0.2刻み
#
# plt.plot(t,t,"r--",t,t**2,"bs",t,t**3,"g^")#三つのグラフをそれぞれの色、線（点）で出力


# data ={"a":np.arange(50),
#        "c":np.random.randint(0,50,50),
#        "d":np.random.randn(50)}
#
# data["b"] =data["a"] + 10* np.random.randn(50)
# data["d"] = np.abs(data["d"])*100
#
# plt.scatter("a","b",c="c",s="d",data=data)#cは色、ｓは点の大きさを指定。a,bはそれぞれｘ、ｙ
# plt.xlabel("entry a")
# plt.ylabel("entry b")

# names= ["group_a","group_b","group_c"]
# values = [1,10,100]
#
# plt.figure(figsize=(9,3))
#
# plt.subplot(131) #複数グラフ並べる
# plt.bar(names,values)
# plt.subplot(132)
# plt.scatter(names,values)
# plt.subplot(133)
# plt.plot(names,values)
# plt.suptitle("Categorical plotting")#タイトル
# line,= plt.plot([1,2,3,4],[1,4,9,16],linewidth=10.0) #線の太さ
# line.set_antialiased(True)#アンチエイリアス(線の)滑らかさ


# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure()
# plt.subplot(211)
# plt.plot(t1,f(t1),"bo",t2,f(t2),"k")#尺が違う二つの配列を線と点で配置
#
# plt.subplot(212)
# plt.plot(t2,np.cos(2*np.pi*t2),"r--")
mu, sigma = 100,15
x = mu+ sigma *np.random.randn(10000)
n , bins , patches = plt.hist(x, 50, density=1, facecolor="g")
plt.xlabel("itaru")
plt.ylabel("satomi")
plt.title("SoraKokoro")
plt.text(140,.025,r"$\mu=100,\ \ sigma=15$")
plt.show()



