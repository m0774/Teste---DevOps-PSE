import os
import yaml

diretorioRaiz = 'INSIRA O CAMINHO PARA O DIRETÓRIO' 

def carregar_yaml(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            return yaml.safe_load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
    except yaml.YAMLError as e:
        print(f"Erro ao processar o arquivo YAML {caminho}: {e}")
    return None

def salvar_yaml(caminho, dados):
    try:
        with open(caminho, 'w') as arquivo:
            yaml.dump(dados, arquivo, default_flow_style=False)
        print(f"Configurações redis removidas de: {caminho}")
    except yaml.YAMLError as e:
        print(f"Erro ao salvar o arquivo YAML {caminho}: {e}")

def remover_redis_config(caminho):
    doc = carregar_yaml(caminho)
    if not doc:
        return

    if 'redisConfig' in doc:
        del doc['redisConfig']
    if 'redis' in doc:
        del doc['redis']

    salvar_yaml(caminho, doc)

def percorrer_diretorio(diretorio):
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith('.yaml'):
                caminho_completo = os.path.join(raiz, arquivo)
                remover_redis_config(caminho_completo)

percorrer_diretorio(diretorioRaiz)
