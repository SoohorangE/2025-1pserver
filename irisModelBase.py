# 2025.3.10
# 프로젝트2 붓꽃분류기 만들기
import joblib
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

iris_df = pd.read_csv('iris.csv')

y = iris_df['species']
X = iris_df.drop('species', axis=1)

kn = KNeighborsClassifier()
model_kn = kn.fit(X, y)
rfc = RandomForestClassifier()
model_rfc = rfc.fit(X, y)

joblib.dump(model_rfc, 'model_rfc.pkl')
joblib.dump(model_kn, 'model_kn.pkl')

# X_new = np.array([[3,3,3,3]])
# kn ['versicolor'] [[0.  0.8 0.2]]

# X_new = np.array([[1, 4.2, 1.4, 7]])
# kn ['versicolor'] [[0.2 0.6 0.2]]

# X_new = np.array([[1, 4.2, 1.4, 7]])
# kn ['versicolor'] [[0.2 0.6 0.2]]
# rfc ['setosa'] [[0.5  0.22 0.28]]

X_new = np.array([[5.0, 3.4, 1.4, 0.2]])
# kn ['setosa'][[1. 0. 0.]]
# rfc ['setosa'][[1. 0. 0.]]

model_kn = joblib.load('model_kn.pkl')
model_rfc = joblib.load('model_rfc.pkl')

kn_predict = model_kn.predict(X_new)
rfc_predict = model_rfc.predict(X_new)

kn_probability = model_kn.predict_proba(X_new)
rfc_probability = model_rfc.predict_proba(X_new)

print(kn_predict)
print(kn_probability)

print(rfc_predict)
print(rfc_probability)
