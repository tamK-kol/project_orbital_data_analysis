import pandas as pd

def detect_maneuvers(df, threshold=0.5):
    # Detect maneuvers by checking if the absolute SMA difference exceeds the threshold
    df['Maneuver'] = df['SMA_diff'].apply(lambda x: 1 if abs(x) > threshold else 0)
    return df

if __name__ == "__main__":
    # Load the feature data
    df = pd.read_csv("E:/My Work/Project/Dignatara/data/SMA_features.csv")
    
    # Detect maneuvers
    df = detect_maneuvers(df, threshold=0.5)
    
    # Save the detected maneuvers to a new CSV file
    df.to_csv("E:/My Work/Project/Dignatara/data/SMA_maneuvers.csv", index=False)
    print(df[df['Maneuver'] == 1].head())
