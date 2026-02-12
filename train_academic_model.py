import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the CSV
df = pd.read_csv('data/academic.csv')

# Features and target
X = df[['Hours_Studied', 'Attendance', 'Internal_Score']]
y = df['Exam_Score']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('models/academic_model.pkl', 'wb'))
print("Academic model trained and saved!")
