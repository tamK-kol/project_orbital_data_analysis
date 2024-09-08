from scripts.data_preprocessing import load_data
from scripts.feature_extraction import extract_features
from scripts.maneuver_detection import detect_maneuvers
from scripts.result_visualization import visualize_results

def main():
    # Load the raw data
    df = load_data("E:/My Work/Project/Dignatara/data/SMA_data.csv")
    
    # Extract features
    df = extract_features(df)
    
    # Detect maneuvers
    df = detect_maneuvers(df, threshold=0.5)
    
    # List of reference maneuver dates
    reference_dates = [
        "2018-05-03",
        "2018-10-11",
        "2019-03-27",
        "2019-05-17",
        "2019-09-11",
        "2019-11-01"
    ]
    
    # Add reference dates to the DataFrame for visualization
    df['Reference Dates'] = df['Date'].apply(lambda x: x.strftime("%Y-%m-%d") in reference_dates)
    
    # Visualize results
    visualize_results(df, reference_dates)

if __name__ == "__main__":
    main()
