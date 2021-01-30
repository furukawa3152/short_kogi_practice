from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
train = pd.read_csv("titanic_train2.csv")
test = pd.read_csv("titanic_test2.csv")

data = [train,test]
data[0].to_pickle("titanic_train.pkl")
data[1].to_pickle("titanic_test.pkl")

train = pd.read_pickle("titanic_train.pkl")
test = pd.read_pickle("titanic_test.pkl")
data = [train,test]
# print(data[0].head())
#テストデータ作成のため分割
tr_train,tr_test=train_test_split(train,test_size=0.3,random_state=1234)
#訓練用の説明変数
tr_train_X = tr_train[train.columns[1:]]
#訓練用の目的変数
tr_train_Y = tr_train[train.columns[0]]

#評価用の説明変数
tr_test_X = tr_test[train.columns[1:]]

#評価用の目的変数
tr_test_Y = tr_test[train.columns[0]]

#決定木の実装
#作成
from sklearn.ensemble import RandomForestClassifier
# model=RandomForestClassifier(n_estimators=100)
# # #学習
# model.fit(tr_train_X,tr_train_Y)
# #予測
# predict = model.predict(tr_test_X)
#
# #精度確認
# from sklearn import metrics
# print("判別率：",metrics.accuracy_score(predict,tr_test_Y))

#K-分割交差検証
# from sklearn.model_selection import KFold,cross_val_score,cross_val_predict
#
# kf=KFold(n_splits=5, random_state=30,shuffle=True)
x = train[train.columns[1:]]
y = train["Survived"]
# cv_result =cross_val_score(model,x,y,cv=kf)
# print(cv_result)
# print("平均精度：{}".format(cv_result.mean()))
#
#グリッドサーチの実装#最適なn_estinatorは400と出る
from sklearn.model_selection import GridSearchCV
param={"n_estimators":range(100,1000,100)}
GS_rf=GridSearchCV(estimator=RandomForestClassifier(random_state=0),
                   param_grid=param,
                   verbose=True,
                   cv=5)
GS_rf.fit(x,y)
# print("ベストスコア：{}".format(GS_rf.best_score_))
# print("最適なパラメータ{}".format(GS_rf.best_estimator_))



#最後に正解のないテストデータへの予測（グリッドサーチのベストモデルを用いて分類）
model=GS_rf.best_estimator_
# #学習
model.fit(train[train.columns[1:]],train[train.columns[0]])
#予測
test_prediction = model.predict(test)


passenger_id = np.arange(894,1310)
test_result = pd.DataFrame({"Passengerid":passenger_id,"Survived":test_prediction})

test_result.to_csv("titanic_forsubmission.csv",index=False)

#最後に予測に効いた説明変数を求める。それぞれの貢献度合いをグラフに
feature_importances = pd.DataFrame({"feature_importances":model.feature_importances_})
sns.barplot(tr_test_X.columns,feature_importances["feature_importances"])
plt.show()






