import os
import yaml

def adjust_container_port(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        if data is None:
            return

        if 'ports' in data:
            for port_config in data['ports']:
                if port_config.get('name') == 'http' and 'containerPort' in port_config:
                    port_config['containerPort'] = "$PORT"

        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)

        print(f"Adjusted ports in file: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                adjust_container_port(file_path)

if __name__ == "__main__":
    target_directory = '../applications'  
    traverse_directory(target_directory)
