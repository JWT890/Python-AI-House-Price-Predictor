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

unique_values = []
for col in object_cols:
    unique_values.append(dataset[col].unique().size)
plt.figure(figsize=(10, 6))
plt.title('No. Unique values of Categorical Features')
plt.xticks(rotation=90)
sns.barplot(x=object_cols, y=unique_values)

plt.figure(figsize=(18, 36))
plt.title('Categorical Features: Distribution')
plt.xticks(rotation=90)
index = 1

for col in object_cols:
    y = dataset[col].value_counts()
    plt.subplot(11, 4, index)
    plt.xticks(rotation=90)
    sns.barplot(x=list(y.index), y=y)
    index += 1

from sklearn.preprocessing import OneHotEncoder

dataset.drop(['Id'],
			axis=1,
			inplace=True)
dataset['SalePrice'] = dataset['SalePrice'].fillna(
dataset['SalePrice'].mean())
new_dataset = dataset.dropna()
new_dataset.isnull().sum()

