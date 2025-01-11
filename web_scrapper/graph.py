import asciichartpy
import time
import random
import os

# Settings for the graph
width = 50  # Width of the chart
height = 15  # Optional, controls scaling
history = []  # Store historical data
max_points = 100  # Maximum number of points to display

# Generate random data and update chart in real time
try:
    while True:
        # Append a new random data point
        new_value = random.randint(0, 100)
        history.append(new_value)

        # Keep only the most recent `max_points` data points
        if len(history) > max_points:
            history = history[-max_points:]

        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Render the graph
        chart = asciichartpy.plot(history, {'height': height, 'offset': 3})
        print(chart)

        # Wait before adding the next point
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Real-time graphing stopped.")