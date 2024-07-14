import os
import yaml

def atualizar_resources(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            dados = yaml.safe_load(file)
        
        if dados is None:
            return

        if 'resources' in dados:
            if 'limits' in dados['resources'] and 'cpu' in dados['resources']['limits']:
                dados['resources']['limits']['cpu'] = '100m'
            if 'requests' in dados['resources'] and 'cpu' in dados['resources']['requests']:
                dados['resources']['requests']['cpu'] = '10m'

        with open(caminho_arquivo, 'w', encoding='utf-8') as file:
            yaml.dump(dados, file, allow_unicode=True, default_flow_style=False, sort_keys=False)

        print(f"Recursos atualizados no arquivo: {caminho_arquivo}")
    except yaml.YAMLError as e:
        print(f"Erro ao analisar YAML no arquivo: {caminho_arquivo} - {e}")
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")

def percorrer_diretorio(diretorio):
    print(f"Iniciando a verificação no diretório: {diretorio}")
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file == 'values.yaml':
                caminho_arquivo = os.path.join(root, file)
                print(f"Processando arquivo: {caminho_arquivo}")
                atualizar_resources(caminho_arquivo)
    print("Verificação concluída.")

if __name__ == "__main__":
    diretorio_alvo = '../applications' 
    if os.path.exists(diretorio_alvo) and os.path.isdir(diretorio_alvo):
        percorrer_diretorio(diretorio_alvo)
    else:
        print(f"Diretório especificado não existe ou não é um diretório: {diretorio_alvo}")
