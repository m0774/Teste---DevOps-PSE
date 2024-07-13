import os
import yaml

def remove_duplicates(data):
    if isinstance(data, list):
        unique_list = []
        seen = set()
        for item in data:
            item_str = yaml.dump(item)
            if item_str not in seen:
                seen.add(item_str)
                unique_list.append(item)
        return unique_list
    elif isinstance(data, dict):
        unique_data = {}
        for key, value in data.items():
            unique_data[key] = remove_duplicates(value)
        return unique_data
    else:
        return data

def process_yaml_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        if data is None:
            return

        unique_data = remove_duplicates(data)

        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(unique_data, file, default_flow_style=False, sort_keys=False)

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
