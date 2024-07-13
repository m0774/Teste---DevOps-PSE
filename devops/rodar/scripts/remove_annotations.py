import os

def remove_ssl_redirect_annotation(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                if 'nginx.ingress.kubernetes.io/ssl-redirect' not in line:
                    file.write(line)
        
        print(f"Processed and updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                remove_ssl_redirect_annotation(file_path)

if __name__ == "__main__":
    target_directory = '../applications' 
    traverse_directory(target_directory)
