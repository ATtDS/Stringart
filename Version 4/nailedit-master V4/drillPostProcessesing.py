# Define the path for the original and modified G-code files
original_file_path = '/Users/eliasabouchaaya/Desktop/adav30_drills.tap'
modified_file_path = 'ada30mod.gcode'

# Open the original G-code file
with open(original_file_path, 'r') as file:
    lines = file.readlines()

# Initialize an empty list to hold the modified G-code
modified_lines = []

# Variables to track the state
is_drilling_cycle = False
i = 0
for line in lines:
    i= i+1
    stripped_line = line.strip()
    print(i)
    # Check if the line is the start of a G81 drilling cycle
    if stripped_line.startswith('G98 G81'):
        is_drilling_cycle = True
        # Extract the Z-depth and feed rate for drilling from this line
        depth = stripped_line.split(' Z')[1].split(' ')[0]
        feed_rate = stripped_line.split(' F')[1]
        continue  # Skip adding this line to the modified G-code
    
    # Check if we are in a drilling cycle and the line specifies an X, Y position
    if is_drilling_cycle and stripped_line.startswith('X'):
        x_pos = stripped_line.split(' ')[0]
        y_pos = stripped_line.split(' ')[1]
        
        # Add G-code to move up to safe height, move to position, drill, and retract
        modified_lines.append('G0 Z15.00\n')  # Move up to safe height
        modified_lines.append(f'G0 {x_pos} {y_pos}\n')  # Move to X, Y position
        modified_lines.append(f'G1 Z{depth} F{feed_rate}\n')  # Drill down
        modified_lines.append('G0 Z15.00\n')  # Retract to safe height
    else:
        # Add the current line to the modified G-code
        modified_lines.append(line)
        # If the line is an M code or similar, we assume the drilling cycle is over
        if stripped_line.startswith('M'):
            is_drilling_cycle = False

# Write the modified G-code to a new file
with open(modified_file_path, 'w') as file:
    file.writelines(modified_lines)

print(f'Modified G-code has been saved to {modified_file_path}.')
