# 2025.3.10
# 프로젝트2 붓꽃분류기 만들기

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

iris_df = pd.read_csv('iris.csv')

y = iris_df['species']
X = iris_df.drop('species', axis=1)

kn = KNeighborsClassifier()
model = kn.fit(X, y)

# X_new = np.array([[3,3,3,3]])
# kn ['versicolor'] [[0.  0.8 0.2]]

# X_new = np.array([[1, 4.2, 1.4, 7]])
# kn ['versicolor'] [[0.2 0.6 0.2]]

X_new = np.array([[1, 4.2, 1.4, 7]])
predict = model.predict(X_new)

probability = model.predict_proba(X_new)

print(predict)
print(probability)
