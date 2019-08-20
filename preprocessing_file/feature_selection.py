import pandas as pd
import numpy as np
import datetime as t
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

dataframe = pd.read_csv("../preprocessing_file/kickstarter_token.csv", delimiter=";", low_memory=False)
array = dataframe.values
# print(array)
X = array[:, 0:-1]
Y = array[:, -1]
model = ExtraTreesClassifier()
print('start of fitting '.format(t.datetime.now()))
model.fit(X, Y)
print('end of fitting '.format(t.datetime.now()))
np.savetxt('../preprocessing_file/kickstarter_feature_importance.csv', model.feature_importances_, delimiter=";")

# model = SelectKBest(score_func=chi2, k='all')
# print('start of fitting '.format(t.datetime.now()))
# f_importance = model.fit(X, Y)
# print('end of fitting '.format(t.datetime.now()))
# np.savetxt('../kickstarter_feature_importance.csv', f_importance.scores_, delimiter=";")
