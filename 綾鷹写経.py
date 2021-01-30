# 画像の読み込み

from PIL import Image
import os, glob  # 特定の形式（正規表現で”.jpg”を引っ張る）
import numpy as np
import random, math

root_dir = r"C:\Users\user\PycharmProjects\short_kogi_practice\potato-chips"
categories = ["consomme-punch", "kyusyu-shoyu", "norishio", "norishio-punch",
              "shiawase-butter", "shoyu-mayo", "usushio"]

X = []  # 画像データ
Y = []  # ラベルデータ


def make_sample(files):
    global X, Y
    X = []
    Y = []
    for cat, fname in files:
        add_sample(cat, fname)
    return np.array(X), np.array(Y)


def add_sample(cat, fname):
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((150, 150))
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)


allfiles = []

for idx, cat in enumerate(categories):
    image_dir = root_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    for f in files:
        allfiles.append((idx, f))

random.shuffle(allfiles)
th = math.floor(len(allfiles) * 0.8)
train = allfiles[0:th]
test = allfiles[th:]

X_train, y_train = make_sample(train)
X_test, y_test = make_sample(test)
xy = (X_train, X_test, y_train, y_test)
# np.save(r"C:\Users\user\PycharmProjects\short_kogi_practice\data_name.npy",xy)
import matplotlib.pyplot as plt
import japanize_matplotlib

index_name_list = []
plt.figure(figsize=(15, 2))

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(X_train[i, :, :], cmap="gray_r", )
    title_name = f"{i}番目の画像データ"
    plt.title(title_name)
    index_name_list.append(title_name)
plt.show()

import pandas as pd

print(len(y_train))
