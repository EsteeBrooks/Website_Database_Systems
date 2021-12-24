import numpy as np
import pandas as pd

iris = pd.read_csv("PycharmProjects/PythonProject/iris.data")
# print(iris.head())
# print(iris.assign(sepal_ratio=iris["SepalWidth"] / iris["SepalLength"]).head())
# # Use a function to assign the new column values:
# print(iris.assign(sepal_ratio=lambda x: (x["SepalWidth"] / x["SepalLength"])).head())
(iris.query("SepalLength > 5")
    .assign(
        SepalRatio=lambda x: x.SepalWidth / x.SepalLength,
        PetalRatio=lambda x: x.PetalWidth / x.PetalLength,
).plot(kind="scatter", x="SepalRatio", y="PetalRatio"))