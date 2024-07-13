import os

def update_version_in_file(file_path, old_versions, new_version):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                for old_version in old_versions:
                    if f'version: {old_version}' in line:
                        line = line.replace(f'version: {old_version}', f'version: {new_version}')
                file.write(line)
        
        print(f"Updated version in: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def traverse_directory(directory, old_versions, new_version):
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'kustomization.yaml':
                file_path = os.path.join(root, file)
                update_version_in_file(file_path, old_versions, new_version)

if __name__ == "__main__":
    target_directory = '../applications'
    old_versions = ['2.2.0', '2.1.0', '1.0.1']
    new_version = '2.2.1'
    traverse_directory(target_directory, old_versions, new_version)
