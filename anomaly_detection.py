import matplotlib.pyplot as plt
from collections import deque

window_size = 10  # Adjust the window size as needed
data_stream = deque(maxlen=window_size)
z_scores = []
threshold = 2.5  # Set an appropriate threshold for anomaly detection

def calculate_z_score(value):
    mean = (sum(data_stream) )/ len(data_stream)
    std_dev = (sum((x - mean) ** 2 for x in data_stream) / len(data_stream)) ** 0.5
    z_score = (value - mean) / std_dev if std_dev != 0 else 0
    return z_score

while True:
    user_input = (input("Enter a data point (or type 'exit' to stop): "))
    
    if user_input == 'exit':
        break
    
    data_stream.append(float(user_input))
    z_score = calculate_z_score(float(user_input))
    z_scores.append(z_score)
    
    if abs(z_score) > threshold:
        print(f"Anomaly detected: {user_input}")
    plt.plot(z_scores, label='Z Scores')
    plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
    plt.xlabel('Data Points')
    plt.ylabel('Z Score')
    plt.legend()
    plt.show()    