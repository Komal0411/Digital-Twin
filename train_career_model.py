import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data
df = pd.read_csv("data/career.csv")

# EXACT columns from SQL table
X = df[[
    "Skills",
    "Experience",
    "Projects_Completed",
    "Job_Applications"
]]

y = df["Performance_Score"]

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
model.fit(X, y)

# Save model
pickle.dump(model, open("models/career_model.pkl", "wb"))

print("Career model trained successfully")
