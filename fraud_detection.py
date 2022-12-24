import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
%matplotlib inline
#import csv file
df = pd.read_csv('creditcard.csv')
print(df.shape)
df.head()
