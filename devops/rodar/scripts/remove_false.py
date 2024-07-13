import os
import yaml

def remove_disabled_fields(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        if data is None:
            return

        # Verifica se existe a chave 'enabled' e se seu valor é False (em minúsculo)
        if 'enabled' in data and data['enabled'] is False:
            # Remove campos adicionais dentro da configuração
            for key in list(data.keys()):
                if key != 'enabled':
                    del data[key]

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
                remove_disabled_fields(file_path)

if __name__ == "__main__":
    target_directory = '../applications'  # Substitua pelo caminho do seu diretório
    traverse_directory(target_directory)
