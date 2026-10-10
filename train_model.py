import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

# Input features
X = data.drop("Career", axis=1)

# Target
y = data["Career"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model trained successfully!")
print("Accuracy:", accuracy)

# Create models folder
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/career_model.pkl")

print("Model saved successfully!")
print("Location: models/career_model.pkl")