import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv('data/behavior.csv')

X = df[['Productivity_Score','Social_Interactions','Habits','Focus','Consistency','Motivation']]
y = df['Emotional_Score']

model = RandomForestRegressor()
model.fit(X, y)

pickle.dump(model, open('models/behavior_model.pkl', 'wb'))
print("Behavior model trained!")
