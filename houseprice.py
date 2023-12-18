import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("HousePricePrediction.xlsx")

dataset.shape

obj = (dataset.dtypes == 'object')
object_cols = list(obj[obj].index)
print("Categorical variables: ", len(object_cols))

dataset.shape

int_ = (dataset.dtypes == 'int')
num_cols = list(int_[int_].index)
print("Integer variables: ", len(num_cols))

fl = (dataset.dtypes == 'float')
fl_cols = list(fl[fl].index)
print("Float variables: ", len(fl_cols))


