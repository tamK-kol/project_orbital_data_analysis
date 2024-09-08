# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('SMA_data.csv')
data['Datetime'] = pd.to_datetime(data['Datetime'])

# Extract features
window_size = 60  
features = []
for i in range(len(data) - window_size):
    window = data.iloc[i:i+window_size]
    mean_sma = window['SMA'].mean()
    std_sma = window['SMA'].std()
    slope_sma = (window['SMA'].iloc[-1] - window['SMA'].iloc[0]) / window_size
    features.append([mean_sma, std_sma, slope_sma])

# Create labels
labels = np.zeros(len(features))
for i in range(len(labels)):
    if data.iloc[i+window_size]['SMA'] > data.iloc[i]['SMA'] + 0.1:
        labels[i] = 1  # maneuver detected

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train random forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.3f}')

# Plot detected maneuvers
detected_maneuvers = np.where(y_pred == 1)[0]
plt.plot(data['Datetime'], data['SMA'])
plt.scatter(data['Datetime'].iloc[detected_maneuvers + window_size], data['SMA'].iloc[detected_maneuvers + window_size], c='r')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
