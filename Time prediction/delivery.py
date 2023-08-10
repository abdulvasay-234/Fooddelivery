import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("food_delivery.csv", encoding='latin1')

df.head()
