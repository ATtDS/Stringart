import random
import json

# Calculate meters per pixel
mpp = 0.3 / 600

# Define a base configuration for string art generation
base_config = {
    "proc_width": 600,
    "proc_height": 600,
    "ppi": mpp,
    "backgroundColor": 0,
    "currentPoint": 0,
    "lastPoint": -1,
    "start_at": (0.5, 0),
    "inputImagePath": "ada.png",
    "edgesImagePath": "edges.jpeg",
    "backgroundColor":0,                      # canvas color
    "threadColor":(255, 160), 
    "nailDiameter": 1.5 / 1000.0 / (0.3 / 600)
}

# List to hold all configurations
configurations = []

# Define ranges for each variable parameter
parameter_ranges = {
    "searchRadius": (0.1, 0.40),
    "nailDistMin": lambda mpp: (9 / 1000.0 / mpp, 12 / 1000.0 / mpp),
    "nailDistMax": lambda mpp: (15 / 1000.0 / mpp, 25 / 1000.0 / mpp),
    "edgeThreshold": (0.05, 0.3),
    "maxSegmentConnect": (1, 4),
    "maxConnectsPerNail": (3, 10),
    "blurAmount": (1.0, 9.0),
    "img_contrast": (0.5, 1.5),
    "img_brightness": (0.5, 1.5),
    "img_invert": (0, 1),
    "maxIterations": (2000, 7000)
}

# Generate 30 variations
for i in range(20):
    config = base_config.copy()
    for key, value_range in parameter_ranges.items():
        if callable(value_range):
            value_range = value_range(mpp)
        if isinstance(value_range, list):
            config[key] = random.choice(value_range)
        else:
            config[key] = random.uniform(*value_range)
    configurations.append(config)

# Convert configurations to JSON and save to a file
with open('configurations.json', 'w') as f:
    json.dump(configurations, f, indent=4)

print("Configurations have been saved to 'configurations.json'.")
