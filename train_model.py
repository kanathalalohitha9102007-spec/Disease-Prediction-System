import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Dataset
data = {
    "fever": [1,1,0,1,0],
    "cough": [1,0,1,1,0],
    "headache": [1,1,0,0,1],
    "fatigue": [1,0,1,1,0],
    "disease": ["Flu","Cold","Allergy","Flu","Migraine"]
}

df = pd.DataFrame(data)

X = df.drop("disease", axis=1)
y = df["disease"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save files
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(list(X.columns), open("symptoms.pkl", "wb"))

print("✅ Model and symptoms saved successfully!")