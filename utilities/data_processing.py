import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_raw_data():
    # Load your data from 'data/raw/study1_data.csv'
    df = pd.read_csv('data/raw/study1_data.csv')
    return df

def preprocess_data(df):
    scaler = StandardScaler()
    features = ['feature1', 'feature2', 'feature3']
    # Normalize and rename the columns to include '_normalized'
    normalized_features = scaler.fit_transform(df[features])
    normalized_df = pd.DataFrame(normalized_features, columns=[f"{feature}_normalized" for feature in features])
    df = pd.concat([df.drop(columns=features), normalized_df], axis=1)
    return df

def save_processed_data(df, filepath):
    # Save the processed data to 'data/processed/processed_data1.csv'
    df.to_csv(filepath, index=False)
