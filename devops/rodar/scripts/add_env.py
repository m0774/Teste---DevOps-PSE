import os
import yaml

def add_env_to_values_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        if data is None:
            return

        if os.path.basename(file_path) == 'values.yaml':
            if 'env' in data:
                data['env']['ENV'] = 'dev'
            else:
                data['env'] = {'ENV': 'dev'}

            with open(file_path, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, default_flow_style=False, sort_keys=False)

            print(f"Added ENV: dev to file: {file_path}")
        else:
            print(f"Ignoring file: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                add_env_to_values_yaml(file_path)

if __name__ == "__main__":
    target_directory = '../applications'  
    traverse_directory(target_directory)
