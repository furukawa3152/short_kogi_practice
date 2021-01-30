from pprint import pprint

import pandas as pd
import numpy as np
def_titanic =pd.read_csv("titanic_train.csv")
# print(def_titanic.info())
# pprint(def_titanic.sort_values("Age",ascending=False))
# def_temp = def_titanic[def_titanic["Age"]<40]#先に４０以下を指定
# def_temp = def_temp[def_temp["Sex"]=="male"]#さらに男のみに絞る
# print(def_temp)
# print(def_titanic[(def_titanic["Age"]<40)&(def_titanic["Sex"]=="male")])#＆でまとめることも可能
# print(def_titanic.loc[:,"Age"].describe())

print(def_titanic.isnull().sum())#欠損値の有無を出力
print(def_titanic.dropna())#欠損値のある行を削除

