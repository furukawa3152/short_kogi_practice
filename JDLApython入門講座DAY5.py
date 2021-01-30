import matplotlib.pyplot as plt

import numpy as np
# x = np.linspace(0,10,20)
# y = x**2
# z = (x-1)**3
# w = ((x-2)*(x-4))**2
# # plt.plot(x,y,label="y=x*2")
# # plt.plot(x,y,label="z=(x-1)*3")
# # plt.plot(x,w,label="w=()")
# # plt.legend()
# # plt.show()
# #一列目に表示
# plt.figure(figsize=(12,4))
# plt.subplot(1,3,1)
# plt.plot(x,y,label="y=x*2")
# plt.legend()
# #列目に表示
# plt.subplot(1,3,2)
# plt.plot(x,y,label="z=(x-1)*3")
# plt.legend
# #三列目に表示
# plt.subplot(1,3,3)
# plt.plot(x,w,label="w=()")
# plt.legend
# plt.show()

# #グラフ同士の重なりを防ぐ
# plt.tight_layout()

import pandas as pd

tips = pd.read_csv("tips.csv")
# # print(tips.isnull().sum())
# # left = range(4)
# # day = tips.day.value_counts().keys()
# # height = tips.day.value_counts().values
# # plt.bar(left,height,tick_label=day)
# # plt.show()
# fig,ax = plt.subplots(2,1,figsize = (8,8))
# tips_male = tips[tips["sex"] == "Male"][["total_bill","tip"]]
# tips_female = tips[tips["sex"] == "Female"][["total_bill","tip"]]
# ax[0].scatter(x = tips_male["total_bill"],y=tips_male["tip"],label="Male",color = "blue")
# ax[1].scatter(x = tips_female["total_bill"],y=tips_female["tip"],label="Female",color = "red")
# for i in range(2):#男性、女性の年齢別チップ額の分布
#     ax[i].set_xlabel("total_bill")
#     ax[i].set_ylabel("tip")
#     ax[i].legend()
# plt.show()

import seaborn as sns
# fig,ax=plt.subplots(1,3,figsize=(15,5))
#
# sns.countplot(tips.smoker,ax=ax[0])
# sns.distplot(tips.tip,bins=20,kde=False,ax=ax[1])
# sns.regplot(tips.total_bill,tips.tip,fit_reg=False,ax=ax[2])

# sns.pairplot(tips[["total_bill","tip"]])

sns.boxplot(tips["sex"],tips["tip"],hue=tips["day"])
plt.show()



