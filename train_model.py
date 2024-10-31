import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os
from utilities import data_processing

# Load raw data
df = data_processing.load_raw_data()

# Preprocess data
df = data_processing.preprocess_data(df)

# Save processed data
data_processing.save_processed_data(df, 'data/processed/processed_data1.csv')

# Prepare features and labels
X = df[['feature1_normalized', 'feature2_normalized', 'feature3_normalized']]
y = df['label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make predictions
predictions = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Ensure the models directory exists
if not os.path.exists('models'):
    os.makedirs('models')

# Save the trained model
joblib.dump(clf, 'models/depression_model.pkl')
print("Model saved to 'models/depression_model.pkl'")
