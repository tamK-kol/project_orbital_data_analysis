## Detecting Orbital Maneuvers Using SMA Data By Tamal Koley

### Introduction
The goal of this project is to develop an automatic method to detect orbital maneuvers, such as engine burns or orientation adjustments, using only the variation of the semi-major axis (SMA) over time. Maneuvers are identified based on significant changes in SMA, using machine learning to recognize these variations effectively.

### Methodology
1. Data Preprocessing

The dataset contains two columns: 'Datetime' and 'SMA.' The 'Datetime' column is converted to a timestamp format for ease of use in calculations. The data is then processed in windows of 60 intervals (equivalent to 1 hour), which is used as the basis for feature extraction.

2. Feature Extraction

For each window of data, we extract three features:
* Mean SMA: The average SMA value within the window.
* Standard Deviation of SMA: Measures the variability of SMA within the window.
* Slope of SMA: The rate of change of SMA over the window, calculated as the difference between the first and last SMA values divided by the window size.

These features are selected because they capture both the central tendency and the dynamics of SMA within the time window, which are indicative of potential maneuvers.

3. Labeling

Labels are created based on a simple heuristic: if the SMA value after the window is significantly larger (by more than 0.1 units) than the SMA at the start of the window, it is labeled as a maneuver (label = 1). Otherwise, it is labeled as a non-maneuver (label = 0).

4. Model Selection

A RandomForestClassifier was chosen due to its robustness in handling feature variability and its ability to capture non-linear relationships in the data. The model was trained on the extracted features with the corresponding labels.
The data was split into training (80%) and testing (20%) sets to evaluate the model’s performance. The accuracy score was used as the primary metric for assessing the model.

### Results
The model achieved an accuracy of 99.6% on the test set, indicating that it was highly effective at distinguishing between maneuver and non-maneuver events based on the features extracted from SMA data.

Below is a plot that highlights the detected maneuvers:

![alt text](image.png)


### Analysis
The RandomForestClassifier performed exceptionally well, with a high accuracy score. However, this performance may be due to the simplistic nature of the labeling strategy (i.e., a fixed threshold for SMA change). Future improvements could include:

* Tuning the threshold to reduce false positives/negatives.
* Experimenting with different window sizes to better capture short or long-term maneuvers.
* Introducing additional features such as velocity or orbital inclination to provide more context for maneuver detection.

While the model performs well on this dataset, its generalizability to different or noisier datasets may require further validation.

### Conclusion
This project demonstrates the viability of using machine learning, specifically RandomForestClassifier, for detecting orbital maneuvers based on SMA variation. The approach can accurately detect maneuvers with minimal feature engineering, though improvements could be made to enhance robustness. Future work will focus on refining the model and exploring other algorithms that may better capture subtle patterns in orbital maneuvering data.
