import os
import yaml

def process_yaml_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        if data is None:
            return

        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)

        print(f"Processed file: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                process_yaml_file(file_path)

if __name__ == "__main__":
    target_directory = '../applications'  
    traverse_directory(target_directory)
