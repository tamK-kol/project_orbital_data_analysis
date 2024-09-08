import pandas as pd
import matplotlib.pyplot as plt

def visualize_results(df):
    # Plot the SMA values for all points
    plt.figure(figsize=(10, 6))
    plt.plot(df['Datetime'], df['SMA'], label='SMA', alpha=0.5)

    # Filter the data to only include points where Maneuver is 1
    maneuver_points = df[df['Maneuver'] == 1]

    # Highlight the maneuver points
    plt.scatter(maneuver_points['Datetime'], maneuver_points['SMA'], color='red', label='Detected Maneuvers', zorder=5)

    # Set the x-axis to the Datetime values
    plt.xlabel('Datetime')
    plt.ylabel('SMA')
    plt.title('Orbital Data with Detected Maneuvers')
    plt.legend()
    plt.tight_layout()

    # Save the plot
    plt.savefig("E:/My Work/Project/Dignatara/results/orbital_data_with_maneuvers.png")
    plt.show()

# Load the data
df = pd.read_csv("E:\My Work\Project\Dignatara\data\SMA_maneuvers.csv")

# Visualize the results
visualize_results(df)