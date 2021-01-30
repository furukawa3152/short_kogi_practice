import pandas as pd

df = pd.DataFrame(
    {"Name": ["Bob", "Ken", "Tom"],
     "Age": [22, 35, 58],
     "Sex": ["male", "male", "female"]}
)
ages = pd.Series([22, 35, 58], name="Age")  # 行のみ用意

# print(df.describe())#数値の分析
# print(df.describe(include=["O"]))#数値以外への分析

titanic = pd.read_csv("data/titanic.csv")  # CSVを読み込む
# titanic.to_excel("titanic.xlsx",sheet_name="passenger",index=False)#Excelに吐き出す

# ages = titanic["Age"]#一列抜き取る
# print(ages.head)
# type(ages)#Series

# print(ages.shape)#桁数

# age_sex = titanic[["Age","Sex"]]#二列抜き取る（データフレームに）
# print(age_sex.shape)
# type(age_sex)#DataFrame

above_35 = titanic[titanic["Age"] > 35]
# print(above_35.describe())

# class_23 =titanic[titanic["Pclass"].isin([2,3])] #列名Pclassのなかに2,3を含むものを抽出
# print(class_23)
# print(class_23["Pclass"].value_counts()) #class_23のPclassのそれぞれの個数をカウント
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]  # 上のisinを使った文と同じ。| （パイプ）はorという意味

age_no_na = titanic[titanic["Age"].notna()]  # 欠損値を省く

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]  # Ageが35以上の人のName列を取得
# print(type(adult_names))

adult_names_age = titanic.loc[titanic["Age"] > 20, ["Name", "Age"]]  # Ageが35以上の人のName列とAge列を取得リスト内の順列は元データと同じ必要
# print(adult_names_age.describe())

# print(titanic.iloc[9:25,2:5])#行と列を指定して取得
# print(titanic.columns)

titanic.iloc[0:3, 3] = "anonymous"  # 代入
# print(titanic.head())

import matplotlib.pyplot as plt

# air_quality = pd.read_csv("data/air_quality_no2.csv",index_col=0,parse_dates=True)#時系列データをいい感じにさせるための設定

# air_quality["station_antwerp"].plot()
# air_quality.plot.scatter(x="station_london",#散布図
#                          y="station_paris",
#                          alpha=0.2)
# air_quality.plot.box()#箱ひげ図
# axs =air_quality.plot.area(figsize=(12,4),subplots=False)#面グラフ（subplotsがTrueだと分ける）
# axs =air_quality[["station_antwerp","station_london"]].plot.area(figsize=(12,4),subplots=True)#要素を抜き出す
# fig,axs =plt.subplots(figsize=(12,4));
# air_quality.plot.area(ax=axs)#このあたりfor文使ってグラフ大量生産も可能
# axs.set_ylabel("No$_2$ concentration");#y軸に命名
# fig.savefig("no2_concentrations.png")#画像として保存
# plt.show()#この表記で描画。

air_quality = pd.read_csv("data/air_Quality_no2.csv", index_col=0, parse_dates=True)
air_quality["london_mg_per_cubic"] = air_quality[
                                         "station_london"] * 1.882  # london_mg_per_cubicという行を新しく作成（station_londonに1.882をかけたもの）

# print(air_quality.head(3))

air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]  # 列どうしの計算も可能
air_quality_renamed = air_quality.rename(
    columns={"station_antwerp": "BETR.801",
             "station_paris": "FRO4014",
             "station_london": "London_Westminster"}
)
air_quality_renamed = air_quality.rename(columns=str.lower)

# print(air_quality_renamed.head(3))

# print(titanic["Age"].mean())#Ageの平均値を出す

# print(titanic[["Age","Fare"]].median())#中央値

# print(titanic.agg({"Age":["min","max","median","skew"],
#                    "Fare":["min","max","median","mean"]}))#それぞれのデータ

# print(titanic[["Sex","Age"]].groupby("Sex").mean())#性別でグルーピングした年齢の平均値

# print(titanic.groupby("Sex").mean())#性別ごとの全データ平均
# print(titanic.groupby("Sex")["Age"].mean())

# print(titanic)

# print(titanic.groupby(["Sex","Pclass"])["Fare"].mean()) #SexごとのPclassのFare平均値

# print(titanic["Pclass"].value_counts())#Pclassの個数

# print(titanic.groupby("Pclass")["Pclass"].count())

air_quality_long = pd.read_csv("data/air_quality_no2_long.csv",
                               index_col="date.utc", parse_dates=True)
# print(air_quality_long.head(3))

# print(titanic.head(3)？

# print(titanic.sort_values(by="Age").head(3))#Ageでソート
# print(titanic.sort_values(by=["Pclass","Age"],ascending=False).head(3))#複数条件でソート

# print(titanic.sort_values(by=["Age","Pclass"],ascending=False).head(3))#複数条件でソート

# no2 =air_quality_long[air_quality_long["parameter"] =="no2"]
# print(no2["parameter"].value_counts())

# no2_subset =no2.sort_index().groupby(["location"]).head(100)

# no2_subset.pivot(columns = "location",values="value").plot()
# print(air_quality_long.pivot_table(values="value", index="location",
#                                    columns="parameter", aggfunc="mean", margins=True))
# plt.show()

air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv",
                              parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv",
                               parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value", ]]
# print(air_quality_pm25.head())
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)  # ファイルを結合
# print(air_quality["parameter"].value_counts())

# print("pm25:",air_quality_pm25.shape[0]) #pm25: 1110
# print("no2:",air_quality_no2.shape[0]) #no2: 2068
# print("concat:",air_quality.shape[0])  #concat: 3178

air_quality = air_quality.sort_values("date.utc")  # 混ざったデータを日付順でソート
# print(air_quality.head())

air_quality = pd.concat([air_quality_pm25, air_quality_no2],
                        keys=["いたる", "さちょみ"])  # インデックスをつけて結合
air_quality.reset_index()
# print(air_quality.head())
stations_coord = pd.read_csv("data/air_quality_stations.csv")

air_quality = pd.merge(air_quality, stations_coord, how="left"
                       , on="location")  # 左側（air_quality）が基準。locationのデータを基準に突合。
# print(air_quality.head())

air_quality = pd.read_csv("data/air_quality_no2_long.csv")
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
# print(air_quality.city.unique())#cityの行のユニーク値を取得

# print(air_quality.info())#この時点でdatetimeはobject
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
# print(air_quality.info()) #datetimeはdatetime64という時間データになった。

# print(air_quality["datetime"].min()-air_quality["datetime"].max()) #時間データなので引き算も可能

air_quality["month"] = air_quality["datetime"].dt.month #month行を作成
# print(air_quality.head())

# print(air_quality.groupby(
#     [air_quality["datetime"].dt.weekday,"location"]
# )["value"].mean())#週ごとの平均を集計

fig,axs = plt.subplots(figsize=(12,4))
air_quality.groupby(
    air_quality["datetime"].dt.hour)["value"]\
    .mean().plot(kind="bar",rot=0,ax=axs)

no2 =air_quality.pivot(index="datetime",columns="location",values="value")#駅ごとの内容を集計
#
# plt.show()

# print(no2["2019-05-20":"2019-05-21"])

monthly_max =no2.resample('M').max()
print(monthly_max)