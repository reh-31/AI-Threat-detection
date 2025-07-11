# -*- coding: utf-8 -*-
"""Cyber_security.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q360P0AnE4D0r0JggQMpAF453hl2H5FB
"""

from google.colab import files

# Upload Parquet file
uploaded = files.upload()

# Get the filename
filename = list(uploaded.keys())[0]
print(f"Uploaded File: {filename}")

!pip install pandas pyarrow scikit-learn matplotlib scapy

import pandas as pd

# Read the uploaded parquet file
df = pd.read_parquet(filename)

# Preview the first few rows
print(df.head())

# Check dataset info
df.info()

# Ensure 'label' exists in the dataset
if 'label' not in df.columns:
    raise ValueError("Dataset does not contain a 'label' column!")

# Features (X) and labels (y)
X = df.drop(columns=['label'])
y = df['label']

X = pd.get_dummies(X)  # Convert categorical features to numeric

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training Data: {X_train.shape}, Testing Data: {X_test.shape}")

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Train the model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Show performance
print(classification_report(y_test, y_pred))

import joblib

# Save the model
joblib.dump(model, 'threat_detector.pkl')

# Download it locally
from google.colab import files
files.download('threat_detector.pkl')

print(f"Training dataset feature count: {len(X_train.columns)}")
print("Training feature names:", X_train.columns.tolist())