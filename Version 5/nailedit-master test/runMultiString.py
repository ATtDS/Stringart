import json
import subprocess
import sys

def run_configurations(config_file, script_name):
    # Load configurations from the JSON file
    with open(config_file, 'r') as file:
        configurations = json.load(file)

    # Iterate over each configuration and launch the script
    processes = []
    for idx, config in enumerate(configurations):
        # Save the current configuration to a temporary JSON file
        temp_config_file = f'temp_config_{idx}.json'
        with open(temp_config_file, 'w') as temp_file:
            json.dump(config, temp_file)

        # Launch the script using subprocess
        process = subprocess.Popen([sys.executable, script_name, temp_config_file])
        processes.append(process)
        print(f"Launched '{script_name}' with configuration {idx+1}")

    # Optionally wait for all processes to complete
    for process in processes:
        process.wait()
        print("Process ended with return code:", process.returncode)

if __name__ == '__main__':
    CONFIG_FILE = 'configurations.json'
    SCRIPT_NAME = 'nailedit.py'
    run_configurations(CONFIG_FILE, SCRIPT_NAME)
