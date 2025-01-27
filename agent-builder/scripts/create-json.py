import os
import re
import json

# Define the source and target directories
source_dir = "/home/daniel/Git/ai-assistant-template/system-prompts"
target_dir = "/home/daniel/Git/ai-assistant-template/finished-configs"

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Function to extract version number from filenames
def extract_version(filename):
    match = re.search(r'v(\d+)\.md', filename, re.IGNORECASE)
    return int(match.group(1)) if match else 0

# Find all configuration files and extract their versions
config_files = [f for f in os.listdir(source_dir) if f.lower().endswith('.md')]
config_files.sort(key=extract_version, reverse=True)

if not config_files:
    print("No configuration files found.")
else:
    # Get the latest configuration file
    latest_file = config_files[0]
    latest_version = extract_version(latest_file)
    print(f"Latest configuration file: {latest_file} (v{latest_version})")

    # Read the content of the latest configuration file
    with open(os.path.join(source_dir, latest_file), 'r') as file:
        content = file.read()

    # Convert the content to JSON (assuming the content is plain text)
    json_content = {"content": content}

    # Define the output JSON file path
    output_file = os.path.join(target_dir, latest_file.replace('.md', '.json'))

    # Write the JSON content to the output file
    with open(output_file, 'w') as json_file:
        json.dump(json_content, json_file, indent=4)

    print(f"Configuration exported to: {output_file}")