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


df['Type_of_order'].unique()

df['Type_of_order'].value_counts()

plt.figure(figsize=(15,6))
sns.countplot(x='Type_of_order', data=df, palette='hls')
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(15, 6))
counts = df['Type_of_order'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=sns.color_palette('hls'))
plt.title('Type_of_order')
plt.show()

import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(x=df['Type_of_order'].value_counts().index, y=df['Type_of_order'].value_counts())])
fig.update_layout(
        title= 'Type_of_order',
        xaxis_title="Categories",
        yaxis_title="Count"
    )
fig.show()

counts = df['Type_of_order'].value_counts()
fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts)])
fig.update_layout(title= 'Type_of_order')
fig.show()

df['Type_of_vehicle'].unique()

df['Type_of_vehicle'].value_counts()

plt.figure(figsize=(15,6))
sns.countplot(x='Type_of_vehicle', data=df, palette='hls')
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(15, 6))
counts = df['Type_of_vehicle'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=sns.color_palette('hls'))
plt.title('Type_of_vehicle')
plt.show()

fig = go.Figure(data=[go.Bar(x=df['Type_of_vehicle'].value_counts().index, y=df['Type_of_vehicle'].value_counts())])
fig.update_layout(
        title= 'Type_of_vehicle',
        xaxis_title="Categories",
        yaxis_title="Count"
    )
fig.show()


counts = df['Type_of_vehicle'].value_counts()
fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts)])
fig.update_layout(title= 'Type_of_vehicle')
fig.show()

for i in numerical_columns:
    plt.figure(figsize=(15,6))
    sns.histplot(df[i], kde = True, bins = 20, palette = 'hls')
    plt.xticks(rotation = 90)
    plt.show()
for i in numerical_columns:
    plt.figure(figsize=(15,6))
    sns.distplot(df[i], kde = True, bins = 20)
    plt.xticks(rotation = 90)
    plt.show()
  
for i in numerical_columns:
    plt.figure(figsize=(15, 6))
    sns.boxplot(x=i, data=df, palette='hls')
    plt.xticks(rotation=90)
    plt.show()

for i in numerical_columns:
    plt.figure(figsize=(15,6))
    sns.violinplot(x = i, data = df, palette = 'hls')
    plt.xticks(rotation = 90)
    plt.show()

#30

