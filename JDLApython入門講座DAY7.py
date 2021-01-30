from pprint import pprint

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
data = [train,test]

# print(train.info())#まずはデータを見てみる（欠損値あり）
# print(test.info())#こちらも欠損値あり
# pprint(train.tail(10))

# print(train.isnull().sum())#欠損地集計

# sns.boxplot(train["Fare"])
# sns.boxplot(train["Age"])
# plt.show()#外れ値確認

# sns.distplot(train["Age"],bins = 16)#ヒストグラム表示(分布を見る)
# sns.distplot(train["Fare"],bins=10)
# print(train["Fare"].value_counts().tail(15))#Fare（運賃）におけるそれぞれの値がいくつづつあるか
#値が細かいのでグルーピングすべき
# plt.show()

# sns.heatmap(train.corr(),cmap="summer",annot=True)#各値の相関関係を見る
# plt.show()
# sum_survived = train.groupby(["Sex"])[("Survived")].sum()
# sns.barplot(sum_survived.keys(),sum_survived.values)#男女の死亡者数
#数だけ見てもわからん（分母が違うからかも）
#男女それぞれの生存率を求める
# print(train.groupby(["Sex"])["Survived"].mean())
#female    0.742038 male      0.188908 男女の生存率は大きく異なる
# plt.show()
#乗船場所と生存率の集計
# print(train.groupby(["Embarked"])["Survived"].mean())
# sns.heatmap(train.corr(),cmap ="summer",annot = True)
#survivedと創刊のある値を探す
# plt.show()

#ここから前処理
#name
import re
def get_title(name):
    title_search = re.search("([A-Za-z]+)\.",name)
    if title_search:
        return title_search.group(1)
    return ""
for df in [train,test]:
    df["Title"] = df["Name"].apply(get_title)#敬称を抜き出しTitleという行に格納


# print(train["Title"].value_counts())
for df in data:
    df["Title"] = df["Title"].replace(["Mlle","Ms","Mme"],"Miss")

    df["Title"] = df["Title"].replace(["Lady","Countess","Capt","Col","Don","Dr","Major","Rev"
                                   ,"Sir","Jonkheer","Dona"],"others")

# print(test["Title"].value_counts())

#Embarkedの欠損値処理（２名だけなので一番多いSで補完）
train.Embarked = train.Embarked.fillna("S")
# print(train["Embarked"].value_counts())

#Ageの欠損値（敬称ごとの平均値に処理）
for df in data:
    mean = df.groupby("Title")["Age"].mean()
    for title in mean.keys():
        df.loc[(df.Age.isnull())&(df.Title==title),"Age"]= mean[title]

#Fareの欠損値（一か所だけなので中央値で埋める）
test.Fare = test.Fare.fillna(test.Fare.median())

# print(test.isnull().sum())
#年齢のカテゴライズ化
# sns.boxplot(df["Age"])
# plt.show()
for df in data:
    df["Age_band"] = pd.cut(df["Age"],[0,22,30,37,59,100],labels=range(5),right=False)

# print(train["Age_band"].value_counts())
#Fareもカテゴライズ化
for df in data:
    df["Fare_band"] = pd.cut(df["Fare"],[0,8,15,31,66,520],labels=range(5),right=True)

# print(train["Fare_band"].value_counts())

# sns.barplot(train["Title"],train["Survived"])
# plt.show()

#不要列の削除#出来ぬ！！！
# drop_columns = ['PassengerId','Name','Ticket','Cabin','Age','Fare']
#
# train = train.drop(drop_columns,axis=1)
# test = train.drop(drop_columns,axis=1)
# data = [train,test]

# print(train.info())
#文字列を数字に置き換え
for df in data:
    df.loc[df["Sex"]=="female","Sex"]=0
    df.loc[df["Sex"]=="male","Sex"]=1

    df.loc[df["Title"]=="Mr","Title"]=0
    df.loc[df["Title"]=="Miss","Title"]=1
    df.loc[df["Title"]=="Mrs","Title"]=2
    df.loc[df["Title"]=="Master","Title"]=3
    df.loc[df["Title"]=="others","Title"]=4

    df.loc[df["Embarked"]=="S","Embarked"]=0
    df.loc[df["Embarked"]=="C","Embarked"]=1
    df.loc[df["Embarked"]=="Q","Embarked"]=2

data[0].to_csv("titanic_train2.csv")

data[1].to_csv("titanic_test2.csv")









