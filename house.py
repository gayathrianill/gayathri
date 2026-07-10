import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/home/sngce/safna/housing.csv")
print(df)
print(df.shape)
print(df.head(10))
print(df.tail(10))
print(df.columns)
print(df['total_rooms'])
x=df['total_rooms'].head(150).values.reshape(-1,1)
y=df['total_rooms'].head(150).values.reshape(-1,1)
plt.scatter(x,y)
plt.xlabel("total rooms")
plt.ylabel("median house value")
plt.title("total rooms vs median house value")
plt.show()
print(df.describe())