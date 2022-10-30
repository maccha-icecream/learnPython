import numpy as np
import pandas as pd

# Irisデータセット
iris_d = pd.read_csv('../csv/iris.csv')

# データセットのスライス
# print(iris_d[:5])
# print(iris_d[-5:])

# print(iris_d.iloc[0:5, 0:2])
# print(iris_d.loc[1:5, ['sepal_length', 'species']])

# 条件を指定して絞り込む
iris = iris_d[(iris_d['sepal_length'] > 7.0) & (iris_d['sepal_width'] < 3.0)]

# 列の追加と削除
iris_d['my_column'] = np.random.rand(len(iris_d.index))
iris_d.head(10)
del iris_d['my_column']
iris_d.head(10)

# 列を追加して新しいデータセットを作成
my_iris = iris_d.assign(my_column = np.random.rand(len(iris_d.index)))
# print(my_iris.head(10))
my_iris2 = my_iris.drop('my_column', axis=1)
# print(my_iris2.head(10))
# print(my_iris.head(10))

# 行の追加
row = pd.DataFrame([[1, 1, 1, 1, 'setosa']], columns=iris_d.columns)
my_iris3 = iris_d.append(row, ignore_index=True)

my_iris4 = my_iris3.drop(150)
# print(my_iris3[-2:])
# print(my_iris4[-2:])

# iris_dデータフレームの4つ列の値に基づいて昇順にソート
sorted_iris = iris_d.sort_values(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
# print(sorted_iris.head(10))

# iris_dデータフレームの4つ列の値に基づいて降順にソート
dec_sorted_iris = iris_d.sort_values(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], ascending=False)
# print(dec_sorted_iris.head(10))

# 統計量
# print(iris_d.describe())

# データの連結
concat_iris = pd.concat([iris_d[:5], iris_d[-5:]])
# print(concat_iris)

# 列方向に結合
concat_iris2 = pd.concat([iris_d.loc[:,['sepal_length']], iris_d.loc[:,['species']]], axis=1)
# print(concat_iris2.head(10))

# マージ
sepal_length = pd.concat([iris_d.loc[[0, 51, 101], ['sepal_length']], iris_d.loc[[0, 51, 101], ['species']]], axis=1)
sepal_width = pd.concat([iris_d.loc[[0, 51, 101], ['sepal_width']], iris_d.loc[[0, 51, 101], ['species']]], axis=1)
print(sepal_length)
print(sepal_width)
# 引数onにはキーとする列名を指定
# iris.csvの0, 51, 101行目から切り出したデータを'species'をキーに結合
sepal = pd.merge(sepal_length, sepal_width, on='species')
print(sepal)

# グループ集計
print(iris_d.groupby('species').mean())
