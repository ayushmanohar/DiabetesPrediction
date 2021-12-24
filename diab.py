import pandas as pd
import numpy as np
import warnings
import pickle
warnings.filterwarnings("ignore")
data = pd.read_csv('diabetes.csv')
data.head()
data.shape
data.describe()
data.columns[data.isna().any()]
print(data.apply(lambda col: col.unique()))
data
Target = data.Outcome
data  = data.drop(['Outcome'], axis='columns')
data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, Target, test_size =0.2)
len(x_train)
from sklearn.svm import SVC
svm = SVC()
svm.fit(x_train, y_train)
pickle.dump(svm,open('model.pkl','wb'))