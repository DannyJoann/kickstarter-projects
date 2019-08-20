import pandas as pd
import numpy as np
from mlxtend.preprocessing import minmax_scaling
from sklearn.preprocessing import MinMaxScaler

data_to_scale = pd.read_csv("../preprocessing_file/kickstarter_token.csv", delimiter=";", low_memory=False)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data_to_scale)
np.savetxt('../preprocessing_file/kickstarter_scaled.csv', scaled_data, delimiter=";")
