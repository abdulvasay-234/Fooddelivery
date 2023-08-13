import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("food_delivery.csv", encoding='latin1')

df.head()

df.tail()

df.shape

df.columns

df.duplicated().sum()

df.isnull().sum()

df.info()

df.describe()

df.nunique()
object_columns = df.select_dtypes(include='object').columns
print("Object Columns:")
print(object_columns)
print()

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
print("Numerical Columns:")
print(numerical_columns)

#13
