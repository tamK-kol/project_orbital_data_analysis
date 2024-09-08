import pandas as pd

def extract_features(df):
    # Calculate the difference between consecutive SMA values
    df['SMA_diff'] = df['SMA'].diff()
    
    # Drop the first row with NaN due to the diff operation
    df = df.dropna().reset_index(drop=True)

    return df

if __name__ == "__main__":
    # Load the data
    df = pd.read_csv("E:/My Work/Project/Dignatara/data/SMA_data.csv")
    
    # Extract features
    df = extract_features(df)
    
    # Save the features to a new CSV file for later use
    df.to_csv("E:/My Work/Project/Dignatara/data/SMA_features.csv", index=False)
    print(df.head())
