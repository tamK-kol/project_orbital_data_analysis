import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = load_data("E:/My Work/Project/Dignatara/data/SMA_data.csv")
    print(df)
