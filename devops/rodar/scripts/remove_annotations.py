import os

def remover_anotacao_redirecionamento_ssl(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            linhas = file.readlines()

        with open(caminho_arquivo, 'w', encoding='utf-8') as file:
            for linha in linhas:
                if 'nginx.ingress.kubernetes.io/ssl-redirect' not in linha:
                    file.write(linha)
        
        print(f"Processado e atualizado: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")

def percorrer_diretorio(diretorio):
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                caminho_arquivo = os.path.join(root, file)
                remover_anotacao_redirecionamento_ssl(caminho_arquivo)

if __name__ == "__main__":
    diretorio_alvo = '../applications' 
    percorrer_diretorio(diretorio_alvo)
