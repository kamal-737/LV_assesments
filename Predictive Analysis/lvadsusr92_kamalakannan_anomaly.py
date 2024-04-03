# -*- coding: utf-8 -*-
"""lvadsusr92_kamalakannan_anomaly.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k_DouyodsUUoDvhuRHmarqFwpaP3K-9Z
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Step 1: Read Data
df = pd.read_csv('/content/social_network.csv')

# Step 2: Data Preprocessing
# Handle missing values
df.fillna(0, inplace=True)  # Assuming missing values are replaced with 0

# Convert date columns to datetime format
df['account_creation_date'] = pd.to_datetime(df['account_creation_date'])

# Step 4: Exploratory Data Analysis (EDA)
# Summary Statistics
print("Summary Statistics:")
print(df.describe())

# Visualization
sns.pairplot(df)
plt.show()

# Step 5: Label Encoding for Categorical Columns
# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Perform label encoding for each categorical column
for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])

# Step 6: Anomaly Detection Algorithm
# Exclude datetime column before Feature Scaling
X = df.drop(['user_id', 'account_creation_date'], axis=1)

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Anomaly Detection using Isolation Forest
anomaly = IsolationForest(contamination=0.05, random_state=42)
anomalies = anomaly.fit_predict(X_scaled)

# Step 7: Flag Anomalies
df['anomaly_flag'] = np.where(anomalies == -1, 'Anomaly', 'Normal')

# Step 8: Further Investigation
# Further actions can be decided based on the 'anomaly_flag'

# Print flagged anomalies for further investigation
print("Flagged Anomalies:")
print(df[df['anomaly_flag'] == 'Anomaly'])