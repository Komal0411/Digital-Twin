import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('data/wellness.csv')

X = df[['Sleep_Hours','Exercise_Hours','Mood','Stress_Level']]
y = df['Wellness_Index']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('models/wellness_model.pkl', 'wb'))
print("Wellness model trained!")
